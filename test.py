def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


def test_forms(cldf_dataset):
    assert len(list(cldf_dataset["FormTable"])) == 1585
    assert any(f["Form"] == "plaːŋ" for f in cldf_dataset["FormTable"])


def test_parameters(cldf_dataset):
    assert len(list(cldf_dataset["ParameterTable"])) == 100


def test_languages(cldf_dataset):
    assert len(list(cldf_dataset["LanguageTable"])) == 16


def test_cognates(cldf_dataset):
    assert len(list(cldf_dataset["CognateTable"])) == 1585
    assert any(f["Form"] == "lənlaːw" for f in cldf_dataset["CognateTable"])
