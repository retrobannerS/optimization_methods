import os
import shutil
import tomllib
from parser import write_yaml, write_template

# Change the current working directory to the root of the project
os.chdir(os.path.join(os.path.dirname(__file__), ".."))

# Recursively remove out directory and then create it again
shutil.rmtree("out", ignore_errors=True)
os.makedirs("out", exist_ok=True)

# Recursively remove temporary directory and then create it again
shutil.rmtree("tmp", ignore_errors=True)
os.makedirs("tmp", exist_ok=True)

with open("build-conf.toml", "rb") as file:
    conf = tomllib.load(file)

write_yaml(conf, "tmp/metadata.yaml")

# Create void file and link out template
with open("tmp/void.tex", "w") as file:
    pass
os.system(
    f"pandoc tmp/void.tex -o tmp/raw_template.tex {' '.join(conf['pandoc']['args'])}"
)

# Parse our template
preambles = [os.path.join("preambles", file) for file in conf["pandoc"]["preambles"]]
write_template(preambles)

# Move to separated folder
shutil.rmtree("src/template", ignore_errors=True)
os.makedirs("src/template", exist_ok=True)
shutil.move("tmp/template.tex", "src/template/template.tex")
shutil.move("tmp/titlepage.tex", "src/template/titlepage.tex")
shutil.move("tmp/toc.tex", "src/template/toc.tex")

# Remove temporary directory
shutil.rmtree("tmp", ignore_errors=True)
