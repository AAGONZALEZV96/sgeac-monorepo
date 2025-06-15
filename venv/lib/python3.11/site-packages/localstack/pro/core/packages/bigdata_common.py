import os
from typing import Dict
from localstack.packages.core import InstallTarget
from localstack.utils.archives import unzip
from localstack.utils.common import cp_r,download,file_exists_not_empty,mkdir
from localstack.utils.files import load_file,new_tmp_dir,rm_rf,save_file
from localstack.utils.testutil import create_zip_file
def download_and_cache_jar_file(jar_url,cache_dir,target_dir):
	E=target_dir;D=cache_dir;C=jar_url;F=C.split('/')[-1];mkdir(E);mkdir(D);B=os.path.join(E,F)
	if file_exists_not_empty(B):return B
	A=os.path.join(D,F)
	if not file_exists_not_empty(A):download(C,A)
	cp_r(A,B);return A
def bigdata_jar_cache_dir(target):return os.path.join(target.value,'bigdata-jars')
def replace_in_zip_file(zip_file,file_path,search_replace,raise_if_missing=False):
	C=zip_file;A=new_tmp_dir();unzip(C,A);B=os.path.join(A,file_path)
	if not os.path.exists(B):
		if raise_if_missing:raise Exception(f"Unable to replace content in non-existing file in archive: {B}")
		return
	replace_in_file(B,search_replace);create_zip_file(A,C);rm_rf(A)
def replace_in_file(file_path,search_replace):
	B=file_path;A=load_file(B)
	for(C,D)in search_replace.items():A=A.replace(C,D)
	save_file(B,A)