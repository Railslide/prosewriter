from prosewriter.prosewriter import convert_syntax, extract_dependencies


def test_convert_syntax():
    result = convert_syntax("test_package", "1.2.3")
    assert result == "test_package==1.2.3"


def test_convert_syntax_caret():
    result = convert_syntax("test_package", "^1.2.3")
    assert result == "test_package==1.2.3"


def test_extract_dependencies_prod_only():
    toml_dict = {
        "tool": {
            "poetry": {
                "name": "test",
                "version": "1",
                "description": "test description",
                "authors": [],
                "license": "test_license",
                "dependencies": {"python": "^3.10", "toml": "^0.10.2"},
                "dev-dependencies": {"pytest": "^7.1.1"},
            }
        },
        "build-system": {},
    }
    result = extract_dependencies(toml_dict)
    assert result == {"toml": "^0.10.2"}


def test_extract_dependencies_all():
    toml_dict = {
        "tool": {
            "poetry": {
                "name": "test",
                "version": "1",
                "description": "test description",
                "authors": [],
                "license": "test_license",
                "dependencies": {"python": "^3.10", "toml": "^0.10.2"},
                "dev-dependencies": {"pytest": "^7.1.1"},
            }
        },
        "build-system": {},
    }
    result = extract_dependencies(toml_dict, include_devs=True)
    assert result == {"toml": "^0.10.2", "pytest": "^7.1.1"}


def test_extract_dependencies_dev_only():
    toml_dict = {
        "tool": {
            "poetry": {
                "name": "test",
                "version": "1",
                "description": "test description",
                "authors": [],
                "license": "test_license",
                "dependencies": {"python": "^3.10", "toml": "^0.10.2"},
                "dev-dependencies": {"pytest": "^7.1.1"},
            }
        },
        "build-system": {},
    }
    result = extract_dependencies(toml_dict, include_devs=True, dev_only=True)
    assert result == {"pytest": "^7.1.1"}
