import pytest
import Plotter


@pytest.fixture
def app(qtbot):
    test_app = Plotter.MainWindow()
    qtbot.addWidget(test_app)
    return test_app
    
@pytest.fixture(scope='function', autouse=True)
def first_app(app, request):
    request.instance.app = app

class Test_General:
    # Test function input
    def test_QLineEdit(self, request):
        assert request.instance.app.function_input.text() == ""


    # Test button text
    def test_submit_text(self, request):
        assert request.instance.app.button_to_conv.text() == "Plot"
    
    
    # Test range prefixes
    def test_range_prefixes(self, request):
        assert request.instance.app.min_input.prefix() == "Min value: "
        assert request.instance.app.max_input.prefix() == "Max value: "
    
    
    # Test range values
    def test_range_values(self, request):
        assert request.instance.app.min_input.minimum() == -3000.0
        assert request.instance.app.max_input.minimum() == -3000.0
        assert request.instance.app.min_input.maximum() == 3000.0
        assert request.instance.app.max_input.maximum() == 3000.0
        
        
    # Test range changes
    def test_range_changes(self, request):
        request.instance.app.min_input.stepBy(15)
        assert request.instance.app.min_input.value() == 4
        request.instance.app.max_input.stepBy(-15)
        assert request.instance.app.max_input.value() == 5

