import toml


def convert_syntax(dependency_name, poetry_version):
    requirement_version = poetry_version.replace("^", "")
    return "==".join((dependency_name, requirement_version))


def extract_dependencies(pyproject_dict, include_devs=False, dev_only=False):
    dependencies = {}
    if not dev_only:
        prod_dependencies = pyproject_dict["tool"]["poetry"]["dependencies"]
        prod_dependencies.pop("python")
        dependencies.update(prod_dependencies)

    if include_devs or dev_only:
        dev_dependencies = pyproject_dict["tool"]["poetry"].get("dev-dependencies")
        dependencies.update(dev_dependencies)
    return dependencies


def main():
    with open("../pyproject.toml") as f:
        pyproject_dict = toml.load(f)
    dependencies = extract_dependencies(pyproject_dict, include_devs=True)
    requirements = []
    for dep, version in dependencies.items():
        requirements.append(convert_syntax(dep, version))
    print("\n".join(requirements))


if __name__ == "__main__":
    # TODO: get path as an argument
    main()
