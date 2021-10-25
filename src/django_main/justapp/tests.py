from django.test import TestCase
from .models import unique_rand, is_not_reach_max_students, School
from django.core.exceptions import ValidationError

from mock import patch, Mock


class ModelHelpers_TestCase(TestCase):


    @patch('justapp.models.Student') # injecting student mock -> mocked_student
    def test_unique_rand(self, mocked_student):
    	"""unique_rand helper can run correctly"""
    	# mocking queryset
    	mocked_queryset = Mock()
    	mocked_queryset.exists.return_value = False
    	# injecting mocked_queryset into mocked_student
    	mocked_student.objects.filter.return_value = mocked_queryset
    	# 1) validate output is 20 chars
    	self.assertEqual(len(unique_rand()),20)
    	# 2) validate student filter has been called
    	mocked_student.objects.filter.assert_called_once() 

    
    
    @patch('justapp.models.Student') # injecting student mock -> mocked_student
    def test_is_not_reach_max_students(self, mocked_student):
        """is_not_reach_max_students helpers shall raise error if reaching max students"""
        # mocked school object
        mocked_school = Mock(spec=School)
        mocked_school.max_students = 2
        # mocking queryset
        mocked_queryset = Mock()
        mocked_queryset.count.return_value = 2
        # injecting mocked_queryset into mocked_student
        mocked_student.objects.filter.return_value = mocked_queryset
        self.assertRaises(ValidationError,is_not_reach_max_students, mocked_school)
        mocked_student.objects.filter.assert_called_once() 


