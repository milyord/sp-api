from os import path
from pathlib import Path

from openapi_python_client import MetaType, cli, create_new_client, update_existing_client, utils


def start():
    model_paths = Path("converter/models").glob("*.json")
    config = cli._process_config(path=None)
    Path("sp").mkdir(exist_ok=True)

    for model in model_paths:
        package_name = utils.snake_case(path.basename(model).split(".")[0])
        config.package_name_override = f"sp/{package_name}"
        if Path(config.package_name_override).is_dir():
            update_existing_client(
                url=None,
                path=Path(model),
                config=config,
                meta=MetaType.NONE,
                custom_template_path=Path("templates"),
            )
        else:
            create_new_client(
                url=None,
                path=Path(model),
                config=config,
                meta=MetaType.NONE,
                custom_template_path=Path("templates"),
            )
