from tsp.db_operation import MySQLDB


class AssertInfo:
    data = []


def diff_json(response_data, assert_data):
    """Compare the JSON data format"""
    if isinstance(response_data, dict):
        for key in assert_data:
            if key not in response_data:
                info = f"❌ Response data has no key: {key}"
                print(info)
                AssertInfo.data.append(info)
        for key in response_data:
            if key in assert_data:
                # print(f"校验：{key}:{response_data[key]}")
                diff_json(response_data[key], assert_data[key])
            else:
                info = f"💡 Assert data has not key: {key}"
                print(info)
    elif isinstance(response_data, list):
        if len(response_data) == 0:
            print("response is []")
        if len(response_data) != len(assert_data):
            print(f"list len: '{len(response_data)}' != '{len(assert_data)}'")

        if response_data:
            if isinstance(response_data[0], dict):
                response_data = sorted(response_data, key=lambda x: x[list(response_data[0].keys())[0]])
            else:
                response_data = sorted(response_data)
        if assert_data:
            if isinstance(assert_data[0], dict):
                assert_data = sorted(assert_data, key=lambda x: x[list(assert_data[0].keys())[0]])
            else:
                assert_data = sorted(assert_data)
        print("diff_json")
        print(f"response_data:{response_data}")
        print(f"assert_data:{assert_data}")
        for src_list, dst_list in zip(response_data, assert_data):
            diff_json(src_list, dst_list)
    else:
        if str(response_data) != str(assert_data):
            info = f"❌ Value are not equal: {response_data}"
            print(info)
            AssertInfo.data.append(info)


my_sql_dev = MySQLDB(host="rm-2zef25889658j8c6w.mysql.rds.aliyuncs.com",
                 port=3306,
                 user="peilian",
                 password="qe0SQTOxI34S8W8e",
                 database="peilian")
my_sql_prd = MySQLDB(host="127.0.0.1",
                 port=3391,
                 user="fengxiao",
                 password="3r5VkR3Rq5zekaN2F8",
                 database="peilian")


# tables_dev = my_sql_dev.query_sql("show tables")
tables_prd = my_sql_prd.query_sql("show tables")
# print(tables_prd)
# print(list(set([table["Tables_in_peilian"] for table in tables_dev]).difference(set([table["Tables_in_peilian"] for table in tables_prd]))))

for table in tables_prd:
    print(f"开始比较表：{table['Tables_in_peilian']}")
    # coach_info_dev = my_sql_dev.query_sql(f"desc {table['Tables_in_peilian']}")
    coach_info_dev = my_sql_dev.query_sql(f"desc partner_info")
    # coach_info_prd = my_sql_prd.query_sql(f"desc {table['Tables_in_peilian']}")
    coach_info_prd = my_sql_prd.query_sql(f"desc partner_info")
    print(f"coach_info_dev:{coach_info_dev}")
    print(f"coach_info_prd:{coach_info_prd}")
    diff_json(coach_info_dev, coach_info_prd)
    break
# 比较表的数量
# 比较表一致
# 比较表字段







