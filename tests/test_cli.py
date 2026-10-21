from utils.legal import validate_authorization


def test_validate_authorization_accepts_authorized_target(tmp_path):
    auth_file = tmp_path / "authorization.txt"
    auth_file.write_text("authorization: granted\n", encoding="utf-8")

    target = {
        "identifier": "AA:BB:CC:DD:EE:FF",
        "owner": "Responsible operator",
        "authorized": True,
        "authorization_file": str(auth_file),
    }

    assert validate_authorization(target) is True


def test_validate_authorization_rejects_missing_authorization_file():
    target = {
        "identifier": "AA:BB:CC:DD:EE:FF",
        "owner": "Responsible operator",
        "authorized": True,
        "authorization_file": "./missing-auth.txt",
    }

    assert validate_authorization(target) is False


def test_validate_authorization_rejects_unauthorized_target():
    target = {
        "identifier": "AA:BB:CC:DD:EE:FF",
        "owner": "Responsible operator",
        "authorized": False,
    }

    assert validate_authorization(target) is False
