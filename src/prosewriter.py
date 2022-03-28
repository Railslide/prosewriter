import toml


def convert_syntax(dependency_name, poetry_version):
    requirement_version = poetry_version.replace("^", "")
    return "==".join((dependency_name, requirement_version))


def extract_dependencies(pyproject_dict, include_devs=False):
    dependencies = pyproject_dict["tool"]["poetry"]["dependencies"]
    dependencies.pop("python")

    lines = []
    for dep, version in dependencies.items():
        version = version.replace()

    print("\n".join(lines))


def main():
    with open("pyproject.toml") as f:
        pyproject_dict = toml.load(f)
    extract_dependencies(pyproject_dict)


if __name__ == "__main__":
    # TODO: get path as an argument
    main()
