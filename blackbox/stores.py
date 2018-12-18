"""
File system functions api for Blackbox on Python.

@author
"""

from io import BytesIO
import subprocess
import sys



class KeyStore():

    def __init__(self, key_store_dir):
        self.__key_store_dir = key_store_dir

    def ls(self):
        """
        List all files in the keystore

        :return:  a list of files
        :rtype:  list
        """
        proc = subprocess.Popen('blackbox_list_files', cwd=self.__key_store_dir, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False)
        proc.wait()
        out = []
        err = None
        for line in proc.stdout:
            out.append(line.strip())
        for line in proc.stderr:
            if err:
                err = "{}\n{}".format(out, line)
            else:
                err = line
        return {
            'files': out
        }


    def diff(self):
        """
        Run the encrypted v. decrypted diff on blackbox

        :return: The diff result dict
        :rtype:  dict
        """
        proc = subprocess.Popen('blackbox_diff', cwd=self.__key_store_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        proc.wait()
        out = None
        err = None
        for line in proc.stdout:
            if out:
                out = "{}\n{}".format(out, line)
            else:
                out = line
        for line in proc.stderr:
            if err:
                err = "{}\n{}".format(out, line)
            else:
                err = line
        return {'stdout': out, 'stderr': err, 'code': proc.returncode}

    def shred(self):
        """
        Shred and delete decrypted files.

        :return:  Completion status dict
        :rtype;  dict
        """
        proc = subprocess.Popen('blackbox_shred_all_files', cwd=self.__key_store_dir, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False)
        proc.wait()
        out = None
        err = None
        for line in proc.stdout:
            if out:
                out = "{}\n{}".format(out, line)
            else:
                out = line
        for line in proc.stderr:
            if err:
                err = "{}\n{}".format(out, line)
            else:
                err = line
        return {'stdout': out, 'stderr': err, 'code': proc.returncode}

    def start_edit(self, fname):
        """
        Start editing a file

        :param fname:  The file name in the directory
        :type fname:  str
        :return: success status
        :rtype:  bool
        """
        proc = subprocess.Popen(['blackbox_edit_start', fname], cwd=self.__key_store_dir, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False)
        proc.wait()
        out = None
        err = None
        for line in proc.stdout:
            if out:
                out = "{}\n{}".format(out, line)
            else:
                out = line
        for line in proc.stderr:
            if err:
                err = "{}\n{}".format(out, line)
            else:
                err = line
        return {'stdout': out, 'stderr': err, 'code': proc.returncode}

    def end_edit(self, fname):
        """
        Re-encrypt edited file

        :param fname:  The file name
        :type fname:  str
        :return:  success status
        :rtype:  bool
        """
        proc = subprocess.Popen(['blackbox_edit_end', fname], cwd=self.__key_store_dir, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False)
        proc.wait()
        out = None
        err = None
        for line in proc.stdout:
            if out:
                out = "{}\n{}".format(out, line)
            else:
                out = line
        for line in proc.stderr:
            if err:
                err = "{}\n{}".format(out, line)
            else:
                err = line
        return {'stdout': out, 'stderr': err, 'code': proc.returncode}

    def remove_file(self, fname):
        """
        Remove a file from the system

        :param fname:  The name of the file
        :type fname:  str
        :return:  Success dict
        :rtype:  dict
        """
        proc = subprocess.Popen(['blackbox_deregister_file', fname], cwd=self.__key_store_dir, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False)
        proc.wait()
        out = None
        err = None
        for line in proc.stdout:
            if out:
                out = "{}\n{}".format(out, line)
            else:
                out = line
        for line in proc.stderr:
            if err:
                err = "{}\n{}".format(out, line)
            else:
                err = line
        return {'stdout': out, 'stderr': err, 'code': proc.returncode}


    def add_file(self, fname):
        """
        Save a file to blackbox

        :param fname:  The file name
        :type fname:  str
        :return:  Completion status dict
        :rtype:  dict
        """
        proc = subprocess.Popen(['blackbox_register_new_file', fname], cwd=self.__key_store_dir, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False)
        proc.wait()
        out = None
        err = None
        for line in proc.stdout:
            if out:
                out = "{}\n{}".format(out, line)
            else:
                out = line
        for line in proc.stderr:
            if err:
                err = "{}\n{}".format(out, line)
            else:
                err = line
        return {'stdout': out, 'stderr': err, 'code': proc.returncode}


    def cat_file(self, fname, add_new_line=False):
        """
        Save a file to blackbox

        :param fname:  The file name
        :type fname:  str
        :return:  Completion status dict
        :rtype:  dict
        """
        proc = subprocess.Popen(['blackbox_cat', fname], cwd=self.__key_store_dir, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False)
        proc.wait()
        out = None
        err = None
        for line in proc.stdout:
            if out:
                if type(line) is str:
                    uline = line
                else:
                    uline = line.decode()
                if add_new_line:
                    out = "{}\n{}".format(out, uline)
                else:
                    out = "{}{}".format(out, uline)
            else:
                if type(line) is str:
                    out = line
                else:
                    out = line.decode()
        for line in proc.stderr:
            if err:
                err = "{}\n{}".format(out, line)
            else:
                err = line
        return {'stdout': out, 'stderr': err, 'code': proc.returncode}
