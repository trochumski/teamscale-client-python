"""All tests mocked using the responses api:

https://github.com/getsentry/responses
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import datetime
import re
import responses

from teamscale_client import TeamscaleClient
from teamscale_client.constants import CoverageFormats
from teamscale_client.data import Finding, FileFindings
from teamscale_client.utils import to_json


URL = "http://localhost:8080"

def get_client():
    return TeamscaleClient(URL, "admin", "admin", "foo")

def get_project_service_mock(service_id):
    return re.compile(r'%s/p/foo/%s/.*' % (URL, service_id))

def get_global_service_mock(service_id):
    return re.compile(r'%s/%s/.*' % (URL, service_id))

@responses.activate
def test_put():
    responses.add(responses.PUT, 'http://localhost:8080',
                      body='success', status=200)
    resp = get_client().put("http://localhost:8080", "[]", {})
    assert resp.text == "success"

@responses.activate
def test_upload_findings():
    responses.add(responses.PUT, get_project_service_mock('add-external-findings'),
                      body='success', status=200)
    resp = get_client().upload_findings([], datetime.datetime.now(), "Test message", "partition-name")
    assert resp.text == "success"

@responses.activate
def test_upload_metrics():
    responses.add(responses.PUT, get_project_service_mock('add-external-metrics'),
                      body='success', status=200)
    resp = get_client().upload_metrics([], datetime.datetime.now(), "Test message", "partition-name")
    assert resp.text == "success"

@responses.activate
def test_upload_metric_description():
    responses.add(responses.PUT, get_global_service_mock('add-external-metric-description'),
                      body='success', status=200)
    resp = get_client().upload_metric_definitions([])
    assert resp.text == "success"

@responses.activate
def test_coverage_upload():
    files = ["tests/data/file1.txt", "tests/data/file2.txt"]
    responses.add(responses.POST, get_project_service_mock('external-report'),
                      body='success', status=200)
    resp = get_client().upload_coverage_data(files, CoverageFormats.CTC, datetime.datetime.now(), "Test Message", "partition-name")
    assert resp.text == "success"
    assert "file1.txt" in responses.calls[0].request.body.decode() != -1
    assert "file2.txt" in responses.calls[0].request.body.decode() != -1

def test_finding_json_serialization():
    finding = Finding("test-id", "message")
    findings = FileFindings([finding], "path/to/file")
    assert '{"content": null, "findings": [{"assessment": "YELLOW", "endLine": 0, "endOffset": 0, "findingTypeId": "test-id", "identifier": null, "message": "message", "startLine": 0, "startOffset": 0}], "path": "path/to/file"}' == to_json(findings)
