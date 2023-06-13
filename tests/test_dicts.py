import pytest

from utils.dicts import get_val


@pytest.fixture
def coll():
    return {"vcs": "mercurial"}


def test_dict(coll):
    assert get_val(coll, "vcs") == "mercurial"
    assert get_val({}, "vcs") == "git"
    assert get_val({}, "vcs", "bazaar") == "bazaar"
