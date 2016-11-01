# -*- coding: utf-8 -*-
from nose import with_setup
from nose.tools import nottest, raises
from datetime import datetime, timedelta

@nottest
def blank_setup():
    global now
    test = '2016-10-10 12:30:30'
    now = datetime.strptime(test, '%Y-%m-%d %H:%M:%S')

@with_setup(blank_setup)
def test_string_date_format():
    # string format parsed
    assert str(now.date()) == '2016-10-10'
    assert str(now.time()) == '12:30:30'
    assert now == datetime(2016,10,10,12,30,30)

@with_setup(blank_setup)
def test_after_datetime():
    # 지금보다 2일 뒤
    result = now + timedelta(days=2)
    assert result.strftime('%Y-%m-%d') == '2016-10-12'

    # 지금보다 3초 뒤
    result = now + timedelta(seconds=3)
    assert result.strftime('%Y-%m-%d %H:%M:%S') == '2016-10-10 12:30:33'

