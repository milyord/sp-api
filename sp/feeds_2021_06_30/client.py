import ssl
from dataclasses import dataclass, field, replace
from datetime import datetime
from typing import Dict, Literal, Mapping, Union

import boto3
import httpx
from httpx_auth_awssigv4 import SigV4Auth

GRANT_TYPE: str = "refresh_token"
LWA_ENDPOINT: str = "https://api.amazon.com/auth/o2/token"
BASE_URL_HEAD: str = "https://sellingpartnerapi"
REGIONS: Mapping[str, str] = dict(na="us-east-1", eu="eu-west-1", fr="us-west-1")


@dataclass
class Client:
    """A class for keeping track of data related to the API

    Attributes:
      region: The api region for conscructing the base url
      refresh_token: Aquired through Developer Central when an app is first created and then authorized
      lwa_client_id: Developer Central under LWA Credentials after creating an app
      lwa_client_secret: Developer Central under LWA Credentials after creating an app
      aws_access_key_id: Aquired in AWS during IAM Setup
      aws_secret_access_key: Aquired in AWS during IAM Setup
      role_arn: Aquired in AWS during IAM Setup
      cookies: A dictionary of cookies to be sent with every request
      headers: A dictionary of headers to be sent with every request
      timeout: The maximum amount of a time in seconds a request can take. API functions will raise
        httpx.TimeoutException if this is exceeded.
      verify_ssl: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.
      raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
        status code that was not documented in the source OpenAPI document.
    """

    refresh_token: str
    lwa_client_id: str
    lwa_client_secret: str
    aws_access_key_id: str
    aws_secret_access_key: str
    role_arn: str
    base_url: str = field(init=False, default=f"{BASE_URL_HEAD}-us.amazon.com")
    auth: SigV4Auth = field(init=False)
    region: Literal["na", "fr", "eu"] = field(default="na")
    cookies: Dict[str, str] = field(default_factory=dict, kw_only=True)
    headers: Dict[str, str] = field(init=False)
    timeout: float = field(kw_only=True, default=5.0)
    verify_ssl: Union[str, bool, ssl.SSLContext] = field(kw_only=True, default=True)
    raise_on_unexpected_status: bool = field(kw_only=True, default=True)

    def __post_init__(
        self,
    ) -> None:
        self.base_url = f"{BASE_URL_HEAD}-{self.region}.amazon.com"

        LWA = httpx.post(
            url=LWA_ENDPOINT,
            data={
                "grant_type": GRANT_TYPE,
                "refresh_token": self.refresh_token,
                "client_id": self.lwa_client_id,
                "client_secret": self.lwa_client_secret,
            },
        ).json()

        self.headers = {
            "user-agent": "sp-api",
            "x-amz-access-token": LWA["access_token"],
            "x-amz-date": datetime.utcnow().strftime("%Y%m%dT%H%M%SZ"),
            "content-type": "application/json",
        }

        # fetch temporary credentials from AWS STS service
        sts = boto3.Session().client(
            "sts",
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
        )

        sts_credentials = sts.assume_role(RoleArn=self.role_arn, RoleSessionName="httpxcall")["Credentials"]

        self.auth = SigV4Auth(
            access_key=sts_credentials["AccessKeyId"],
            secret_key=sts_credentials["SecretAccessKey"],
            token=sts_credentials["SessionToken"],
            service="execute-api",
            region=REGIONS[self.region],
        )

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return replace(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return replace(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return replace(self, timeout=timeout)

    def get_auth(self) -> SigV4Auth:
        return self.auth
