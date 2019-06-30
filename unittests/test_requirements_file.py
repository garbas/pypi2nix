import pytest

from pypi2nix.requirements_file import RequirementsFile


@pytest.fixture
def project_dir(tmpdir):
    return str(tmpdir)


@pytest.fixture
def requirements_file_from_lines(project_dir, tmpdir_factory):
    def factory(lines):
        requirements_file = tmpdir_factory.mktemp("test").join("requirements.txt")
        requirements_file.write("\n".join(lines))
        return RequirementsFile(str(requirements_file), project_dir)

    return factory


def test_requirements_file_detects_git_source(requirements_file_from_lines):
    requirements_file = requirements_file_from_lines(["git+git://test.com#egg=testegg"])
    requirements_file.process()
    assert "testegg" in requirements_file.sources


def test_requirements_file_handles_comments(requirements_file_from_lines):
    requirements_file = requirements_file_from_lines(["# comment"])
    requirements_file.process()


def test_requirements_file_handles_empty_lines(requirements_file_from_lines):
    requirements_file = requirements_file_from_lines([""])
    requirements_file.process()


def test_requirements_file_can_be_created_from_requirements_lines(project_dir):
    RequirementsFile.from_lines(["pytest"], project_dir=project_dir)


def test_requirements_file_from_lines_throws_when_given_a_string(project_dir):
    with pytest.raises(Exception):
        RequirementsFile.from_lines("pytest", project_dir=project_dir)