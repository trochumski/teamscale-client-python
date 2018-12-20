"""All tests mocked using the responses api:

https://github.com/getsentry/responses
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import datetime
import re
import responses

from teamscale_client import TeamscaleClient
from teamscale_client.constants import CoverageFormats, AssessmentMetricColors, Enablement, TaskStatus
from teamscale_client.data import Finding, FileFindings, MetricDescription, MetricEntry, NonCodeMetricEntry, Baseline, \
    FileSystemSourceCodeConnectorConfiguration, ProjectConfiguration, FindingDescription
from teamscale_client.utils import to_json


URL = "http://localhost:8080"
SUCCESS = 'success'

def get_client():
    """Returns Teamscale client object for requesting servers"""
    responses.add(responses.GET, get_global_service_mock('service-api-info'), status=200,
                  content_type="application/json", body='{ "apiVersion": 6}')
    return TeamscaleClient(URL, "admin", "admin", "foo")

def get_project_service_mock(service_id):
    """Returns mock project service url"""
    return re.compile(r'%s/p/foo/%s/.*' % (URL, service_id))

def get_global_service_mock(service_id):
    """Returns mock global service url"""
    return re.compile(r'%s/%s/.*' % (URL, service_id))

@responses.activate
def test_put():
    """Tests PUT requests to server"""
    responses.add(responses.PUT, 'http://localhost:8080',
                      body=SUCCESS, status=200)
    resp = get_client().put("http://localhost:8080", "[]", {})
    assert resp.text == SUCCESS

@responses.activate
def test_add_findings_group():
    """ Tests uploading of findings groups into Teamscale server.
    """
    responses.add(responses.PUT, get_global_service_mock('external-findings-group'), body=SUCCESS, status=200)
    resp = get_client().add_findings_group('name', 'map.*')
    assert resp.text == SUCCESS

@responses.activate
def test_add_findings_descriptions():
    """ Tests uploading of findings descriptions into Teamscale server
    """
    findings_descriptions = [FindingDescription('type1', 'desc1', Enablement.RED, 'name1'),
                             FindingDescription('type2', 'desc2', Enablement.YELLOW, 'name 2')]
    responses.add(responses.PUT, get_global_service_mock('external-findings-description'), body=SUCCESS, status=200)
    resp = get_client().add_finding_descriptions(findings_descriptions)
    assert resp.text == SUCCESS

@responses.activate
def test_upload_findings():
    """Tests uploading of findings"""
    responses.add(responses.PUT, get_project_service_mock('add-external-findings'),
                      body=SUCCESS, status=200)
    resp = get_client().upload_findings(_get_test_findings(), datetime.datetime.now(), "Test message", "partition-name")
    assert "content" in responses.calls[1].request.body
    assert "test-id" in responses.calls[1].request.body
    assert resp.text == SUCCESS

@responses.activate
def test_upload_metrics():
    """Tests uploading of metrics"""
    metric = MetricEntry("test/path", {"metric-1": 1, "metric-2" : [1, 3, 4]})
    responses.add(responses.PUT, get_project_service_mock('add-external-metrics'),
                      body=SUCCESS, status=200)
    resp = get_client().upload_metrics([metric], datetime.datetime.now(), "Test message", "partition-name")
    assert '[{"metrics": {"metric-1": 1, "metric-2": [1, 3, 4]}, "path": "test/path"}]' == responses.calls[1].request.body
    assert resp.text == SUCCESS

@responses.activate
def test_upload_non_code_metrics():
    """Tests uploading of non code metrics"""
    metric = NonCodeMetricEntry("metric1/non/code/metric/path", "This is a test content", 2, {AssessmentMetricColors.RED: 2, AssessmentMetricColors.GREEN : 1}, 25.0)
    responses.add(responses.PUT, get_project_service_mock("add-non-code-metrics"),
                      body=SUCCESS, status=200)
    resp = get_client().upload_non_code_metrics([metric], datetime.datetime.now(), "Test message", "partition-name")
    assert '[{"assessment": {"GREEN": 1, "RED": 2}, "content": "This is a test content", "count": 2, "path": "metric1/non/code/metric/path", "time": 25.0}]' == responses.calls[1].request.body
    assert resp.text == SUCCESS

@responses.activate
def test_upload_metric_description():
    """Tests uploading of metric descriptions"""
    description = MetricDescription("metric_i,", "Metric Name", "Great Description", "awesome group")
    responses.add(responses.PUT, get_global_service_mock('external-metric'),
                      body=SUCCESS, status=200)
    resp = get_client().add_metric_descriptions([description])
    assert '{"analysisGroup": "awesome group", "metricDefinition": {"aggregation": "SUM", "description": "Great Description", "name": "Metric Name", "properties": ["SIZE_METRIC"], "valueType": "NUMERIC"}, "metricId": "metric_i,"}' == to_json(description)
    assert resp.text == SUCCESS

@responses.activate
def test_coverage_upload():
    """Tests uploading of test coverage"""
    files = ["tests/data/file1.txt", "tests/data/file2.txt"]
    responses.add(responses.POST, get_project_service_mock('external-report'),
                      body=SUCCESS, status=200)
    resp = get_client().upload_coverage_data(files, CoverageFormats.CTC, datetime.datetime.now(), "Test Message", "partition-name")
    assert resp.text == SUCCESS
    assert "file1.txt" in responses.calls[1].request.body.decode()
    assert "file2.txt" in responses.calls[1].request.body.decode()

@responses.activate
def test_get_baseline():
    """Tests retrieving of baselines"""
    responses.add(responses.GET, get_project_service_mock('baselines'),
                      status=200, content_type="application/json", body='[{ "name": "Baseline 1", "description": "Test description", "timestamp": 123192873091 }]')
    resp = get_client().get_baselines()
    assert len(resp) == 1
    assert resp[0].name == "Baseline 1"

@responses.activate
def test_add_baseline():
    """Test uploading of baselines"""
    baseline = Baseline("Baseline 1", "Test description", datetime.datetime.now())
    responses.add(responses.PUT, get_project_service_mock('baselines'),
                      body=SUCCESS, status=200)
    resp = get_client().add_baseline(baseline)
    assert resp.text == SUCCESS
    assert "Baseline 1" in responses.calls[1].request.body

@responses.activate
def test_delete_baseline():
    """Test deletion of baselines"""
    responses.add(responses.DELETE, get_project_service_mock('baselines'),
                      body=SUCCESS, status=200)
    resp = get_client().delete_baseline("Baseline 1")
    assert resp.text == SUCCESS

@responses.activate
def test_architecture_upload():
    """Tests uploading of architectures"""
    # Just reuse text files for testing, it's just a mock anyway
    paths = {"archs/first.architecture" : "tests/data/file1.txt", "archs/second.architecture" : "tests/data/file2.txt"}
    responses.add(responses.POST, get_project_service_mock('architecture-upload'),
                      body=SUCCESS, status=200)
    resp = get_client().upload_architectures(paths, datetime.datetime.now(), "Test Message")
    assert resp.text == SUCCESS
    assert "file1.txt" in responses.calls[1].request.body.decode()
    assert "file2.txt" in responses.calls[1].request.body.decode()

def _get_test_findings():
    """Returns test findings"""
    finding = Finding("test-id", "message")
    return [FileFindings([finding], "path/to/file")]

def test_finding_json_serialization():
    """Tests that findings json is correctly serialized"""
    findings = _get_test_findings()
    assert '[{"content": null, "findings": [{"assessment": "YELLOW", "endLine": null, "endOffset": null, "findingProperties": null, "findingTypeId": "test-id", "identifier": null, "message": "message", "startLine": null, "startOffset": null, "uniformPath": null}], "path": "path/to/file"}]' == to_json(findings)

@responses.activate
def test_get_projects():
    """Tests retrieving of projects"""
    responses.add(responses.GET, get_global_service_mock('projects'),
                      status=200, content_type="application/json", body='[{"description": "", "creationTimestamp": 1487534523817, "alias": "My Test Project", "reanalyzing": false, "deleting": false, "id": "test-project", "name": "Test Project"}]')
    resp = get_client().get_projects()
    assert len(resp) == 1
    assert resp[0].name == "Test Project"

@responses.activate
def test_add_project():
    """Test adding projects"""
    file_system_config = FileSystemSourceCodeConnectorConfiguration(input_directory="/path/to/folder",
                                                                    repository_identifier="Local",
                                                                    included_file_names="**.py")
    project_configuration = ProjectConfiguration(name="Test Project", project_id="test-project",
                                                 profile="Python (default)", connectors=[file_system_config])

    responses.add(responses.PUT, get_global_service_mock('create-project'),
                      body='{"message": "success"}', status=200)
    resp = get_client().create_project(project_configuration)
    assert resp.status_code == 200 and TeamscaleClient._get_response_message(resp) == SUCCESS

def test_compare_findings():
    """Tests comparing between findings."""
    first_finding = Finding("1a", "first message a", uniform_path='path/to/a', start_line=10, end_line=30)
    second_finding = Finding("2", "second message", uniform_path='path/to/a', start_line=20, end_line=25)
    third_finding = Finding("3", "third message", uniform_path='path/to/b', start_line=20, end_line=25)

    assert first_finding < second_finding
    assert second_finding < third_finding
    assert first_finding == first_finding
    assert third_finding > second_finding
    assert second_finding >= first_finding
    assert second_finding >= first_finding
    assert second_finding != first_finding

@responses.activate
def test_get_tasks():
    """Tests retrieving of projects"""
    responses.add(responses.GET, get_project_service_mock('tasks'),
                  status=200, content_type="application/json",
                  body='[{"id": 1, "subject": "uiae", "author": "admin", "description": "", "assignee": "", "created": 1536581194732, "updated": 1536583991791, "updatedBy": "admin", "status": "OPEN", "resolution": "NONE", "findings": [{"findingId": "40315BE118FE08044FBF605325445250"}], "comments": [{"author": "admin", "date": 1536583991791, "text": "Added finding: 40315BE118FE08044FBF605325445250", "changeComment": true, "resolvedAuthor": {"username": "admin", "firstName": "Default", "lastName": "Administrator", "emailAddress": "", "gravatarHash": "dummy", "useGravatar": false, "aliases": [], "authenticator": "HashedStored:anonymized", "groupIds": ["Administrators"]}}], "tags": [], "resolvedAuthor": {"username": "admin", "firstName": "Default", "lastName": "Administrator", "emailAddress": "", "gravatarHash": "dummy", "useGravatar": false, "aliases": [], "authenticator": "HashedStored:anonymized", "groupIds": ["Administrators"]}, "resolvedUpdatedBy": {"username": "admin", "firstName": "Default", "lastName": "Administrator", "emailAddress": "", "gravatarHash": "dummy", "useGravatar": false, "aliases": [], "authenticator": "HashedStored:anonymized", "groupIds": ["Administrators"]}}]')
    resp = get_client().get_tasks(TaskStatus.OPEN)
    assert len(resp) == 1
    assert resp[0].id == 1
    assert resp[0].author == 'admin'

@responses.activate
def test_add_issue_metric():
    """Tests the addition of a issue metric"""
    responses.add(responses.PUT, get_project_service_mock('issue-metrics'),
                      body='{"message": "success"}', status=200)
    get_client().add_issue_metric("example/foo", "instate(status=YELLOW) > 2d")
    assert "YELLOW" in responses.calls[1].request.body.decode()

@responses.activate
def test_get_all_dashboard_details():
    """Tests query of all dashboard details"""
    responses.add(responses.GET, get_global_service_mock('dashboards'),
                      body='[{"name":"new dashboard","owner":"gib","descriptorJSON":"{\\"widgets\\":[{\\"widget-id\\":\\"commit-chart\\",\\"position\\":{\\"x\\":0,\\"y\\":0,\\"width\\":12,\\"height\\":6},\\"Title\\":\\"Commit Chart\\",\\"Path\\":{\\"project\\":\\"myProject\\",\\"path\\":\\"\\",\\"hiddenInWidgetTitle\\":false},\\"Trend\\":{\\"type\\":\\"timespan\\",\\"value\\":0},\\"Zooming\\":true,\\"Hide Y-Axes\\":false,\\"Baselines\\":true,\\"Action menu\\":false,\\"Min. commits per developer\\":0,\\"Order\\":\\"by time\\"}]}","author":"gib","comment":"","canRead":false,"canWrite":false}]', status=200)
    dashboards = get_client().get_all_dashboard_details()
    assert dashboards[0]['name'] == 'new dashboard'

@responses.activate
def test_delete_dashboard():
    """Test deletion of dashboards"""
    responses.add(responses.DELETE, get_global_service_mock('dashboards'),
                      body=SUCCESS, status=200)
    resp = get_client().delete_dashboard("some dashboard name")
    assert resp.text == SUCCESS
