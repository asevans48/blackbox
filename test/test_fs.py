"""
Test functions for the file system

@author aevans
"""

import os

import pytest

from blackbox.stores import KeyStore


HOME = os.path.sep.join(os.path.dirname(os.path.realpath(__file__)).split(os.path.sep)[:-1])


@pytest.fixture
def test_keystore():
    return KeyStore(HOME)


def test_diff(test_keystore):
    """
    Test the diff function
    """
    r = test_keystore.diff()
    assert(r['stderr'] is None)
    assert(r['stdout'] is not None)


def test_ls(test_keystore):
    """
    Test the ls function
    """
    files = test_keystore.ls()
    assert(type(files) is list)


def test_shred(test_keystore):
    """
    Test the shred function
    """
    rdict = test_keystore.shred()
    print(rdict)
    assert(type(rdict) is dict)
    assert(rdict['stderr'] is None)

def test_add_file(test_keystore):
    """
    Test the copy file function
    """
    new_fpath = os.path.sep.join([HOME, 'test2.txt'])
    if os.path.exists(new_fpath+'.gpg'):
        os.remove(new_fpath+'.gpg')
    with open(new_fpath, 'w') as fp:
        fp.write('my brand new test file')
    rdict = test_keystore.add_file('test2.txt')
    assert (type(rdict) is dict)
    assert(rdict['code'] is 0)

def test_remove_file(test_keystore):
    """
    Test the remove file function
    """
    new_fpath = os.path.sep.join([HOME, 'test2.txt'])
    if os.path.exists(new_fpath+'.gpg') is False:
        with open(new_fpath, 'w') as fp:
            fp.write('my brand new test file')
        test_keystore.add_file('test2.txt')
    rdict = test_keystore.remove_file(new_fpath+'.gpg')
    assert (type(rdict) is dict)
    assert (rdict['code'] is 0)


def test_cat_file(test_keystore):
    """
    Test the cat file function
    """
    rdict = test_keystore.cat_file('test1.txt')
    assert (type(rdict) is dict)
    assert(rdict['code'] is 0)
    assert(rdict['stdout'] is not None)
    assert(len(rdict['stdout']) > 0)
