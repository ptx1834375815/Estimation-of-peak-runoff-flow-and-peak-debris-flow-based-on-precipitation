#!/usr/bin/env python3
"""
Created on Thu Feb 27 13:49:03 2020

@author: Chengyan Fan
"""
from data_downloader import downloader

netrc = downloader.Netrc()
netrc.add('urs.earthdata.nasa.gov','ptx@imde.ac.cn','1o12o9oSS..')

from data_downloader import downloader, parse_urls

####################################################################################################
#  在此修改输入输出文件路径
#########################

# 文件输出目录
folder_out = r'D:\wget\GPMfinal07big'
# 包含url的文件路径
url_file = r"D:\wget\GPMfinal07big/final07big.txt"
####################################################################################################

urls = parse_urls.from_urls_file(url_file)
downloader.download_datas(urls, folder_out)
# 通过浏览器方法
# downloader.download_datas(urls, folder_out, authorize_from_browser=True)

