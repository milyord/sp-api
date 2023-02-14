import { promises as fs } from "fs";
import converter from "swagger2openapi";
import glob from "glob";
import path from "path";

const options = {
  patch: true,
};

async function convert() {
  try {
    const swaggerFilePaths = glob.sync(
      "../selling-partner-api-models/models/**/**.json"
    );

    swaggerFilePaths.forEach(async (filePath) => {
      const converted = await converter.convertFile(filePath, options);
      await fs.writeFile(
        `models/${path.basename(filePath)}`,
        JSON.stringify(converted.openapi)
      );
    });
  } catch (err) {
    console.log(err);
  }
}

convert();
