import unittest
from unittest.mock import MagicMock, patch

import pytest

from commands.check_duplication import has_duplication
from models.job import Job
from models.link import Link


@patch("commands.check_duplication.Job")
@patch("commands.check_duplication.Link")
def test_has_duplication_retrun_false_for_new_entry(MockJob, MockLink):
    MockJob.find_by_external_id.return_value = None
    MockLink.find_by_external_id.return_value = None
    external_id = "xx"
    result = has_duplication("xxxx")
    assert result == False


@patch("commands.check_duplication.Job")
@patch("commands.check_duplication.Link")
@pytest.mark.parametrize(
    "test_job_model, test_link_model", [(Job(), None), (None, Link()), (Job(), Link())]
)
def test_has_duplication_retrun_true_for_existing_entry(
    MockJob,
    MockLink,
    test_job_model,
    test_link_model,
):
    MockJob.find_by_external_id.return_value = test_job_model
    MockLink.find_by_external_id.return_value = test_link_model

    # MockLink.find_by_external_id.return_value = Link()
    external_id = "xx"
    result = has_duplication("xxxx")
    assert result == True
