import toml


def extract_dependencies(pyproject_file, include_devs=False):
    with open("pyproject.toml") as f:
        pyproject_dict = toml.load(f)

    dependencies = pyproject_dict["tool"]["poetry"]["dependencies"]
    dependencies.pop("python")

    lines = []
    for dep, version in dependencies.items():
        version = version.replace("^", "")
        lines.append("==".join((dep, version)))
    print("\n".join(lines))


if __name__ == "__main__":
    extract_dependencies("a")
