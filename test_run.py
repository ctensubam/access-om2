
from __future__ import print_function

from model_test_setup import ModelTestSetup
import subprocess as sp
import shutil
import os

class TestRun(ModelTestSetup):

    def __init__(self):
        super(TestRun, self).__init__()

    def get_paths(self, exp_name):
        paths = {} 
        paths['exp'] = os.path.join('payu-experiments/access', exp_name)
        paths['archive'] = os.path.join(self.lab_path, 'archive', exp_name)
        paths['archive_link'] = os.path.join(paths['exp'], 'archive')
        paths['output'] = os.path.join(paths['archive'], 'output000')
        paths['restart'] = os.path.join(paths['archive'], 'restart000')
        paths['stdout'] = os.path.join(paths['output'], 'access.out')
        paths['stderr'] = os.path.join(paths['output'], 'access.err')

        return paths

    def pre_run_checks(self, paths):

        # No model output should exist.
        assert(not os.path.exists(paths['archive']))


    def post_run_checks(self, paths):

        # Model output should exist.
        assert(os.path.exists(paths['output']))
        assert(os.path.exists(paths['restart']))
        assert(os.path.exists(paths['stdout']))
        assert(os.path.exists(paths['stderr']))

        # Check that model completed successfully.
        with open(paths['stdout'], 'r') as f:
            s = f.read()
            assert('MOM4: --- completed ---' in s)
            assert('********** End of MATM **********' in s)


    def post_run_cleanup(self, paths, qsub_files):

        # Do some clean-up
        shutil.rmtree(paths['archive'])
        os.remove(paths['archive_link'])
        for f in qsub_files:
            os.remove(f)


    def do_basic_run(self, exp):

        paths = self.get_paths(exp)
        
        self.pre_run_checks(paths)

        qsub_out, qsub_err, qsub_files = self.run(paths['exp'], self.lab_path)

        self.post_run_checks(paths)
        self.post_run_cleanup(paths, qsub_files)


    def test_ACCESS_OM_tiny(self):
        """
        Run the ACCESS-OM_tiny experiment.
        """

        self.do_basic_run('access-om_tiny')


    def test_ACCESS_CM_tiny(self):
        """
        Run the ACCESS-CM_tiny experiment.
        """

        #self.do_basic_run('access-cm_tiny')
        pass


    def test_ACCESS_OM(self):
        """
        Run the ACCESS-OM experiment.
        """

        #self.do_basic_run('access-om')
        pass


    def test_ACCESS_CM(self):
        """
        Run the ACCESS-CM experiment.
        """

        #self.do_basic_run('access-cm')
        pass


    def test_ACCESS_OM_1440x1080(self):
        """
        Run the ACCESS-OM_1440x1080 experiment.
        """

        #self.do_basic_run('access-om_1440x1080')
        pass

    def test_ACCESS_CM_1440x1080(self):
        """
        Run the ACCESS-CM_1440x1080 experiment.
        """

        #self.do_basic_run('access-cm_1440x1080')
        pass
