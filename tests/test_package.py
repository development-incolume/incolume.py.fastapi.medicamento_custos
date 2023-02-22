import re

import pytest
from incolume.py.medicamento_custos import configfile, versionfile, __version__


__author__ = '@britodfbr'  # pragma: no cover


class TestCase:
    def test_configfile(self):
        assert configfile.is_file(), f"{configfile=}"

    def test_versionfile(self):
        assert versionfile.is_file(), f"{versionfile=}"

    @pytest.mark.parametrize(
        ["entrance", "expected"],
        (
            (__version__, True),
            ("1", False),
            ("1.0", False),
            ("0.1", False),
            ("1.1.1-rc0", False),
            ("1.1.1-rc-0", False),
            ("1.0.1-dev0", False),
            ('1.1.1-a0', False),
            ('1.1.1-a.0', True),
            ("0.0.1", True),
            ("0.1.0", True),
            ("1.0.0", True),
            ("1.0.1", True),
            ("1.1.1", True),
            ("1.1.1-rc.0", True),
            ("1.0.1-dev.0", True),
            ("1.0.1-dev.1", True),
            ("1.0.1-dev.2", True),
            ("1.0.1-alpha.0", True),
            ("1.0.1-alpha.266", True),
            ("1.0.1-dev.0", True),
            ("1.0.1-beta.0", True),
            ("1.1.1-alpha.99999", True),
            ("11111.1.1-rc.99999", True),
            ("1.1.99999", True),
            ("1.999999.1", True),
        ),
    )
    def test_semantic_version(self, entrance, expected):
        assert bool(
            re.fullmatch(r"\d+\.\d+\.\d+(-\w+\.\d+)?", entrance, flags=re.I)
        ) == expected
