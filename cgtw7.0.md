## 全局公共参数
#### 全局Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 全局Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 全局Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 全局认证方式
```text
noauth
```
#### 全局预执行脚本
```javascript
暂无预执行脚本
```
#### 全局后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0
```text
暂无描述
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
token | - | -
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
apt.globals.set("db", "proj_xiaoying");
apt.globals.set("module", "asset");
apt.globals.set("etask_db", "proj_xiaoying_etask");
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/login
```text
登陆
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/login/login
```text
登陆
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | account | String | 是 | 控制器
data[method] | login | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[account] | xiaoying | String | 是 | 账号
data[password] | a111111 | String | 是 | 密码
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("token", response.json.data.token);
apt.globals.set("account_id", response.json.data.account_id);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"client_type": "py",
		"token": "50E8EB4C-FE99-403A-C3EB-9277359C3CD5",
		"account_id": "B8B95A85-36E8-B6FB-DB78-301A358C77F3",
		"remote_ip": "192.168.199.85",
		"name": "xiaoying",
		"account": "xiaoying",
		"image": "/upload/public/00000000/6ba3b2a8a21ba192d1d76239c3940284_min.jpg",
		"file_key": "48d6d6cd6b9701eeb6ee92b2ed97ea29",
		"update_time": "2023-02-23 08:16:43"
	}
}
```
#### 错误响应示例
```javascript
{
	"code": "0",
	"type": "msg",
	"data": "账号或密码错误,请检查; \n[account::login]"
}
```
## /cgtw7.0/status
```text
状态类(客户端-系统设置-状态管理)
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/status/get_status_and_color
```text
获取所有状态的名称和颜色
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | status | String | 是 | 控制器
data[method] | get_status_and_color | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"Work": "#00DDDC",
		"终审通过": "#0bbf66",
		"客户通过": "#0cc991",
		"Approve": "#0cc991",
		"工程通过": "#0cc991",
		"Unassigned": "#d121b1",
		"内部通过": "#0cc991",
		"导演通过": "#0cc991",
		"等上游文件": "#0e4dab",
		"Check": "#0E86FE",
		"Change_status": "#1553b0",
		"FBX通过": "#178705",
		"客户自定义": "#19355e",
		"Active": "#2e9dff",
		"Revert": "#3E9EFF",
		"Wait": "#5d636b",
		"FBX暂停": "#6f7a25",
		"Ready": "#860EFE",
		"Fix": "#C0C0C0",
		"返给某个环节": "#d48446",
		"FBX返修": "#fc350d",
		"Rework": "#FE5858",
		"Close": "#FEDD15",
		"导演返修": "#ff3d74",
		"客户返修": "#ff3d74",
		"内部返修": "#ff3d74",
		"工程返修": "#ff6952",
		"Retake": "#ff6952",
		"Pause": "#FF9E3E"
	}
}
```
## /cgtw7.0/status/get_filter
```text
获取状态数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | status | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[field_array][] | color | Array | 是 | 字段标识列表
data[filter_array][0][] | status_type | Array | 否 | 过滤语句列表
data[filter_array][0][] | = | Array | 否 | 过滤语句列表
data[filter_array][0][] | check | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"color": "#0E86FE",
			"#id": "d61861d4-2728-473f-b1ac-e93ecc5f38e0"
		}
	]
}
```
## /cgtw7.0/account
```text
账号类(系统设置-账号管理)
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/account/fields
```text
获取账号表的字段标识数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | account | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"account.entity",
		"account.name",
		"account.id",
		"account.status",
		"account.department",
		"account.image",
		"account.password",
		"account.sex",
		"account.mail",
		"account.description",
		"account.signature",
		"account.department_sort_id",
		"account.level",
		"account.team",
		"account.group",
		"account.create_time",
		"account.create_by",
		"account.last_update_time",
		"account.last_update_by",
		"account.talk_permission",
		"account.black_list",
		"account.project_permission",
		"account.mobile",
		"account.position",
		"account.login_ip",
		"account.tag",
		"account.danhang",
		"account.duohang",
		"account.zhengshu",
		"account.xiaoshu",
		"account.liebiao",
		"account.duoxuan",
		"account.biaoqian",
		"account.ziduanbiaoqian",
		"account.jindu",
		"account.meiti",
		"account.chaolianjie",
		"account.riqi",
		"account.fuxuan",
		"account.yonghu",
		"account.yonghu_account_id",
		"account.driver_map",
		"account.liri",
		"account.project_group",
		"account.allow_all_network",
		"account.media",
		"account.login_time",
		"account.expire_time",
		"department.id",
		"department.entity"
	]
}
```
## /cgtw7.0/account/fields_and_str
```text
获取账号表的字段标识与字段名称列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | account | String | 是 | 控制器
data[method] | fields_and_str | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"sign": "account.entity",
			"field_str": "账号"
		},
		{
			"sign": "account.name",
			"field_str": "姓名"
		},
		{
			"sign": "account.id",
			"field_str": "账号ID"
		},
		{
			"sign": "account.status",
			"field_str": "启用状态"
		},
		{
			"sign": "account.department",
			"field_str": "关联部门"
		},
		{
			"sign": "account.image",
			"field_str": "头像"
		},
		{
			"sign": "account.password",
			"field_str": "密码"
		},
		{
			"sign": "account.sex",
			"field_str": "性别"
		},
		{
			"sign": "account.mail",
			"field_str": "邮箱"
		},
		{
			"sign": "account.description",
			"field_str": "描述"
		},
		{
			"sign": "account.signature",
			"field_str": "个人签名"
		},
		{
			"sign": "account.department_sort_id",
			"field_str": "部门序号"
		},
		{
			"sign": "account.level",
			"field_str": "职等"
		},
		{
			"sign": "account.team",
			"field_str": "组别"
		},
		{
			"sign": "account.group",
			"field_str": "权限组"
		},
		{
			"sign": "account.create_time",
			"field_str": "创建时间"
		},
		{
			"sign": "account.create_by",
			"field_str": "创建人员"
		},
		{
			"sign": "account.last_update_time",
			"field_str": "最新编辑时间"
		},
		{
			"sign": "account.last_update_by",
			"field_str": "最新编辑人员"
		},
		{
			"sign": "account.talk_permission",
			"field_str": "聊天权限组"
		},
		{
			"sign": "account.black_list",
			"field_str": "访问项目黑名单"
		},
		{
			"sign": "account.project_permission",
			"field_str": "允许访问项目"
		},
		{
			"sign": "account.mobile",
			"field_str": "手机号"
		},
		{
			"sign": "account.position",
			"field_str": "职位"
		},
		{
			"sign": "account.login_ip",
			"field_str": "登录IP"
		},
		{
			"sign": "account.tag",
			"field_str": "标签"
		},
		{
			"sign": "account.danhang",
			"field_str": "danhang"
		},
		{
			"sign": "account.duohang",
			"field_str": "duohang"
		},
		{
			"sign": "account.zhengshu",
			"field_str": "zhengshu"
		},
		{
			"sign": "account.xiaoshu",
			"field_str": "xiaoshu"
		},
		{
			"sign": "account.liebiao",
			"field_str": "liebiao"
		},
		{
			"sign": "account.duoxuan",
			"field_str": "duoxuan"
		},
		{
			"sign": "account.biaoqian",
			"field_str": "biaoqian"
		},
		{
			"sign": "account.ziduanbiaoqian",
			"field_str": "ziduanbiaoqian"
		},
		{
			"sign": "account.jindu",
			"field_str": "jindu"
		},
		{
			"sign": "account.meiti",
			"field_str": "meiti"
		},
		{
			"sign": "account.chaolianjie",
			"field_str": "chaolianjie"
		},
		{
			"sign": "account.riqi",
			"field_str": "riqi"
		},
		{
			"sign": "account.fuxuan",
			"field_str": "fuxuan"
		},
		{
			"sign": "account.yonghu",
			"field_str": "yonghu"
		},
		{
			"sign": "account.yonghu_account_id",
			"field_str": "yonghu ID"
		},
		{
			"sign": "account.driver_map",
			"field_str": "盘符映射"
		},
		{
			"sign": "account.liri",
			"field_str": "日历"
		},
		{
			"sign": "account.project_group",
			"field_str": "项目组"
		},
		{
			"sign": "account.allow_all_network",
			"field_str": "允许所有网络访问"
		},
		{
			"sign": "account.media",
			"field_str": "media"
		},
		{
			"sign": "account.login_time",
			"field_str": "最后登录时间"
		},
		{
			"sign": "account.expire_time",
			"field_str": "过期时间"
		},
		{
			"sign": "department.id",
			"field_str": "部门ID"
		},
		{
			"sign": "department.entity",
			"field_str": "部门"
		}
	]
}
```
## /cgtw7.0/account/get_id
```text
获取账号表的账号id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | account | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | 5000 | String | 否 | 限制条数,默认5000
data[start_num] | - | String | 否 | 开始条数,默认为""
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"BCCB1378-399A-AF01-D203-9F7A78B69527",
		"001B2CF3-444D-EB5E-F145-BC7CD1B66A03",
		"B0782D6D-B85A-6895-2E16-24E0D7364BD8",
		"009F273A-7351-0F91-888D-55128AD6DA19",
	]
}
```
## /cgtw7.0/account/get
```text
根据ID列表获取记录数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | account | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[sign_array][0] | account.entity | Array | 是 | 字段标识列表
data[id_array][0] | BCCB1378-399A-AF01-D203-9F7A78B69527 | Array | 是 | ID列表
data[order_sign_array][0] | account.entity | Array | 否 | 顺序的字段标识列表
data[limit] | 5000 | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"account.entity": "11",
			"id": "BCCB1378-399A-AF01-D203-9F7A78B69527"
		}
	]
}
```
#### 错误响应示例
```javascript
{
	"code": "0",
	"type": "msg",
	"data": "ERROR:  syntax error at end of input\nLINE 1: ...) order by COALESCE(account.json_data->>'entity', '') limit \n                                                                       ^"
}
```
## /cgtw7.0/account/get_filter
```text
获取账号表的记录数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | account | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[sign_array][] | account.entity | Array | 是 | 字段标识列表
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | String | 否 | 限制条数(默认5000条)
data[order_sign_list] | - | Array | 否 | 顺序的字段标识列表 (list)
data[start_num] | - | String | 否 | 开始条数 (str/unicode), 默认为""
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.assert('response.raw.status==200');
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"account.entity": "11",
			"id": "BCCB1378-399A-AF01-D203-9F7A78B69527"
		}
	]
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
code | 1 | String | -
type | json | String | -
data | - | Array | -
data.account.entity | 11 | String | -
data.id | BCCB1378-399A-AF01-D203-9F7A78B69527 | String | -
#### 错误响应示例
```javascript
{
	"code": "0",
	"type": "msg",
	"data": "filter_array错误, (!)不在(!=,=,~,<,>,<=,>=,has,!has,in,concat,!concat,start,end,is)中; \n[fsql::get_sql_filter_array]"
}
```
## /cgtw7.0/account/count
```text
统计记录条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | account | String | 是 | 控制器
data[method] | count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "1048"
}
```
## /cgtw7.0/account/distinct
```text
获取去重后的记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | account | String | 是 | 控制器
data[method] | distinct | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[distinct_sign] | account.department | String | 是 | 字段标识
data[filter_list] | - | Array | 否 | 过滤语句列表
data[order_sign_array] | - | Array | 否 | 顺序的字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"绑定组",
		"原画组",
		"外包",
		"贴图组",
		"系统组",
		"合成组",
		"模型组",
		"灯光组",
		"模型一组",
		"动画组",
	]
}
```
## /cgtw7.0/account/group_count
```text
按字段标识进行分组统计条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | account | String | 是 | 控制器
data[method] | group_count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[sign_array][] | account.department | Array | 是 | 字段标识列表
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"count": 2,
			"account.department": "绑定组"
		},
		{
			"count": 12,
			"account.department": "原画组"
		},
		{
			"count": 3,
			"account.department": "外包"
		},
		{
			"count": 4,
			"account.department": "贴图组"
		},
		{
			"count": 9,
			"account.department": "系统组"
		},
		{
			"count": 2,
			"account.department": "合成组"
		},
		{
			"count": 3,
			"account.department": "模型组"
		},
		{
			"count": 2,
			"account.department": "灯光组"
		},
		{
			"count": 2,
			"account.department": "模型一组"
		},
		{
			"count": 1,
			"account.department": "动画组"
		}
	]
}
```
## /cgtw7.0/account/set
```text
更新记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | account | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[id_array][0] | {{account_id}} | Array | 是 | ID列表 (list)
data[sign_data_array][account.mail] | 11@email.com | Array | 是 | 更新的数据(dict), 格式:{"字段标识" : "值", "字段标识" : "值" }
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/project
```text
项目表(客户端-项目)
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/project/fields
```text
获取项目表所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"project.entity",
		"project.full_name",
		"project.id",
		"project.status",
		"project.database",
		"project.color",
		"project.start_date",
		"project.end_date",
		"project.image",
		"project.description",
		"project.frame_rate",
		"project.resolution",
		"project.create_time",
		"project.create_by",
		"project.last_update_time",
		"project.last_update_by",
		"project.template",
		"project.tag",
		"project.is_etask",
		"project.text",
		"project.mtext",
		"project.integer",
		"project.decimals",
		"project.list",
		"project.multiple_choice_list",
		"project.media",
		"project.hyperlink",
		"project.date_and_time",
		"project.check_box",
		"project.user",
		"project.user_account_id",
		"project.project_fps",
		"project.project_resolution",
		"project.colorspace",
		"project.custom_colorspace",
		"project.project_group",
		"project.video_author",
		"project.template_id"
	]
}
```
## /cgtw7.0/project/fields_and_str
```text
获取所有字段标识和中文名
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | fields_and_str | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"sign": "project.entity",
			"field_str": "项目代号"
		},
		{
			"sign": "project.full_name",
			"field_str": "项目全称"
		},
		{
			"sign": "project.id",
			"field_str": "项目ID"
		},
		{
			"sign": "project.status",
			"field_str": "状态"
		},
		{
			"sign": "project.database",
			"field_str": "数据库"
		},
		{
			"sign": "project.color",
			"field_str": "颜色"
		},
		{
			"sign": "project.start_date",
			"field_str": "开始日期"
		},
		{
			"sign": "project.end_date",
			"field_str": "结束日期"
		},
		{
			"sign": "project.image",
			"field_str": "项目缩略图"
		},
		{
			"sign": "project.description",
			"field_str": "描述"
		},
		{
			"sign": "project.frame_rate",
			"field_str": "帧率"
		},
		{
			"sign": "project.resolution",
			"field_str": "分辨率"
		},
		{
			"sign": "project.create_time",
			"field_str": "创建时间"
		},
		{
			"sign": "project.create_by",
			"field_str": "创建人员"
		},
		{
			"sign": "project.last_update_time",
			"field_str": "最新编辑时间"
		},
		{
			"sign": "project.last_update_by",
			"field_str": "最新编辑人员"
		},
		{
			"sign": "project.template",
			"field_str": "模板"
		},
		{
			"sign": "project.tag",
			"field_str": "标签"
		},
		{
			"sign": "project.is_etask",
			"field_str": "简易版项目"
		},
		{
			"sign": "project.text",
			"field_str": "单行文本"
		},
		{
			"sign": "project.mtext",
			"field_str": "多行文本"
		},
		{
			"sign": "project.integer",
			"field_str": "整数"
		},
		{
			"sign": "project.decimals",
			"field_str": "小数"
		},
		{
			"sign": "project.list",
			"field_str": "列表"
		},
		{
			"sign": "project.multiple_choice_list",
			"field_str": "多选列表"
		},
		{
			"sign": "project.media",
			"field_str": "媒体"
		},
		{
			"sign": "project.hyperlink",
			"field_str": "超链接"
		},
		{
			"sign": "project.date_and_time",
			"field_str": "日期时间"
		},
		{
			"sign": "project.check_box",
			"field_str": "复选框"
		},
		{
			"sign": "project.user",
			"field_str": "用户"
		},
		{
			"sign": "project.user_account_id",
			"field_str": "用户 ID"
		},
		{
			"sign": "project.aa",
			"field_str": "aa"
		},
		{
			"sign": "project.project_fps",
			"field_str": "项目帧率"
		},
		{
			"sign": "project.project_resolution",
			"field_str": "项目分辨率"
		},
		{
			"sign": "project.colorspace",
			"field_str": "色彩空间"
		},
		{
			"sign": "project.custom_colorspace",
			"field_str": "自定义色彩空间"
		},
		{
			"sign": "project.project_group",
			"field_str": "项目组"
		},
		{
			"sign": "project.video_author",
			"field_str": "video_author"
		},
		{
			"sign": "project.template_id",
			"field_str": "模板ID"
		}
	]
}
```
## /cgtw7.0/project/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[sign_filter_array] | project.entity | Array | 否 | 过滤语句列表
data[limit] | 5000 | String | 否 | 限制条数
data[start_num] | - | String | 否 | 开始条数,默认为""
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"10E99ACF-FBB2-05B6-140A-B6F1D19B7F74"
	]
}
```
## /cgtw7.0/project/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[sign_array][] | project.database | Array | 是 | 字段标识列表
data[id_array][] | 10E99ACF-FBB2-05B6-140A-B6F1D19B7F74 | Array | 是 | ID列表
data[order_sign_array] | - | Array | 否 | 顺序的字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"project.database": "proj_big",
			"id": "10E99ACF-FBB2-05B6-140A-B6F1D19B7F74"
		}
	]
}
```
## /cgtw7.0/project/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[sign_array][] | project.database | Array | 是 | 字段标识列表
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | 5000 | String | 否 | 限制条数,默认5000
data[order_sign_list] | project.entity | Array | 否 | 顺序的字段标识列表
data[start_num] | - | String | 否 | 开始条数,默认为""
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"project.database": "proj_big",
			"id": "10E99ACF-FBB2-05B6-140A-B6F1D19B7F74"
		}
	]
}
```
## /cgtw7.0/project/set
```text
更新记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[id_array][] | BD81305D-C902-443A-9F49-864F9EDC06CD | Array | 是 | ID列表
data[sign_data_array][project.frame_rate] | 24 | Array | 是 | 更新的数据(dict), 格式:{"字段标识" : "值", "字段标识" : "值" }
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/project/count
```text
统计记录条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "84"
}
```
## /cgtw7.0/project/distinct
```text
获取去重后的记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | distinct | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[distinct_sign] | project.database | String | 是 | 字段标识
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[order_sign_array][] | - | Array | 否 | 顺序的字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"proj_001",
		"proj_big"
	]
}
```
## /cgtw7.0/project/group_count
```text
按字段标识进行分组统计条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | group_count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[sign_array][] | project.entity | Array | 是 | 字段标识列表
data[sign_filter_array] | - | Array | 是 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"count": 1,
			"project.entity": "001"
		},
		{
			"count": 1,
			"project.entity": "003"
		},
		{
			"count": 1,
			"project.entity": "11"
		}
	]
}
```
## /cgtw7.0/project/get_members
```text
获取项目成员
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | get_members | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"76ae9e2f-7067-409a-9319-f538c68dcde4",
		"912E47F0-7A27-6970-5DCA-E41EDB33BF72",
		"C07A29BB-0B32-D17E-47DD-56A4A3A9A3ED",
		"0502AD9B-5A38-B9AB-7E39-00F7C0B9B3A0",
		"F2E31BCA-63C9-55A2-3D24-5FF65CC5C20F",
		"1111",
		"18BE1FB1-5CFA-C535-7E9D-ED69CAA77A45",
		"615FB209-94FA-D916-FE75-36F48068F6FA",
		"9725B50D-9770-D20D-E341-A1C6A891CE7B",
		"051AC3A2-A5BD-C872-48D5-E0B1437897D1",
		"CDED35CB-BF74-CE19-C5D0-55053E93614B",
		"AD46F080-56C8-4C47-FBC0-8F17776B6AC6",
		"87db8934-e479-4f00-89a7-5a59df0d9130",
		"3A6B5820-55AE-E14E-77BF-16DA98840AD2",
		"7AAA4D2B-1F53-EE4F-68FB-47B9A317B4DC",
		"81269A61-D620-5BF4-CAF3-51EA840CF904",
		"6D145817-39A4-46DA-8B9A-4ADE6D46334E",
		"2E3E48BC-D7F9-4C00-96BB-64F8EC4E078A",
		"DFABAA85-47E8-D4A7-968B-1D9677E90D91",
		"6DA2BB75-4DEC-BF7A-2D66-334AEACF9742",
		"D29791AB-893D-DE54-13D3-7C941C25B33F",
		"B8B95A85-36E8-B6FB-DB78-301A358C77F3",
		"A98C9570-F63D-84A5-1620-3EA8CB13D87E",
		"5AF63FD8-9098-F970-012E-85BB50E248C9",
		"DAB78B25-3F74-3DCB-E0CD-DF6B53BAFB0E",
		"C84FF25F-D83F-CC64-E992-5D41ED1DCDFE",
		"5302BCDD-14FD-6E1D-AE51-C29527C07F66",
		"9D6EB9FC-9B03-DDE7-8C2C-0DA74FDC36C4",
		"F9D85EE6-9876-9BAE-154A-4238FF4E76DD",
		"E4AD7EA2-9596-298B-BB10-AB6F984D26B8",
		"C6B55D87-82BB-463D-D05D-A981B8D1D260",
		"C7EF3F80-2A57-198B-5889-80DADA08E3C3",
		"73825608-A6F7-CBEC-C8F1-2C0825330EE9",
		"264BC0E5-3BE5-D7E6-675D-F4ED654CFE25",
		"FBD2C1A4-5E2E-496A-DF53-71669098592C",
		"E1EA3934-C8D9-0B07-C5FC-C587718E2336",
		"037634F0-53BD-8BAA-6FD3-5A9758B18CB0",
		"8bdb8934-e4d9-4f00-89a7-5a59dfefe9we",
		"EE93BE0D-6DC5-19EF-BE72-E5CECD8386D6",
		"8A0CCAA1-B2F4-218A-4709-6348412AC717"
	]
}
```
## /cgtw7.0/project/is_etask
```text
判断项目是否是简易版
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | is_etask | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/project/create
```text
创建项目
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | project | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[field_data_array][entity] | - | String | 是 | 项目名称
data[field_data_array][full_name] | - | String | 是 | -
data[template_id] | - | String | 是 | 模板id
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"project.entity",
		"project.full_name",
		"project.id",
		"project.status",
		"project.database",
		"project.color",
		"project.start_date",
		"project.end_date",
		"project.image",
		"project.description",
		"project.frame_rate",
		"project.resolution",
		"project.create_time",
		"project.create_by",
		"project.last_update_time",
		"project.last_update_by",
		"project.template",
		"project.tag",
		"project.is_etask",
		"project.text",
		"project.mtext",
		"project.integer",
		"project.decimals",
		"project.list",
		"project.multiple_choice_list",
		"project.media",
		"project.hyperlink",
		"project.date_and_time",
		"project.check_box",
		"project.user",
		"project.user_account_id",
		"project.project_fps",
		"project.project_resolution",
		"project.colorspace",
		"project.custom_colorspace",
		"project.project_group",
		"project.video_author",
		"project.template_id"
	]
}
```
## /cgtw7.0/info
```text
高级版-信息接口
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/info/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"asset.entity",
		"asset.cn_name",
		"asset.id",
		"asset.image",
		"asset.assign_pipeline",
		"asset.create_time",
		"asset.create_by",
		"asset.last_update_time",
		"asset.last_update_by",
		"asset.link_shot",
		"asset.pid_QVRRVDRO_VQEQ_QTUR_XAFB_XFAVRDUAXVWS",
		"asset.pid_DCFXFRBQ_UQRS_QACB_OUOX_AWAWTSEAREEE",
		"asset.pid_OPEBARCQ_DAAR_WSOR_ACQX_WORWBUDDVSCO",
		"asset.pid_PVCSBDVX_SBFO_BWES_OTBW_DOOERPXPBOXQ",
		"asset.pipeline_template_name",
		"asset.link_asset_type",
		"asset.lineedit",
		"asset.textedit",
		"asset.int",
		"asset.float",
		"asset.list",
		"asset.mullist",
		"asset.tag",
		"asset.media",
		"asset.link",
		"asset.datetime",
		"asset.checkbox",
		"asset.pipeline_template_id",
		"asset.url",
		"asset.url_id",
		"asset.frame",
		"asset.zcfs",
		"asset.zznd",
		"asset.zcdj",
		"asset.status",
		"asset.pack_time",
		"asset.artist",
		"asset.account_id",
		"asset.sanqi_muliselect",
		"asset.sanqi_tongji",
		"asset.colorrgb",
		"asset.rig_version",
		"asset.sync_task_name",
		"asset.asset_summary",
		"asset.link_eps",
		"asset.geng_hao_san_link_eps",
		"asset.ln_eps",
		"asset.test_create",
		"asset_type.id",
		"asset_type.entity",
		"asset_type.url",
		"asset_type.url_id",
		"asset_type.artist",
		"asset_type.account_id"
	]
}
```
## /cgtw7.0/info/modules
```text
获取所有模块
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | modules | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"shot",
		"test_module",
		"asset_type",
		"cgtw_unreal_version",
		"eps",
		"cross_module",
		"asset"
	]
}
```
## /cgtw7.0/info/fields_and_str
```text
获取所有字段标识和中文名
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | fields_and_str | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"sign": "asset.entity",
			"field_str": "资产名称"
		},
		{
			"sign": "asset.cn_name",
			"field_str": "中文名"
		},
		{
			"sign": "asset.id",
			"field_str": "资产ID"
		},
		{
			"sign": "asset.image",
			"field_str": "信息缩略图"
		},
		{
			"sign": "asset.assign_pipeline",
			"field_str": "已经分配阶段"
		},
		{
			"sign": "asset.create_time",
			"field_str": "创建时间"
		},
		{
			"sign": "asset.create_by",
			"field_str": "创建人员"
		},
		{
			"sign": "asset.last_update_time",
			"field_str": "最新编辑时间"
		},
		{
			"sign": "asset.last_update_by",
			"field_str": "最新编辑人员"
		},
		{
			"sign": "asset.link_shot",
			"field_str": "关联shot"
		},
		{
			"sign": "asset.pid_QVRRVDRO_VQEQ_QTUR_XAFB_XFAVRDUAXVWS",
			"field_str": "Design_status"
		},
		{
			"sign": "asset.pid_DCFXFRBQ_UQRS_QACB_OUOX_AWAWTSEAREEE",
			"field_str": "Mod_status"
		},
		{
			"sign": "asset.pid_OPEBARCQ_DAAR_WSOR_ACQX_WORWBUDDVSCO",
			"field_str": "Texture_status"
		},
		{
			"sign": "asset.pid_PVCSBDVX_SBFO_BWES_OTBW_DOOERPXPBOXQ",
			"field_str": "Rig_status"
		},
		{
			"sign": "asset.pipeline_template_name",
			"field_str": "阶段流程"
		},
		{
			"sign": "asset.link_asset_type",
			"field_str": "关联资产类型"
		},
		{
			"sign": "asset.lineedit",
			"field_str": "lineedit"
		},
		{
			"sign": "asset.textedit",
			"field_str": "textedit"
		},
		{
			"sign": "asset.int",
			"field_str": "int"
		},
		{
			"sign": "asset.float",
			"field_str": "float"
		},
		{
			"sign": "asset.list",
			"field_str": "list"
		},
		{
			"sign": "asset.mullist",
			"field_str": "mullist"
		},
		{
			"sign": "asset.tag",
			"field_str": "tag"
		},
		{
			"sign": "asset.media",
			"field_str": "media"
		},
		{
			"sign": "asset.link",
			"field_str": "link"
		},
		{
			"sign": "asset.datetime",
			"field_str": "datetime"
		},
		{
			"sign": "asset.checkbox",
			"field_str": "checkbox"
		},
		{
			"sign": "asset.pipeline_template_id",
			"field_str": "阶段模板ID"
		},
		{
			"sign": "asset.url",
			"field_str": "Url"
		},
		{
			"sign": "asset.url_id",
			"field_str": "Url ID"
		},
		{
			"sign": "asset.frame",
			"field_str": "帧数"
		},
		{
			"sign": "asset.zcfs",
			"field_str": "资产分属"
		},
		{
			"sign": "asset.zznd",
			"field_str": "制作难度"
		},
		{
			"sign": "asset.zcdj",
			"field_str": "资产单价"
		},
		{
			"sign": "asset.status",
			"field_str": "资产总状态"
		},
		{
			"sign": "asset.pack_time",
			"field_str": "打包时间"
		},
		{
			"sign": "asset.artist",
			"field_str": "信息制作者"
		},
		{
			"sign": "asset.account_id",
			"field_str": "信息制作者ID"
		},
		{
			"sign": "asset.sanqi_muliselect",
			"field_str": "三七多选集数"
		},
		{
			"sign": "asset.sanqi_tongji",
			"field_str": "三七集数统计"
		},
		{
			"sign": "asset.colorrgb",
			"field_str": "颜色RGB测试"
		},
		{
			"sign": "asset.rig_version",
			"field_str": "Rig 版本"
		},
		{
			"sign": "asset.sync_task_name",
			"field_str": "任务名称同步"
		},
		{
			"sign": "asset.asset_summary",
			"field_str": "资产汇总"
		},
		{
			"sign": "asset.link_eps",
			"field_str": "关联eps"
		},
		{
			"sign": "asset.geng_hao_san_link_eps",
			"field_str": "更号三-关联集数同步字段"
		},
		{
			"sign": "asset.ln_eps",
			"field_str": "关联集数"
		},
		{
			"sign": "asset.test_create",
			"field_str": "test_create"
		},
		{
			"sign": "asset_type.id",
			"field_str": "资产类型ID"
		},
		{
			"sign": "asset_type.entity",
			"field_str": "资产类型"
		},
		{
			"sign": "asset_type.url",
			"field_str": "Url"
		},
		{
			"sign": "asset_type.url_id",
			"field_str": "Url ID"
		},
		{
			"sign": "asset_type.artist",
			"field_str": "信息制作者"
		},
		{
			"sign": "asset_type.account_id",
			"field_str": "信息制作者ID"
		}
	]
}
```
## /cgtw7.0/info/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[start_num] | - | String | 否 | 开始条数,默认为""
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"849D6CD8-7D37-B37B-492A-91C3726A0717",
		"A58016E1-5E0D-3A2D-6C18-0EC1E6494B14",
		"5D9BB5C2-D218-3E3E-93CD-A8D2EB61E2E9",
		"B3C9EEF1-AAF5-622B-1D6C-99EC12FA6C05",
		"3ADACCAA-4652-03BE-D9AB-043FCE8CD735",
		"B390809D-09F0-04AD-1BA3-F8E80939AA20"
	]
}
```
## /cgtw7.0/info/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[sign_array][] | asset.entity | Array | 是 | 字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[start_num] | - | String | 否 | 开始条数,默认为""
data[order_sign_array] | - | Array | 否 | 顺序的字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"asset.entity": "cat001",
			"id": "849D6CD8-7D37-B37B-492A-91C3726A0717"
		},
		{
			"asset.entity": "cat002",
			"id": "A58016E1-5E0D-3A2D-6C18-0EC1E6494B14"
		},
		{
			"asset.entity": "cat003",
			"id": "5D9BB5C2-D218-3E3E-93CD-A8D2EB61E2E9"
		},
		{
			"asset.entity": "sc01_v00002",
			"id": "B3C9EEF1-AAF5-622B-1D6C-99EC12FA6C05"
		},
		{
			"asset.entity": "sc01_v00017",
			"id": "3ADACCAA-4652-03BE-D9AB-043FCE8CD735"
		},
		{
			"asset.entity": "shot01_010",
			"id": "B390809D-09F0-04AD-1BA3-F8E80939AA20"
		}
	]
}
```
## /cgtw7.0/info/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[sign_array][] | asset.entity | Array | 是 | 字段标识列表
data[id_array][] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | Array | 是 | ID列表
data[order_sign_array] | - | Array | 否 | 顺序的字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"asset.entity": "cat001",
			"id": "849D6CD8-7D37-B37B-492A-91C3726A0717"
		}
	]
}
```
## /cgtw7.0/info/get_dir
```text
用目录标识列表获取对应的目录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | get_dir | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | Array | 是 | ID列表
data[sign_array][] | asset_source | Array | 是 | 目录标识列表
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "849D6CD8-7D37-B37B-492A-91C3726A0717",
			"asset_source": "a:/xiaoying/Asset/Chars/cat001/source"
		}
	]
}
```
## /cgtw7.0/info/get_field_and_dir
```text
用目录标识列表和字段标识列表获取对应的目录和字段列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | get_field_and_dir | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | Array | 是 | ID列表
data[folder_sign_array][] | asset_source | Array | 是 | 目录标识列表
data[os] | win | String | 是 | 系统平台
data[field_sign_array][] | asset.entity | Array | 是 | 字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"asset.entity": "cat001",
			"id": "849D6CD8-7D37-B37B-492A-91C3726A0717",
			"asset_source": "a:/xiaoying/Asset/Chars/cat001/source"
		}
	]
}
```
## /cgtw7.0/info/get_makedirs
```text
获取创建目录的列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | get_makedirs | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | Array | 是 | ID列表
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"z:/11",
		"a:/xiaoying/Asset/Chars/cat001/Design/check",
		"a:/xiaoying/Asset/Chars/cat001/Design/work",
		"a:/xiaoying/Asset/Chars/cat001/Design/approve",
		"a:/xiaoying/Asset/Chars/cat001/Design/file_ver",
		"a:/xiaoying/Asset/Chars/cat001/Design/same_ver",
		"a:/xiaoying/Asset/Chars/cat001/Design",
		"a:/xiaoying/Asset/Chars/cat001/Mod/check",
		"a:/xiaoying/Asset/Chars/cat001/Mod/work",
		"a:/xiaoying/Asset/Chars/cat001/Mod/approve",
		"a:/xiaoying/Asset/Chars/cat001/Texture/check",
		"a:/xiaoying/Asset/Chars/cat001/Texture/work",
		"a:/xiaoying/Asset/Chars/cat001/Texture/approve",
		"a:/xiaoying/Asset/Chars/cat001/Texture/Texture",
		"a:/xiaoying/Asset/Chars/cat001/Rig/check",
		"a:/xiaoying/Asset/Chars/cat001/Rig/work",
		"a:/xiaoying/Asset/Chars/cat001/Rig/approve",
		"a:/xiaoying/Asset/Chars/cat001/Rig/file_version",
		"a:/xiaoying/Asset/Chars/cat001/source",
		"a:/xiaoying/Shot/Layout",
		"a:/xiaoying/Shot/Animation",
		"a:/xiaoying/Shot/Lighting",
		"a:/xiaoying/Shot/VFX",
		"a:/xiaoying/Shot/Comp",
		"a:/xiaoying/Shot/Source",
		"a:/xiaoying/Shot",
		"a:/xiaoying/Audio",
		"a:/xiaoying/Audio/2023-02-27",
		"a:/xiaoying/Animatic",
		"a:/xiaoying/Storyboard",
		"a:/xiaoying/Reference",
		"a:/xiaoying/20230227",
		"a:/ref_1",
		"a:/source",
		"a:/file_ver"
	]
}
```
## /cgtw7.0/info/get_sign_filebox
```text
根据文件框标识获取文件框设置信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | get_sign_filebox | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | Array | 是 | ID列表
data[os] | win | String | 是 | 系统平台
data[filebox_sign] | source | String | 是 | 文件框标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"849D6CD8-7D37-B37B-492A-91C3726A0717": {
			"ref_task_id_list": [],
			"ref_pipeline_id": "",
			"#id": "9BC82220-B4BD-9101-AF40-0D26156AD36D",
			"path": "a:/xiaoying/Asset/Chars/cat001/source",
			"server": "a:/",
			"server_id": "271E10CC-A6BA-F359-073F-FBC355198353",
			"pipeline_id": "",
			"title": "source",
			"sign": "source",
			"color": "#FEC20E",
			"rule": [
				"*"
			],
			"rule_view": [
				"*"
			],
			"show_type": "Files and Folders",
			"is_drag_in": "Y",
			"is_ref": "",
			"ref_id": "",
			"is_approve_version": "",
			"is_upload_online": "N",
			"online_upload_group": "all",
			"convert_type": [],
			"is_version": "N",
			"version_type": "same",
			"version_length": "3",
			"is_upgrade_version": "N",
			"is_follow": "N",
			"follow_sign": "",
			"submit_type": "",
			"drag_in": [
				{
					"plugin_id": "check_rule"
				}
			],
			"is_move_old_to_history": "N",
			"is_move_same_to_history": "N",
			"is_in_history_add_version": "N",
			"is_in_history_add_datetime": "N",
			"is_cover_disable": "N",
			"is_msg_to_first_qc": "N",
			"show_group_id": "all",
			"max_version": "",
			"max_version_id": "",
			"version_list": [],
			"version_id_list": [],
			"last_max_version": "",
			"last_max_version_id": "",
			"last_link_id": "",
			"follow_version": "",
			"follow_title": "",
			"is_submit": "N",
			"reviewer_account_id": ""
		}
	}
}
```
## /cgtw7.0/info/get_filebox
```text
获取文件框设置信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | get_filebox | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | String | 是 | ID
data[os] | win | String | 是 | 系统平台
data[filebox_id] | 9BC82220-B4BD-9101-AF40-0D26156AD36D | String | 是 | 文件框标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"ref_task_id_list": [],
		"ref_pipeline_id": "",
		"#id": "9BC82220-B4BD-9101-AF40-0D26156AD36D",
		"path": "a:/xiaoying/Asset/Chars/cat001/source",
		"server": "a:/",
		"server_id": "271E10CC-A6BA-F359-073F-FBC355198353",
		"pipeline_id": "",
		"title": "source",
		"sign": "source",
		"color": "#FEC20E",
		"rule": [
			"*"
		],
		"rule_view": [
			"*"
		],
		"show_type": "Files and Folders",
		"is_drag_in": "Y",
		"is_ref": "",
		"ref_id": "",
		"is_approve_version": "",
		"is_upload_online": "N",
		"online_upload_group": "all",
		"convert_type": [],
		"is_version": "N",
		"version_type": "same",
		"version_length": "3",
		"is_upgrade_version": "N",
		"is_follow": "N",
		"follow_sign": "",
		"submit_type": "",
		"drag_in": [
			{
				"plugin_id": "check_rule"
			}
		],
		"is_move_old_to_history": "N",
		"is_move_same_to_history": "N",
		"is_in_history_add_version": "N",
		"is_in_history_add_datetime": "N",
		"is_cover_disable": "N",
		"is_msg_to_first_qc": "N",
		"show_group_id": "all",
		"max_version": "",
		"max_version_id": "",
		"version_list": [],
		"version_id_list": [],
		"last_max_version": "",
		"last_max_version_id": "",
		"last_link_id": "",
		"follow_version": "",
		"follow_title": "",
		"is_submit": "N",
		"reviewer_account_id": ""
	}
}
```
## /cgtw7.0/info/set
```text
更新记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | Array | 是 | ID列表
data[sign_data_array][asset.cn_name] | 11 | Array | 是 | 更新的数据(dict), 格式:{"字段标识" : "值", "字段标识" : "值" }
data[exec_event_filter] | - | Boolean | 否 | 执行事件过滤器
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/info/delete
```text
删除记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | delete | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | 849D6CD8-7137-B37B-492A-91C3726A0717 | Array | 是 | ID列表
data[exec_event_filter] | - | Boolean | 是 | 执行事件过滤器
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/info/create
```text
创建记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[sign_data_array][asset.entity] | test_create | Array | 是 | 更新的数据(dict), 格式:{"字段标识" : "值", "字段标识" : "值" }
data[sign_data_array][asset_type.id] | 5F42E769-ADBF-5131-4172-26D107BB255E | Array | 是 | 更新的数据(dict), 格式:{"字段标识" : "值", "字段标识" : "值" }
data[check_unique] | - | Boolean | 否 | 检查唯一值
data[exec_event_filter] | - | Boolean | 否 | 执行事件过滤器
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "EC66ABC4-9C21-BD9C-12C5-52C8B3EC41D0"
}
```
## /cgtw7.0/info/count
```text
统计记录条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "9"
}
```
## /cgtw7.0/info/distinct
```text
获取去重后的记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | distinct | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[distinct_sign] | asset_type.entity | String | 是 | 字段标识
data[order_sign_array] | - | Array | 否 | 顺序的字段标识列表
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"Chars",
		"Sets"
	]
}
```
## /cgtw7.0/info/group_count
```text
按字段标识进行分组统计条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | group_count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[sign_filter_array] | - | String | 否 | 过滤语句列表
data[sign_array][] | asset.entity | String | 是 | 字段标识列表
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"count": 1,
			"asset.entity": "cat001"
		},
		{
			"count": 1,
			"asset.entity": "cat002"
		},
		{
			"count": 2,
			"asset.entity": "cat003"
		},
		{
			"count": 1,
			"asset.entity": "sc001"
		},
		{
			"count": 1,
			"asset.entity": "sc01_v00002"
		},
		{
			"count": 1,
			"asset.entity": "sc01_v00017"
		},
		{
			"count": 1,
			"asset.entity": "shot01_010"
		},
		{
			"count": 1,
			"asset.entity": "test_create"
		}
	]
}
```
## /cgtw7.0/info/send_msg
```text
给指定用户发送任务相关消息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | info | String | 是 | 控制器
data[method] | send_msg | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[account_id_array] | {{account_id}} | String | 是 | -
data[task_id] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | String | 是 | Id
data[content][] | - | Array | 是 | 发送的内容
data[important] | - | Boolean | 否 | 是否强提醒
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/task
```text
高级版-任务接口
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/task/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_big | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"asset.entity",
		"asset.cn_name",
		"asset.id",
		"asset.image",
		"asset.assign_pipeline",
		"asset.create_time",
		"asset.create_by",
		"asset.last_update_time",
		"asset.last_update_by",
		"asset.link_shot",
		"asset.pid_QVRRVDRO_VQEQ_QTUR_XAFB_XFAVRDUAXVWS",
		"asset.pid_DCFXFRBQ_UQRS_QACB_OUOX_AWAWTSEAREEE",
		"asset.pid_OPEBARCQ_DAAR_WSOR_ACQX_WORWBUDDVSCO",
		"asset.pid_PVCSBDVX_SBFO_BWES_OTBW_DOOERPXPBOXQ",
		"asset.pipeline_template_name",
		"asset.link_eps",
		"asset.link_asset_type",
		"asset.lineedit",
		"asset.textedit",
		"asset.int",
		"asset.float",
		"asset.list",
		"asset.mullist",
		"asset.tag",
		"asset.media",
		"asset.link",
		"asset.datetime",
		"asset.checkbox",
		"asset.pipeline_template_id",
		"asset.url",
		"asset.url_id",
		"asset.zcfs",
		"asset.zznd",
		"asset.zcdj",
		"asset.status",
		"asset.pack_time",
		"asset.artist",
		"asset.account_id",
		"asset.sanqi_muliselect",
		"asset.sanqi_tongji",
		"asset.colorrgb",
		"asset.rig_version",
		"asset.sync_task_name",
		"asset.asset_summary",
		"asset.geng_hao_san_link_eps",
		"asset.ln_eps",
		"asset_type.id",
		"asset_type.entity",
		"asset_type.url",
		"asset_type.url_id",
		"asset_type.artist",
		"asset_type.account_id",
		"eps.entity",
		"eps.id",
		"eps.project_code",
		"eps.project_description",
		"eps.create_time",
		"eps.create_by",
		"eps.last_update_time",
		"eps.last_update_by",
		"eps.image",
		"eps.url",
		"eps.url_id",
		"eps.fps",
		"eps.frame_rate",
		"eps.erfwer",
		"eps.zzzz",
		"eps.shuoming",
		"eps.artist",
		"eps.account_id",
		"eps.status",
		"pipeline.id",
		"pipeline.entity",
		"pipeline.abridge",
		"pipeline.sort_id",
		"task.image",
		"task.start_date",
		"task.end_date",
		"task.dead_line",
		"task.status",
		"task.finish_time",
		"task.first_submit_time",
		"task.entity",
		"task.id",
		"task.assign_time",
		"task.last_submit_time",
		"task.pipeline",
		"task.pipeline_id",
		"task.flow_finish_id",
		"task.account_id",
		"task.artist",
		"task.leader_status",
		"task.director_status",
		"task.client_status",
		"task.flow_id",
		"task.pipeline_sort_id",
		"task.note_num",
		"task.difficulty_level",
		"task.days",
		"task.submit_count",
		"task.assign_artist",
		"task.flow_name",
		"task.url",
		"task.total_use_time",
		"task.leader_status_retake_count",
		"task.director_status_retake_count",
		"task.client_status_retake_count",
		"task.create_time",
		"task.create_by",
		"task.last_update_time",
		"task.url_id",
		"task.last_update_by",
		"task.start_work_time",
		"task.remaining_day",
		"task.qc_remaining_day",
		"task.factor",
		"task.finish_diff",
		"task.submit_diff",
		"task.overdue",
		"task.account",
		"task.module",
		"task.last_retake_time",
		"task.file_status",
		"task.review_show_data",
		"task.priority",
		"task.score",
		"task.check_field",
		"task.expected_time",
		"task.product_director",
		"task.check_field_sign",
		"task.version_data",
		"task.status_note_id",
		"task.tag",
		"task.task_frame",
		"task.task_script",
		"task.pack_time",
		"task.duration",
		"task.frame",
		"task.api_create",
		"task.text",
		"task.image_test",
		"task.gcnbsh",
		"task.tgwjzzsh",
		"task.last_review_version_id",
		"task.bbb",
		"task.leader_status_approve_count",
		"task.field_tag",
		"task.link_id",
		"task.sub_pipeline_id",
		"task.status_retake_count",
		"task.version",
		"task.yilai",
		"task.ak_multi_list",
		"task.ak_single_list",
		"task.jindu",
		"task.kaiguan",
		"task.lianjie",
		"task.director_status_approve_count",
		"task.fbxreview",
		"task.tgareview",
		"task.reviewer",
		"task.reviewer_account_id",
		"task.testtime",
		"task.zhimingxingtong_taskartist",
		"task.zhimingxingtong_taskartist_account_id",
		"task.status_note",
		"task.yhtest",
		"task.yhtest_account_id",
		"task.service_supply_partner",
		"task.service_supply_partner_account_id",
		"task.write_time",
		"task.bfb",
		"task.bfba",
		"task.aa",
		"task.k_user_field",
		"task.k_user_field_account_id",
		"task.zhimingxingtong_chuangyiren_task",
		"task.zhimingxingtong_chuangyiren_task_account_id",
		"task.zhimingxingtong_duohang",
		"task.cc",
		"task.zhimingxingtong_notefield",
		"task.bfbzd",
		"task.test_line_to",
		"task.leader_status_approve_time",
		"task.leader_status_retake_time",
		"task.san_qi_list",
		"task.last_review_submit_file",
		"task.last_submit_file",
		"task.last_version_id",
		"task.stest",
		"task.plan_days",
		"task.js_date",
		"task.pipeline_notice",
		"task.sanqibaifenbi",
		"task.check_field_start_time",
		"task.cgtw_record_packing_latest_time",
		"task.asset_level",
		"task.level_factor",
		"task.custom_sum_test",
		"task.dde",
		"task.from_retake_count",
		"task.trwjdmc",
		"task.supplier",
		"task.project",
		"task.miliaa",
		"task.cnnametask",
		"task.new_field_tag",
		"task.desreview_version",
		"task.shuzi",
		"task.jihq",
		"task.ddd",
		"task.long",
		"task.submit_path",
		"task.hjrth",
		"task.yhzd",
		"task.user",
		"task.user_account_id",
		"task.approve_time_list",
		"task.lbyhzd",
		"task.lbyhzd_account_id",
		"task.aniapprovename",
		"task.liebiaoz",
		"task.ziduanbiaoqian",
		"task.xiao_shu",
		"task.fu_xuan",
		"task.fbxreview_approve_time",
		"task.fbxreview_retake_time",
		"task.leader_status_time",
		"task.leader_status_artist",
		"task.fuku",
		"task.director_status_artist",
		"task.director_status_time"
	]
}
```
## /cgtw7.0/task/modules
```text
获取所有启用任务的模块
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | modules | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"shot",
		"test_module",
		"eps",
		"cross_module",
		"asset"
	]
}
```
## /cgtw7.0/task/fields_and_str
```text
获取所有字段标识和中文名
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | fields_and_str | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"sign": "asset.entity",
			"field_str": "资产名称"
		},
		{
			"sign": "asset.cn_name",
			"field_str": "中文名"
		},
		{
			"sign": "asset.image",
			"field_str": "信息缩略图"
		},
		{
			"sign": "asset.id",
			"field_str": "资产ID"
		},
		{
			"sign": "asset.assign_pipeline",
			"field_str": "已经分配阶段"
		},
		{
			"sign": "asset.create_time",
			"field_str": "创建时间"
		},
		{
			"sign": "asset.create_by",
			"field_str": "创建人员"
		},
		{
			"sign": "asset.last_update_time",
			"field_str": "最新编辑时间"
		},
		{
			"sign": "asset.last_update_by",
			"field_str": "最新编辑人员"
		},
		{
			"sign": "asset.link_shot",
			"field_str": "关联shot"
		},
		{
			"sign": "asset.pid_QVRRVDRO_VQEQ_QTUR_XAFB_XFAVRDUAXVWS",
			"field_str": "Design_status"
		},
		{
			"sign": "asset.pid_DCFXFRBQ_UQRS_QACB_OUOX_AWAWTSEAREEE",
			"field_str": "Mod_status"
		},
		{
			"sign": "asset.pid_OPEBARCQ_DAAR_WSOR_ACQX_WORWBUDDVSCO",
			"field_str": "Texture_status"
		},
		{
			"sign": "asset.pid_PVCSBDVX_SBFO_BWES_OTBW_DOOERPXPBOXQ",
			"field_str": "Rig_status"
		},
		{
			"sign": "asset.pipeline_template_name",
			"field_str": "阶段流程"
		},
		{
			"sign": "asset.link_asset_type",
			"field_str": "关联资产类型"
		},
		{
			"sign": "asset.lineedit",
			"field_str": "lineedit"
		},
		{
			"sign": "asset.textedit",
			"field_str": "textedit"
		},
		{
			"sign": "asset.int",
			"field_str": "int"
		},
		{
			"sign": "asset.float",
			"field_str": "float"
		},
		{
			"sign": "asset.list",
			"field_str": "list"
		},
		{
			"sign": "asset.mullist",
			"field_str": "mullist"
		},
		{
			"sign": "asset.tag",
			"field_str": "tag"
		},
		{
			"sign": "asset.media",
			"field_str": "media"
		},
		{
			"sign": "asset.link",
			"field_str": "link"
		},
		{
			"sign": "asset.datetime",
			"field_str": "datetime"
		},
		{
			"sign": "asset.checkbox",
			"field_str": "checkbox"
		},
		{
			"sign": "asset.pipeline_template_id",
			"field_str": "阶段模板ID"
		},
		{
			"sign": "asset.url",
			"field_str": "Url"
		},
		{
			"sign": "asset.url_id",
			"field_str": "Url ID"
		},
		{
			"sign": "asset.frame",
			"field_str": "帧数"
		},
		{
			"sign": "asset.zcfs",
			"field_str": "资产分属"
		},
		{
			"sign": "asset.zznd",
			"field_str": "制作难度"
		},
		{
			"sign": "asset.zcdj",
			"field_str": "资产单价"
		},
		{
			"sign": "asset.status",
			"field_str": "资产总状态"
		},
		{
			"sign": "asset.pack_time",
			"field_str": "打包时间"
		},
		{
			"sign": "asset.artist",
			"field_str": "信息制作者"
		},
		{
			"sign": "asset.account_id",
			"field_str": "信息制作者ID"
		},
		{
			"sign": "asset.sanqi_muliselect",
			"field_str": "三七多选集数"
		},
		{
			"sign": "asset.sanqi_tongji",
			"field_str": "三七集数统计"
		},
		{
			"sign": "asset.colorrgb",
			"field_str": "颜色RGB测试"
		},
		{
			"sign": "asset.rig_version",
			"field_str": "Rig 版本"
		},
		{
			"sign": "asset.sync_task_name",
			"field_str": "任务名称同步"
		},
		{
			"sign": "asset.asset_summary",
			"field_str": "资产汇总"
		},
		{
			"sign": "asset.link_eps",
			"field_str": "关联eps"
		},
		{
			"sign": "asset.geng_hao_san_link_eps",
			"field_str": "更号三-关联集数同步字段"
		},
		{
			"sign": "asset.ln_eps",
			"field_str": "关联集数"
		},
		{
			"sign": "asset.test_create",
			"field_str": "test_create"
		},
		{
			"sign": "asset_type.id",
			"field_str": "资产类型ID"
		},
		{
			"sign": "asset_type.entity",
			"field_str": "资产类型"
		},
		{
			"sign": "asset_type.url",
			"field_str": "Url"
		},
		{
			"sign": "asset_type.url_id",
			"field_str": "Url ID"
		},
		{
			"sign": "asset_type.artist",
			"field_str": "信息制作者"
		},
		{
			"sign": "asset_type.account_id",
			"field_str": "信息制作者ID"
		},
		{
			"sign": "pipeline.id",
			"field_str": "阶段ID"
		},
		{
			"sign": "pipeline.entity",
			"field_str": "阶段"
		},
		{
			"sign": "pipeline.abridge",
			"field_str": "阶段缩写"
		},
		{
			"sign": "pipeline.sort_id",
			"field_str": "阶段序号"
		},
		{
			"sign": "task.image",
			"field_str": "任务缩略图"
		},
		{
			"sign": "task.start_date",
			"field_str": "预计开始时间"
		},
		{
			"sign": "task.end_date",
			"field_str": "预计完成时间"
		},
		{
			"sign": "task.status",
			"field_str": "任务状态"
		},
		{
			"sign": "task.dead_line",
			"field_str": "规定完成时间"
		},
		{
			"sign": "task.finish_time",
			"field_str": "任务完成时间"
		},
		{
			"sign": "task.first_submit_time",
			"field_str": "首次提交时间"
		},
		{
			"sign": "task.entity",
			"field_str": "任务名称"
		},
		{
			"sign": "task.assign_time",
			"field_str": "分配时间"
		},
		{
			"sign": "task.id",
			"field_str": "任务ID"
		},
		{
			"sign": "task.pipeline",
			"field_str": "关联阶段"
		},
		{
			"sign": "task.last_submit_time",
			"field_str": "最后提交时间"
		},
		{
			"sign": "task.pipeline_id",
			"field_str": "任务阶段ID"
		},
		{
			"sign": "task.flow_finish_id",
			"field_str": "Flow Finish ID"
		},
		{
			"sign": "task.account_id",
			"field_str": "制作者ID"
		},
		{
			"sign": "task.artist",
			"field_str": "制作者"
		},
		{
			"sign": "task.leader_status",
			"field_str": "内部审核"
		},
		{
			"sign": "task.director_status",
			"field_str": "导演审核"
		},
		{
			"sign": "task.client_status",
			"field_str": "客户审核"
		},
		{
			"sign": "task.flow_id",
			"field_str": "流程ID"
		},
		{
			"sign": "task.pipeline_sort_id",
			"field_str": "阶段序号"
		},
		{
			"sign": "task.note_num",
			"field_str": "Note数量"
		},
		{
			"sign": "task.difficulty_level",
			"field_str": "难易度"
		},
		{
			"sign": "task.days",
			"field_str": "Days"
		},
		{
			"sign": "task.submit_count",
			"field_str": "提交次数"
		},
		{
			"sign": "task.assign_artist",
			"field_str": "分配人员"
		},
		{
			"sign": "task.flow_name",
			"field_str": "流程名"
		},
		{
			"sign": "task.url",
			"field_str": "Task Url"
		},
		{
			"sign": "task.total_use_time",
			"field_str": "总工时"
		},
		{
			"sign": "task.leader_status_retake_count",
			"field_str": "内部返修次数"
		},
		{
			"sign": "task.director_status_retake_count",
			"field_str": "导演返修次数"
		},
		{
			"sign": "task.client_status_retake_count",
			"field_str": "客户返修次数"
		},
		{
			"sign": "task.create_time",
			"field_str": "创建时间"
		},
		{
			"sign": "task.create_by",
			"field_str": "创建人员"
		},
		{
			"sign": "task.last_update_time",
			"field_str": "最新编辑时间"
		},
		{
			"sign": "task.url_id",
			"field_str": "Url ID"
		},
		{
			"sign": "task.last_update_by",
			"field_str": "最新编辑人员"
		},
		{
			"sign": "task.start_work_time",
			"field_str": "开始工作时间"
		},
		{
			"sign": "task.finish_diff",
			"field_str": "完成差值"
		},
		{
			"sign": "task.remaining_day",
			"field_str": "剩余天数"
		},
		{
			"sign": "task.overdue",
			"field_str": "超期天数"
		},
		{
			"sign": "task.qc_remaining_day",
			"field_str": "审核剩余天数"
		},
		{
			"sign": "task.factor",
			"field_str": "系数"
		},
		{
			"sign": "task.submit_diff",
			"field_str": "提交差值"
		},
		{
			"sign": "task.account",
			"field_str": "制作者账号"
		},
		{
			"sign": "task.module",
			"field_str": "模块"
		},
		{
			"sign": "task.last_retake_time",
			"field_str": "最新返修时间"
		},
		{
			"sign": "task.file_status",
			"field_str": "工程审核"
		},
		{
			"sign": "task.review_show_data",
			"field_str": "流程预览"
		},
		{
			"sign": "task.priority",
			"field_str": "优先级"
		},
		{
			"sign": "task.score",
			"field_str": "评分"
		},
		{
			"sign": "task.check_field",
			"field_str": "Check Field"
		},
		{
			"sign": "task.expected_time",
			"field_str": "预计工时"
		},
		{
			"sign": "task.product_director",
			"field_str": "制作总监"
		},
		{
			"sign": "task.check_field_sign",
			"field_str": "Check Field Sign"
		},
		{
			"sign": "task.version_data",
			"field_str": "版本数据"
		},
		{
			"sign": "task.status_note_id",
			"field_str": "Status note id"
		},
		{
			"sign": "task.tag",
			"field_str": "任务标签"
		},
		{
			"sign": "task.task_frame",
			"field_str": "任务帧数"
		},
		{
			"sign": "task.task_script",
			"field_str": "task_script"
		},
		{
			"sign": "task.pack_time",
			"field_str": "打包时间"
		},
		{
			"sign": "task.duration",
			"field_str": "duration"
		},
		{
			"sign": "task.frame",
			"field_str": "frame"
		},
		{
			"sign": "task.api_create",
			"field_str": "api_create"
		},
		{
			"sign": "task.text",
			"field_str": "单行文本"
		},
		{
			"sign": "task.image_test",
			"field_str": "缩略图-test"
		},
		{
			"sign": "task.gcnbsh",
			"field_str": "工程内部审核"
		},
		{
			"sign": "task.tgwjzzsh",
			"field_str": "通过文件最终审核"
		},
		{
			"sign": "task.last_review_version_id",
			"field_str": "last_review_version_id"
		},
		{
			"sign": "task.bbb",
			"field_str": "bbb"
		},
		{
			"sign": "task.leader_status_approve_count",
			"field_str": "内部审核通过次数"
		},
		{
			"sign": "task.field_tag",
			"field_str": "任务字段标签"
		},
		{
			"sign": "task.link_id",
			"field_str": "Link ID"
		},
		{
			"sign": "task.sub_pipeline_id",
			"field_str": "Sub Pipeline ID"
		},
		{
			"sign": "task.status_retake_count",
			"field_str": "任务状态返修次数"
		},
		{
			"sign": "task.version",
			"field_str": "version"
		},
		{
			"sign": "task.yilai",
			"field_str": "依赖任务"
		},
		{
			"sign": "task.ak_multi_list",
			"field_str": "任务多选列表"
		},
		{
			"sign": "task.ak_single_list",
			"field_str": "任务列表"
		},
		{
			"sign": "task.jindu",
			"field_str": "进度"
		},
		{
			"sign": "task.kaiguan",
			"field_str": "开关"
		},
		{
			"sign": "task.lianjie",
			"field_str": "链接"
		},
		{
			"sign": "task.director_status_approve_count",
			"field_str": "导演审核通过次数"
		},
		{
			"sign": "task.fbxreview",
			"field_str": "FBX审核"
		},
		{
			"sign": "task.tgareview",
			"field_str": "TGA审核"
		},
		{
			"sign": "task.reviewer",
			"field_str": "审核人"
		},
		{
			"sign": "task.reviewer_account_id",
			"field_str": "审核人ID"
		},
		{
			"sign": "task.testtime",
			"field_str": "时间测试"
		},
		{
			"sign": "task.zhimingxingtong_taskartist",
			"field_str": "智明星通任务制作者"
		},
		{
			"sign": "task.zhimingxingtong_taskartist_account_id",
			"field_str": "智明星通任务制作者 ID"
		},
		{
			"sign": "task.status_note",
			"field_str": "Status note"
		},
		{
			"sign": "task.yhtest",
			"field_str": "用户字段测试"
		},
		{
			"sign": "task.yhtest_account_id",
			"field_str": "用户字段测试 ID"
		},
		{
			"sign": "task.service_supply_partner",
			"field_str": "承接方"
		},
		{
			"sign": "task.service_supply_partner_account_id",
			"field_str": "承接方 ID"
		},
		{
			"sign": "task.write_time",
			"field_str": "承接方填写时间"
		},
		{
			"sign": "task.bfb",
			"field_str": "百分比"
		},
		{
			"sign": "task.bfba",
			"field_str": "百分比a"
		},
		{
			"sign": "task.aa",
			"field_str": "1111111"
		},
		{
			"sign": "task.k_user_field",
			"field_str": "K_用户字段"
		},
		{
			"sign": "task.k_user_field_account_id",
			"field_str": "K_用户字段 ID"
		},
		{
			"sign": "task.zhimingxingtong_chuangyiren_task",
			"field_str": "智明星通-任务创意人"
		},
		{
			"sign": "task.zhimingxingtong_chuangyiren_task_account_id",
			"field_str": "智明星通-任务创意人 ID"
		},
		{
			"sign": "task.zhimingxingtong_duohang",
			"field_str": "智明星通-多行文本"
		},
		{
			"sign": "task.cc",
			"field_str": "富文本"
		},
		{
			"sign": "task.zhimingxingtong_notefield",
			"field_str": "智明星通-同步note到任务字段"
		},
		{
			"sign": "task.bfbzd",
			"field_str": "百分比测试"
		},
		{
			"sign": "task.test_line_to",
			"field_str": "测试但行转富文本"
		},
		{
			"sign": "task.leader_status_approve_time",
			"field_str": "内部最新通过时间"
		},
		{
			"sign": "task.leader_status_retake_time",
			"field_str": "内部最新返修时间"
		},
		{
			"sign": "task.san_qi_list",
			"field_str": "三七-单选列表"
		},
		{
			"sign": "task.last_review_submit_file",
			"field_str": "最后效果提交文件名"
		},
		{
			"sign": "task.last_submit_file",
			"field_str": "最后版本提交文件名"
		},
		{
			"sign": "task.last_version_id",
			"field_str": "last_version_id"
		},
		{
			"sign": "task.stest",
			"field_str": "状态"
		},
		{
			"sign": "task.plan_days",
			"field_str": "预计天数"
		},
		{
			"sign": "task.js_date",
			"field_str": "预计审核完成时间"
		},
		{
			"sign": "task.pipeline_notice",
			"field_str": "Pipeline notice"
		},
		{
			"sign": "task.sanqibaifenbi",
			"field_str": "三七百分比"
		},
		{
			"sign": "task.check_field_start_time",
			"field_str": "Check Field Start Time"
		},
		{
			"sign": "task.cgtw_record_packing_latest_time",
			"field_str": "最新打包时间"
		},
		{
			"sign": "task.asset_level",
			"field_str": "任务级别"
		},
		{
			"sign": "task.level_factor",
			"field_str": "任务等级系数"
		},
		{
			"sign": "task.custom_sum_test",
			"field_str": "自定义求和测试"
		},
		{
			"sign": "task.dde",
			"field_str": "dde"
		},
		{
			"sign": "task.from_retake_count",
			"field_str": "from_retake_count"
		},
		{
			"sign": "task.trwjdmc",
			"field_str": "Check框拖入文件的名称"
		},
		{
			"sign": "task.supplier",
			"field_str": "米粒supplier"
		},
		{
			"sign": "task.project",
			"field_str": "米粒-project"
		},
		{
			"sign": "task.miliaa",
			"field_str": "米粒 1"
		},
		{
			"sign": "task.cnnametask",
			"field_str": "中文名称（任务）"
		},
		{
			"sign": "task.new_field_tag",
			"field_str": "new_field_tag"
		},
		{
			"sign": "task.desreview_version",
			"field_str": "测试看看能不能看到提交版本号"
		},
		{
			"sign": "task.shuzi",
			"field_str": "数字"
		},
		{
			"sign": "task.jihq",
			"field_str": "41424"
		},
		{
			"sign": "task.ddd",
			"field_str": "12345"
		},
		{
			"sign": "task.long",
			"field_str": "整数"
		},
		{
			"sign": "task.submit_path",
			"field_str": "提交路径"
		},
		{
			"sign": "task.hjrth",
			"field_str": "愤怒手机电脑废旧回收呢"
		},
		{
			"sign": "task.yhzd",
			"field_str": "用户字段"
		},
		{
			"sign": "task.user",
			"field_str": "11用户"
		},
		{
			"sign": "task.user_account_id",
			"field_str": "11用户 ID"
		},
		{
			"sign": "task.approve_time_list",
			"field_str": "通过时间"
		},
		{
			"sign": "task.lbyhzd",
			"field_str": "(lb)用户字段"
		},
		{
			"sign": "task.lbyhzd_account_id",
			"field_str": "(lb)用户字段 ID"
		},
		{
			"sign": "task.aniapprovename",
			"field_str": "Ani通过文件名称"
		},
		{
			"sign": "task.liebiaoz",
			"field_str": "列表z"
		},
		{
			"sign": "task.ziduanbiaoqian",
			"field_str": "字段标签z"
		},
		{
			"sign": "task.xiao_shu",
			"field_str": "小数"
		},
		{
			"sign": "task.fu_xuan",
			"field_str": "复选"
		},
		{
			"sign": "task.fbxreview_approve_time",
			"field_str": "FBX审核通过时间"
		},
		{
			"sign": "task.fbxreview_retake_time",
			"field_str": "FBX审核返修时间"
		},
		{
			"sign": "task.leader_status_time",
			"field_str": "内部审核时间"
		},
		{
			"sign": "task.leader_status_artist",
			"field_str": "内部审核人"
		},
		{
			"sign": "task.fuku",
			"field_str": "(lb)富裕的文本"
		},
		{
			"sign": "task.director_status_artist",
			"field_str": "导演审核人"
		},
		{
			"sign": "task.director_status_time",
			"field_str": "导演审核时间"
		}
	]
}
```
## /cgtw7.0/task/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[start_num] | - | String | 否 | 开始条数,默认为""
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("task_asset_id", response.json.data[0]);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"EA6D6829-FD25-2D54-2BF1-65919A910C3E",
		"D128B19C-8E94-7830-7B72-AE03EBDF54F8",
		"1A83C8F8-6E88-E730-DC35-E743B51E6A0D",
		"82771A2B-D425-1D44-AC00-A8EF96EEF1C1",
		"F2AD9A35-F759-8D49-0F2E-ACFC722423F1",
		"CCDB4779-3E45-DD92-F8C7-E0AAE1B5168F",
		"4F6E1FB5-EF0A-AD6D-88AF-527A6137E481",
		"477D1CF0-96F6-3973-8E84-850757C40FB7",
		"553D937B-66FA-D0BB-555D-832DEB87263F",
		"B303BE40-7D85-2244-7225-E4CF44172C2F",
		"6403B693-B0E3-A4F4-315B-492FD0D03D27",
		"116FD794-A236-A697-C54C-1F75B5475E60",
		"FCDB2F54-66D1-866B-E9FE-D3E7625DAD88"
	]
}
```
## /cgtw7.0/task/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[sign_array][] | asset.entity | Array | 是 | 字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[start_num] | - | String | 否 | 开始条数,默认为""
data[order_sign_array] | - | Array | 否 | 顺序的字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"asset.entity": "cat001",
			"id": "EA6D6829-FD25-2D54-2BF1-65919A910C3E"
		},
		{
			"asset.entity": "cat001",
			"id": "D128B19C-8E94-7830-7B72-AE03EBDF54F8"
		},
		{
			"asset.entity": "cat002",
			"id": "1A83C8F8-6E88-E730-DC35-E743B51E6A0D"
		},
		{
			"asset.entity": "cat002",
			"id": "82771A2B-D425-1D44-AC00-A8EF96EEF1C1"
		},
		{
			"asset.entity": "cat002",
			"id": "F2AD9A35-F759-8D49-0F2E-ACFC722423F1"
		},
		{
			"asset.entity": "cat003",
			"id": "CCDB4779-3E45-DD92-F8C7-E0AAE1B5168F"
		},
		{
			"asset.entity": "cat003",
			"id": "4F6E1FB5-EF0A-AD6D-88AF-527A6137E481"
		},
		{
			"asset.entity": "cat002",
			"id": "477D1CF0-96F6-3973-8E84-850757C40FB7"
		},
		{
			"asset.entity": "cat003",
			"id": "553D937B-66FA-D0BB-555D-832DEB87263F"
		},
		{
			"asset.entity": "cat001",
			"id": "B303BE40-7D85-2244-7225-E4CF44172C2F"
		},
		{
			"asset.entity": "cat003",
			"id": "6403B693-B0E3-A4F4-315B-492FD0D03D27"
		},
		{
			"asset.entity": "cat001",
			"id": "116FD794-A236-A697-C54C-1F75B5475E60"
		},
		{
			"asset.entity": "cat001",
			"id": "FCDB2F54-66D1-866B-E9FE-D3E7625DAD88"
		}
	]
}
```
## /cgtw7.0/task/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[sign_array][] | asset.entity | String | 是 | 字段标识列表
data[id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | String | 是 | ID列表
data[order_sign_array] | - | String | 否 | 顺序的字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"asset.entity": "cat001",
			"id": "EA6D6829-FD25-2D54-2BF1-65919A910C3E"
		}
	]
}
```
## /cgtw7.0/task/get_dir
```text
用目录标识列表获取对应的目录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | get_dir | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | Array | 是 | ID列表
data[sign_array][] | asset_source | Array | 是 | 目录标识列表
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "EA6D6829-FD25-2D54-2BF1-65919A910C3E",
			"asset_source": "a:/xiaoying/Asset/Chars/cat001/source"
		}
	]
}
```
## /cgtw7.0/task/get_field_and_dir
```text
用目录标识列表和字段标识列表获取对应的目录和字段列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | get_field_and_dir | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | String | 是 | ID列表
data[folder_sign_array][] | asset_source | Array | 是 | 目录标识列表
data[os] | win | String | 是 | 系统平台
data[field_sign_array][] | asset.entity | Array | 是 | 字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"asset.entity": "cat001",
			"id": "EA6D6829-FD25-2D54-2BF1-65919A910C3E",
			"asset_source": "a:/xiaoying/Asset/Chars/cat001/source"
		}
	]
}
```
## /cgtw7.0/task/get_makedirs
```text
获取创建目录的列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | get_makedirs | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | Array | 是 | ID列表
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"z:/11",
		"a:/xiaoying/Asset/Chars/cat001/Design/check",
		"a:/xiaoying/Asset/Chars/cat001/Design/work",
		"a:/xiaoying/Asset/Chars/cat001/Design/approve",
		"a:/xiaoying/Asset/Chars/cat001/Design/file_ver",
		"a:/xiaoying/Asset/Chars/cat001/Design/same_ver",
		"a:/xiaoying/Asset/Chars/cat001/Design",
		"a:/xiaoying/Asset/Chars/cat001/Mod/check",
		"a:/xiaoying/Asset/Chars/cat001/Mod/work",
		"a:/xiaoying/Asset/Chars/cat001/Mod/approve",
		"a:/xiaoying/Asset/Chars/cat001/Texture/check",
		"a:/xiaoying/Asset/Chars/cat001/Texture/work",
		"a:/xiaoying/Asset/Chars/cat001/Texture/approve",
		"a:/xiaoying/Asset/Chars/cat001/Texture/Texture",
		"a:/xiaoying/Asset/Chars/cat001/Rig/check",
		"a:/xiaoying/Asset/Chars/cat001/Rig/work",
		"a:/xiaoying/Asset/Chars/cat001/Rig/approve",
		"a:/xiaoying/Asset/Chars/cat001/Rig/file_version",
		"a:/xiaoying/Asset/Chars/cat001/source",
		"a:/xiaoying/Shot/Layout",
		"a:/xiaoying/Shot/Animation",
		"a:/xiaoying/Shot/Lighting",
		"a:/xiaoying/Shot/VFX",
		"a:/xiaoying/Shot/Comp",
		"a:/xiaoying/Shot/Source",
		"a:/xiaoying/Shot/Mod",
		"a:/xiaoying/Audio",
		"a:/xiaoying/Audio/2023-02-27",
		"a:/xiaoying/Animatic",
		"a:/xiaoying/Storyboard",
		"a:/xiaoying/Reference",
		"a:/xiaoying/20230227",
		"a:/ref_1",
		"a:/source",
		"a:/file_ver"
	]
}
```
## /cgtw7.0/task/get_submit_filebox_sign
```text
获取提交流程的文件框标识列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | get_submit_filebox_sign | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | String | 是 | ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"review"
	]
}
```
## /cgtw7.0/task/get_sign_filebox
```text
根据文件框标识获取文件框设置信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | get_sign_filebox | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[id_array][] | C976B7DC-7118-AE88-8868-53FF785922C3 | Array | 是 | ID列表
data[os] | win | String | 是 | 系统平台
data[filebox_sign] | design_file_ver | String | 是 | 文件框标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
task_asset_id = request.data["data[id_array][]"]
apt.globals.set("task_asset_id", task_asset_id);
apt.globals.set("task_asset_filebox_id", response.json.data[task_asset_id]['#id']);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"EA6D6829-FD25-2D54-2BF1-65919A910C3E": {
			"ref_task_id_list": [],
			"ref_pipeline_id": "",
			"#id": "22496EFD-0FD1-8B03-2098-45921237C925",
			"path": "a:/xiaoying/Asset/Chars/cat001/Mod/check",
			"server": "a:/",
			"server_id": "271E10CC-A6BA-F359-073F-FBC355198353",
			"pipeline_id": "DCF9F3B2-6234-2ACB-0609-A8A854EA3EEE",
			"title": "审核文件",
			"sign": "review",
			"color": "#FF9E9E",
			"rule": [
				"xiaoying_cat001_Mod_xiaoying_*_v{ver}.*",
				"xiaoying_cat001_Mod_xiaoying_*_v{ver}"
			],
			"rule_view": [
				"xiaoying_cat001_Mod_xiaoying_*_v{ver}.*",
				"xiaoying_cat001_Mod_xiaoying_*_v{ver}"
			],
			"show_type": "Files and Folders",
			"is_drag_in": "Y",
			"is_ref": "",
			"ref_id": "",
			"is_approve_version": "",
			"is_upload_online": "N",
			"online_upload_group": "all",
			"convert_type": [],
			"is_version": "Y",
			"version_type": "file",
			"version_length": "3",
			"is_upgrade_version": "N",
			"is_follow": "N",
			"follow_sign": "",
			"submit_type": "review",
			"drag_in": [
				{
					"plugin_id": "check_rule",
					"disable_rename": "Y"
				}
			],
			"is_move_old_to_history": "N",
			"is_move_same_to_history": "N",
			"is_in_history_add_version": "N",
			"is_in_history_add_datetime": "N",
			"is_cover_disable": "N",
			"is_msg_to_first_qc": "N",
			"show_group_id": "all",
			"max_version": "001",
			"max_version_id": "D0406F20-7C3C-4502-64EC-028D74A566E2",
			"version_list": [
				"001"
			],
			"version_id_list": {
				"D0406F20-7C3C-4502-64EC-028D74A566E2": "001"
			},
			"last_max_version": "001",
			"last_max_version_id": "D0406F20-7C3C-4502-64EC-028D74A566E2",
			"last_link_id": "EA6D6829-FD25-2D54-2BF1-65919A910C3E",
			"follow_version": "",
			"follow_title": "",
			"is_submit": "Y",
			"reviewer_account_id": ""
		}
	}
}
```
## /cgtw7.0/task/get_review_file
```text
获取可预览最后版本文件,用于视频串播
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | get_review_file | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[link_id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | Array | 是 | ID列表
data[os] | win | String | 是 | 系统平台
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "EA6D6829-FD25-2D54-2BF1-65919A910C3E",
			"path": [
				"a:/xiaoying/Asset/Chars/cat001/Mod/check/xiaoying_cat001_Mod_xiaoying_a_v001.mov"
			],
			"file_path": [
				"a:/xiaoying/Asset/Chars/cat001/Mod/check/xiaoying_cat001_Mod_xiaoying_a_v001.mov"
			],
			"dir": "a:/xiaoying/Asset/Chars/cat001/Mod/check"
		}
	]
}
```
## /cgtw7.0/task/get_version_file
```text
获取文件框最后版本文件
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | get_version_file | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[link_id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | Array | 是 | ID列表
data[os] | win | String | 是 | 系统平台
data[module] | asset | String | 是 | 模块标识
data[filebox_sign] | review | String | 是 | 文件框标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "EA6D6829-FD25-2D54-2BF1-65919A910C3E",
			"path": [
				"a:/xiaoying/Asset/Chars/cat001/Mod/check/xiaoying_cat001_Mod_xiaoying_a_v001.mov"
			],
			"file_path": [
				"a:/xiaoying/Asset/Chars/cat001/Mod/check/xiaoying_cat001_Mod_xiaoying_a_v001.mov"
			],
			"dir": "a:/xiaoying/Asset/Chars/cat001/Mod/check"
		}
	]
}
```
## /cgtw7.0/task/set
```text
更新记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | Array | 是 | ID列表
data[sign_data_array][task.bfb] | 11 | Array | 是 | 更新数据 (dict), 格式:{"字段标识" : "值", "字段标识" : "值" }
data[exec_event_filter] | - | Boolean | 否 | 执行事件过滤器
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/task/delete
```text
删除记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | delete | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[id_array][] | 849D6CD8-7137-B37B-492A-91C3726A0717 | Array | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/task/create
```text
创建记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[join_id] | EC66ABC4-9C21-BD9C-12C5-52C8B3EC41D0 | String | 是 | 信息表的ID
data[flow_id] | 426CF0EA-97B6-CABD-8E46-88B44616AE6A | String | 是 | 流程ID
data[task_name] | Mod | String | 是 | 任务名称
data[pipeline_id] | DCF9F3B2-6234-2ACB-0609-A8A854EA3EEE | String | 是 | 阶段ID
data[exec_event_filter] | - | Boolean | 否 | 执行事件过滤器
data[sign_data_array] | - | Array | 否 | 更新的数据(dict), 格式:{"字段标识" : "值", "字段标识" : "值" }
data[pipeline_template_id] | - | String | 否 | 阶段流程ID
data[sub_pipeline_id] | - | String | 否 | 子阶段ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "1E97A0FD-0A13-7D91-CC0E-D7239C87E86A"
}
```
## /cgtw7.0/task/count
```text
统计记录条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "14"
}
```
## /cgtw7.0/task/distinct
```text
获取去重后的记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | distinct | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[distinct_sign] | asset_type.entity | String | 是 | 字段标识
data[order_sign_array] | - | Array | 否 | 顺序的字段标识列表
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"Chars"
	]
}
```
## /cgtw7.0/task/assign
```text
分配任务给制作人员
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | assign | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[assign_account_id] | {{account_id}} | String | 是 | 制作者ID
data[start_date] | 2022-02-02 | String | 是 | 预计开始日期 (str/unicode), 格式:2018-01-01, 默认为""
data[end_date] | 2022-02-02 | String | 是 | 预计完成日期 (str/unicode), 格式:2018-01-01, 默认为""
data[task_id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | Array | 是 | ID列表
data[exec_event_filter] | - | Boolean | 否 | 执行事件过滤器
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/task/update_flow
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | update_flow | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[task_id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | Array | 是 | ID列表
data[field_sign] | task.leader_status | String | 是 | 字段标识
data[dom_array][] | "" | Array | 是 | 内容
data[status] | Approve | String | 是 | 状态
data[retake_pipeline_id_array] | - | Array | 否 | 返修阶段ID列表
data[tag] | - | String | 否 | 标签
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/task/update_task_status
```text
修改任务状态列
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | update_task_status | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[dom_array][] | "" | Array | 是 | 内容
data[status] | Approve | String | 是 | 状态
data[task_id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | Array | 是 | id_list
data[retake_pipeline_id_array] | - | String | 否 | 返修阶段ID列表
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/task/group_count
```text
按字段标识进行分组统计条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | group_count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[sign_array][] | asset.entity | Array | 是 | 字段标识列表
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"count": 5,
			"asset.entity": "cat001"
		},
		{
			"count": 4,
			"asset.entity": "cat002"
		},
		{
			"count": 4,
			"asset.entity": "cat003"
		},
		{
			"count": 1,
			"asset.entity": "test_create"
		}
	]
}
```
## /cgtw7.0/task/send_msg
```text
给指定用户发送任务相关消息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | task | String | 是 | 控制器
data[method] | send_msg | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[account_id_array] | {{account_id}} | String | 是 | 账号ID列表
data[task_id] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | String | 是 | Id
data[content][] | - | String | 是 | 发送的内容
data[important] | - | String | 否 | 是否强提醒
data[module] | asset | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/etask
```text
简易版接口
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/etask/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"etask.id",
		"etask.image",
		"etask.start_date",
		"etask.end_date",
		"etask.status",
		"etask.dead_line",
		"etask.first_submit_time",
		"etask.entity",
		"etask.assign_time",
		"etask.last_submit_time",
		"etask.flow_finish_id",
		"etask.account_id",
		"etask.artist",
		"etask.note_num",
		"etask.difficulty_level",
		"etask.submit_count",
		"etask.assign_artist",
		"etask.create_time",
		"etask.last_update_time",
		"etask.create_by",
		"etask.last_update_by",
		"etask.start_work_time",
		"etask.priority",
		"etask.total_use_time",
		"etask.remaining_day",
		"etask.pipeline_template_name",
		"etask.url",
		"etask.leader_status",
		"etask.director_status",
		"etask.client_status",
		"etask.pipeline_id",
		"etask.flow_id",
		"etask.flow_name",
		"etask.url_id",
		"etask.check_field_sign",
		"etask.version_data",
		"etask.review_show_data",
		"etask.overdue",
		"etask.frame",
		"etask.status_note_id",
		"etask.link_id",
		"etask.finish_time",
		"etask.pipeline_template_id",
		"etask.start_frame",
		"etask.end_frame",
		"etask.task_script",
		"etask.start_time_code",
		"etask.end_time_code",
		"etask.last_image",
		"etask.image_hash",
		"etask.source_name",
		"etask.pack_time",
		"etask.source",
		"etask.resolution",
		"etask.fps",
		"etask.duration",
		"etask.gcshnew",
		"etask.sub_pipeline_id",
		"etask.pici",
		"etask.numcol",
		"etask.link_etype",
		"etask.check_field",
		"etask.reviewer",
		"etask.reviewer_account_id",
		"etask.archive",
		"etask.status_note",
		"etask.last_review_submit_file",
		"etask.last_submit_file",
		"etask.pipeline_notice",
		"etask.check_field_start_time",
		"etask.single",
		"etask.file_status",
		"etask.tag",
		"etask.list",
		"etask.mulselect",
		"etask.field_tag",
		"etask.leader_status_artist",
		"etask.leader_status_time",
		"etype.entity",
		"etype.id",
		"etype.sign",
		"pipeline.entity",
		"pipeline.id",
		"pipeline.sort_id",
		"pipeline.abridge"
	]
}
```
## /cgtw7.0/etask/fields_and_str
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | fields_and_str | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"sign": "etask.id",
			"field_str": "任务ID"
		},
		{
			"sign": "etask.image",
			"field_str": "缩略图"
		},
		{
			"sign": "etask.start_date",
			"field_str": "预计开始时间"
		},
		{
			"sign": "etask.end_date",
			"field_str": "预计完成时间"
		},
		{
			"sign": "etask.status",
			"field_str": "任务状态"
		},
		{
			"sign": "etask.dead_line",
			"field_str": "规定完成时间"
		},
		{
			"sign": "etask.first_submit_time",
			"field_str": "首次提交时间"
		},
		{
			"sign": "etask.entity",
			"field_str": "任务名称"
		},
		{
			"sign": "etask.assign_time",
			"field_str": "分配时间"
		},
		{
			"sign": "etask.last_submit_time",
			"field_str": "最后提交时间"
		},
		{
			"sign": "etask.flow_finish_id",
			"field_str": "Flow Finish ID"
		},
		{
			"sign": "etask.account_id",
			"field_str": "制作者ID"
		},
		{
			"sign": "etask.artist",
			"field_str": "制作者"
		},
		{
			"sign": "etask.note_num",
			"field_str": "Note数量"
		},
		{
			"sign": "etask.difficulty_level",
			"field_str": "难易度"
		},
		{
			"sign": "etask.submit_count",
			"field_str": "提交次数"
		},
		{
			"sign": "etask.assign_artist",
			"field_str": "分配人员"
		},
		{
			"sign": "etask.create_time",
			"field_str": "创建时间"
		},
		{
			"sign": "etask.last_update_time",
			"field_str": "最新编辑时间"
		},
		{
			"sign": "etask.create_by",
			"field_str": "创建人员"
		},
		{
			"sign": "etask.last_update_by",
			"field_str": "最新编辑人员"
		},
		{
			"sign": "etask.start_work_time",
			"field_str": "开始工作时间"
		},
		{
			"sign": "etask.priority",
			"field_str": "优先级"
		},
		{
			"sign": "etask.total_use_time",
			"field_str": "总工时"
		},
		{
			"sign": "etask.remaining_day",
			"field_str": "剩余天数"
		},
		{
			"sign": "etask.pipeline_template_name",
			"field_str": "阶段流程"
		},
		{
			"sign": "etask.url",
			"field_str": "Url"
		},
		{
			"sign": "etask.leader_status",
			"field_str": "组长状态"
		},
		{
			"sign": "etask.director_status",
			"field_str": "导演状态"
		},
		{
			"sign": "etask.client_status",
			"field_str": "客户状态"
		},
		{
			"sign": "etask.pipeline_id",
			"field_str": "任务阶段ID"
		},
		{
			"sign": "etask.flow_id",
			"field_str": "流程ID"
		},
		{
			"sign": "etask.flow_name",
			"field_str": "流程名"
		},
		{
			"sign": "etask.url_id",
			"field_str": "Url ID"
		},
		{
			"sign": "etask.check_field_sign",
			"field_str": "Check Field Sign"
		},
		{
			"sign": "etask.version_data",
			"field_str": "版本数据"
		},
		{
			"sign": "etask.overdue",
			"field_str": "超期天数"
		},
		{
			"sign": "etask.review_show_data",
			"field_str": "流程预览"
		},
		{
			"sign": "etask.frame",
			"field_str": "帧数"
		},
		{
			"sign": "etask.status_note_id",
			"field_str": "Status note id"
		},
		{
			"sign": "etask.link_id",
			"field_str": "Link ID"
		},
		{
			"sign": "etask.finish_time",
			"field_str": "任务完成时间"
		},
		{
			"sign": "etask.pipeline_template_id",
			"field_str": "Pipeline Template ID"
		},
		{
			"sign": "etask.start_frame",
			"field_str": "起始帧"
		},
		{
			"sign": "etask.end_frame",
			"field_str": "结束帧"
		},
		{
			"sign": "etask.start_time_code",
			"field_str": "开始时间码"
		},
		{
			"sign": "etask.end_time_code",
			"field_str": "结束时间码"
		},
		{
			"sign": "etask.last_image",
			"field_str": "结束帧图片"
		},
		{
			"sign": "etask.image_hash",
			"field_str": "图片指纹"
		},
		{
			"sign": "etask.source_name",
			"field_str": "素材名"
		},
		{
			"sign": "etask.pack_time",
			"field_str": "打包时间"
		},
		{
			"sign": "etask.source",
			"field_str": "素材路径"
		},
		{
			"sign": "etask.resolution",
			"field_str": "分辨率"
		},
		{
			"sign": "etask.fps",
			"field_str": "帧率"
		},
		{
			"sign": "etask.duration",
			"field_str": "duration"
		},
		{
			"sign": "etask.gcshnew",
			"field_str": "新工程审核"
		},
		{
			"sign": "etask.sub_pipeline_id",
			"field_str": "Sub Pipeline ID"
		},
		{
			"sign": "etask.pici",
			"field_str": "批次"
		},
		{
			"sign": "etask.numcol",
			"field_str": "数字列"
		},
		{
			"sign": "etask.link_etype",
			"field_str": "关联类型"
		},
		{
			"sign": "etask.check_field",
			"field_str": "Check Field"
		},
		{
			"sign": "etask.reviewer",
			"field_str": "审核人"
		},
		{
			"sign": "etask.reviewer_account_id",
			"field_str": "审核人ID"
		},
		{
			"sign": "etask.archive",
			"field_str": "是否归档"
		},
		{
			"sign": "etask.status_note",
			"field_str": "Status note"
		},
		{
			"sign": "etask.last_review_submit_file",
			"field_str": "最后效果提交文件名"
		},
		{
			"sign": "etask.last_submit_file",
			"field_str": "最后版本提交文件名"
		},
		{
			"sign": "etask.pipeline_notice",
			"field_str": "Pipeline notice"
		},
		{
			"sign": "etask.check_field_start_time",
			"field_str": "Check Field Start Time"
		},
		{
			"sign": "etask.single",
			"field_str": "单选列表"
		},
		{
			"sign": "etask.file_status",
			"field_str": "工程审核"
		},
		{
			"sign": "etask.tag",
			"field_str": "标签"
		},
		{
			"sign": "etask.list",
			"field_str": "列表"
		},
		{
			"sign": "etask.mulselect",
			"field_str": "多选列表"
		},
		{
			"sign": "etask.field_tag",
			"field_str": "字段标签"
		},
		{
			"sign": "etask.leader_status_artist",
			"field_str": "内部审核人"
		},
		{
			"sign": "etask.leader_status_time",
			"field_str": "内部审核时间"
		},
		{
			"sign": "etype.entity",
			"field_str": "类型"
		},
		{
			"sign": "etype.id",
			"field_str": "ID"
		},
		{
			"sign": "etype.sign",
			"field_str": "类型标识"
		},
		{
			"sign": "pipeline.entity",
			"field_str": "阶段"
		},
		{
			"sign": "pipeline.id",
			"field_str": "PipelineID"
		},
		{
			"sign": "pipeline.sort_id",
			"field_str": "阶段序号"
		},
		{
			"sign": "pipeline.abridge",
			"field_str": "阶段缩写"
		}
	]
}
```
## /cgtw7.0/etask/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[start_num] | - | String | 否 | 开始条数,默认为""
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"C750174B-15BF-1FB5-0829-000B12D0A484",
		"EA6D6829-FD25-2D54-2BF1-65919A910C3E",
		"8553FBDC-1022-E544-7293-DD28C6CEA8FC",
		"B006E913-4B83-C465-D2A5-6A38D087F243",
		"16D442F6-A17D-C445-2E6C-14C852053DD1",
		"849D6CD8-7D37-B37B-492A-91C3726A0717"
	]
}
```
## /cgtw7.0/etask/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[sign_filter_array] | - | Array | 是 | 过滤语句列表
data[sign_array][] | etask.entity | Array | 是 | 字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[order_sign_array] | - | Array | 否 | 顺序的字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"etask.entity": "sc023562",
			"id": "397220BB-3F5F-8ED4-E876-71B6189880F0"
		},
		{
			"etask.entity": "sc015763",
			"id": "3E8FDC2B-DCED-063C-F8B7-0D14975B6DE8"
		},
		{
			"etask.entity": "sc015764",
			"id": "303EBE3E-F9BF-CEB6-97F7-74EE09AE1AD6"
		},
		{
			"etask.entity": "sc015765",
			"id": "038BF1A2-0432-EF4F-FF4E-905B6734D55C"
		},
		{
			"etask.entity": "sc015766",
			"id": "B5C5E1A8-8811-315E-6B77-2FA263D5BC63"
		},
		{
			"etask.entity": "sc015768",
			"id": "543C611B-D605-0D49-3D85-E19DDCD93E9C"
		},
		{
			"etask.entity": "sc015769",
			"id": "49C48BC5-93A7-428A-FA7C-3CE8305A671A"
		},
		{
			"etask.entity": "sc015770",
			"id": "3F02882A-7754-0CA3-F2A5-9997F668AA90"
		},
		{
			"etask.entity": "sc015771",
			"id": "C0673425-230D-4FB9-BD21-25F7E341C66B"
		},
		{
			"etask.entity": "sc015773",
			"id": "31969EBA-C2E6-D5CC-6640-E10762123D00"
		},
		{
			"etask.entity": "sc015774",
			"id": "4EE1CC36-3348-1CC1-F4F7-3A0FCE64CFD9"
		},
		{
			"etask.entity": "sc015775",
			"id": "6AAF7B29-71AF-F218-ADBD-FAEDDB030A3F"
		},
		{
			"etask.entity": "sc015776",
			"id": "95C54B59-A4DB-0D40-A6F6-00412B72AED1"
		},
		{
			"etask.entity": "sc015778",
			"id": "26394E24-4B8C-B5D5-DCB6-A93F73485407"
		},
		{
			"etask.entity": "sc015779",
			"id": "C95DFE0F-7D59-4C46-5D62-724752FB41A4"
		},
		{
			"etask.entity": "sc015780",
			"id": "42D83D06-D433-3328-8366-6E0BD6FE9D3A"
		},
		{
			"etask.entity": "sc015781",
			"id": "208D2A8E-60F9-AA64-C76C-6BE8759696AA"
		},
		{
			"etask.entity": "sc015783",
			"id": "EB6A0294-7D01-CD3C-AFDA-D6D3421687C2"
		},
		{
			"etask.entity": "sc023563",
			"id": "239BEB92-A733-26ED-5A27-2F965704DC2C"
		},
		{
			"etask.entity": "sc015785",
			"id": "575B4C19-7AEB-31A9-9D6B-1D6E0BD2899C"
		},
		{
			"etask.entity": "sc015786",
			"id": "90FF2AFE-E1A6-21C8-12D7-3993CF532BA1"
		},
		{
			"etask.entity": "sc015787",
			"id": "9583AEFB-372C-7546-EACC-8384B79B83DA"
		},
		{
			"etask.entity": "sc015788",
			"id": "6A4E35CC-EE21-F9B6-B84C-20DB1E1B7A1C"
		},
		{
			"etask.entity": "sc015790",
			"id": "72A48CCD-5C37-7053-A490-64BC4726F22E"
		},
		{
			"etask.entity": "sc015791",
			"id": "6455169A-8EF6-700E-0F5E-D3C363F59BE7"
		},
		{
			"etask.entity": "sc015792",
			"id": "0ACFDFB4-60B8-7D32-330C-89600CDA5AC8"
		},
		{
			"etask.entity": "sc015793",
			"id": "29199671-AB34-FA82-CD71-38FBC0E82CB6"
		},
		{
			"etask.entity": "sc015795",
			"id": "543F27DB-CED4-CF5F-73C5-FD21CD95DADC"
		},
		{
			"etask.entity": "sc015796",
			"id": "63117674-A6A9-F3ED-6D98-D2D9AA5013C6"
		},
		{
			"etask.entity": "sc015797",
			"id": "4F5EE5A1-5A71-0D66-EC28-08399453B252"
		},
		{
			"etask.entity": "sc015798",
			"id": "01A645EC-1324-D572-7291-1D53A571EC48"
		},
		{
			"etask.entity": "sc015800",
			"id": "BE028668-B805-BCD8-DF86-956F9EA2C0C1"
		},
		{
			"etask.entity": "sc015801",
			"id": "D6772E12-FD45-0F52-33EF-2704570C359E"
		},
		{
			"etask.entity": "sc015802",
			"id": "22E0A611-175F-7B2C-0691-15D87368B131"
		},
		{
			"etask.entity": "sc015803",
			"id": "C1A25ED4-7615-0D39-975F-BBE11882695F"
		},
		{
			"etask.entity": "sc015805",
			"id": "AC43E6C2-DB58-495C-4B5F-3A4A6532A542"
		},
		{
			"etask.entity": "sc012592",
			"id": "DB866F63-0975-0F38-314A-ABCCD4C2EFF8"
		},
		{
			"etask.entity": "sc012594",
			"id": "24AD494D-0570-5797-E370-F3890032EC3D"
		},
		{
			"etask.entity": "sc012599",
			"id": "93EB2879-0DC1-25B4-0355-8331A4BE0CE9"
		},
		{
			"etask.entity": "sc012604",
			"id": "2CD6573F-E536-53B8-4399-ACF74BA0F968"
		},
		{
			"etask.entity": "sc012609",
			"id": "3E2970F2-80E8-5500-A276-E3BFB1AEE77F"
		},
		{
			"etask.entity": "sc012614",
			"id": "D9C2863F-BBD5-AB47-08D9-87374E1B8FB5"
		},
		{
			"etask.entity": "sc012616",
			"id": "1B474F60-DC1F-5B5B-267A-28BFD72760C1"
		},
		{
			"etask.entity": "sc012621",
			"id": "ED4E2AD2-8E88-2002-EAD7-26E200F0A697"
		},
		{
			"etask.entity": "sc012626",
			"id": "4DC92767-4D02-478C-AAE3-DC725AD1B497"
		},
		{
			"etask.entity": "sc012631",
			"id": "8DF7FB1C-35D8-5AAB-7C58-34E68ED135F7"
		},
		{
			"etask.entity": "sc012636",
			"id": "C60A2B39-E6C0-17A1-458C-203B77309813"
		},
		{
			"etask.entity": "sc012638",
			"id": "ECD849A6-27CF-CC27-17B9-6B0372F91C18"
		},
		{
			"etask.entity": "sc012643",
			"id": "543D6266-978A-1FE9-5862-F29A67384908"
		},
		{
			"etask.entity": "sc012648",
			"id": "F2D470A7-13AE-46E4-F1EE-0BF57C0BF53E"
		},
		{
			"etask.entity": "sc012653",
			"id": "A6537260-1AAA-D8AB-5AD0-FB1F4CD2608F"
		},
		{
			"etask.entity": "sc012658",
			"id": "B009E21B-B49E-04B4-7097-04C73C98C9D3"
		},
		{
			"etask.entity": "sc012660",
			"id": "AB331B01-3CB7-11F4-20D1-80549E046C88"
		},
		{
			"etask.entity": "sc012665",
			"id": "B04F5F7D-765C-A205-CE69-4A773A7043D5"
		},
		{
			"etask.entity": "sc023564",
			"id": "F2CA9707-096A-F8BD-8964-856EF7FA22B0"
		},
		{
			"etask.entity": "sc015807",
			"id": "03DDDC6B-AC30-E262-6636-DC252F44D981"
		},
		{
			"etask.entity": "sc015808",
			"id": "181C373B-9507-C2C1-55F6-C619D9A048F3"
		},
		{
			"etask.entity": "sc015809",
			"id": "DBEF4189-199D-39E2-2910-332A1EA265D9"
		},
		{
			"etask.entity": "sc015810",
			"id": "659EF100-66CC-F994-5328-CF881C02F5F7"
		},
		{
			"etask.entity": "sc015812",
			"id": "E132CF9D-D81E-DC9F-30B6-4B9F254276EC"
		},
		{
			"etask.entity": "sc015813",
			"id": "7ECEA581-3A1D-6390-852E-5A9F8C24997A"
		},
		{
			"etask.entity": "sc015814",
			"id": "6808834B-C702-EE95-0D40-106E6F941CF7"
		},
		{
			"etask.entity": "sc015815",
			"id": "A8F9167D-55CC-77D6-3747-5EC910D95B4D"
		},
		{
			"etask.entity": "sc015817",
			"id": "6550B426-24A6-7A71-3771-2960BD14F6EA"
		},
		{
			"etask.entity": "sc015818",
			"id": "1EB8003A-FCBA-18B6-FBEF-EFBB1311AA8A"
		},
		{
			"etask.entity": "sc015819",
			"id": "4D7C0078-785F-E0E0-6C5E-71A8E0A3FCBB"
		},
		{
			"etask.entity": "sc015820",
			"id": "FF112075-2E54-7C68-339B-C94CB8AD8506"
		},
		{
			"etask.entity": "sc015822",
			"id": "B0A9F2BC-C607-E477-E5BD-27C82AD7361E"
		},
		{
			"etask.entity": "sc015823",
			"id": "03B3B4B7-4592-6320-8739-4A7CB95D0F82"
		},
		{
			"etask.entity": "sc015824",
			"id": "157CFCF8-597D-CF46-1A30-1FAB5E5D05C8"
		},
		{
			"etask.entity": "sc015825",
			"id": "B4D34BD5-1AC3-E81E-EB99-D04750B7F35F"
		},
		{
			"etask.entity": "sc015827",
			"id": "81C5B335-04B9-DD05-89F5-1C828955DC31"
		},
		{
			"etask.entity": "sc023565",
			"id": "FCFF1229-8A2C-1BAD-024C-9EE10D754537"
		},
		{
			"etask.entity": "sc015829",
			"id": "112F7CD4-5107-A647-1526-9B7EF0190765"
		},
		{
			"etask.entity": "sc015830",
			"id": "DF273226-C432-5694-26CD-C4976FBC83BF"
		},
		{
			"etask.entity": "sc015831",
			"id": "026E35EA-7B27-65DF-93BC-1C4EC43CDD6F"
		},
		{
			"etask.entity": "sc015832",
			"id": "706F98F6-7E42-1A3F-45D8-38FD6933010F"
		},
		{
			"etask.entity": "sc015834",
			"id": "77412AC7-7915-B30F-61C5-0D60B5C72A8B"
		},
		{
			"etask.entity": "sc015835",
			"id": "B556198A-3E7B-0A61-3AE7-5E203C2F5CD9"
		},
		{
			"etask.entity": "sc015836",
			"id": "1E125CE8-553B-D490-7B64-D8603162B45F"
		},
		{
			"etask.entity": "sc015837",
			"id": "BFE28D7F-AD49-10AA-60E3-8450558A858C"
		},
		{
			"etask.entity": "sc015839",
			"id": "AB00C779-9FC7-2DC4-3CDD-9783A750D8A8"
		},
		{
			"etask.entity": "sc015840",
			"id": "F1696D39-9FB5-64B3-0FB8-97037961B1D5"
		},
		{
			"etask.entity": "sc015841",
			"id": "6D6B6604-28FD-09D7-68D5-B579D36007C8"
		},
		{
			"etask.entity": "sc015842",
			"id": "E976D178-98DF-DD06-F2B5-93ABF53D6C11"
		},
		{
			"etask.entity": "sc015844",
			"id": "7F6EA972-9A66-55B7-AD98-EE976CFD992A"
		},
		{
			"etask.entity": "sc015845",
			"id": "1A359CE1-22D9-1F71-C75C-C5457A20532C"
		},
		{
			"etask.entity": "sc015846",
			"id": "B7EA7EB7-C370-D59F-6D13-336A0ABF5A12"
		},
		{
			"etask.entity": "sc015847",
			"id": "EB1E957B-A9A6-488C-10D5-89D16E053426"
		},
		{
			"etask.entity": "sc015849",
			"id": "587EAD28-2D21-3A42-CBE1-B657CFF5AE1B"
		},
		{
			"etask.entity": "sc023566",
			"id": "629C2193-83D7-BE12-0BB8-3EBDAA5B5809"
		},
		{
			"etask.entity": "sc015851",
			"id": "224FD3F6-5C23-5F39-8A8F-E02DCF3B0D7D"
		},
		{
			"etask.entity": "sc015852",
			"id": "F0FD07F0-F3E0-509B-1A5D-D18E97806B86"
		},
		{
			"etask.entity": "sc015853",
			"id": "835C8CD5-AE7D-E149-1A12-B0201D7B4C0D"
		},
		{
			"etask.entity": "sc015854",
			"id": "2D3510CD-692F-89F3-A776-02CEB32C7406"
		},
		{
			"etask.entity": "sc015856",
			"id": "40FD11CD-D6EA-C625-7253-67F8947EC332"
		},
		{
			"etask.entity": "sc015857",
			"id": "5772B6C2-8A3A-5EA9-2ED0-27BE14956C81"
		},
		{
			"etask.entity": "sc015858",
			"id": "09946A7B-13A4-E190-AEF2-A781DBCEF66D"
		},
		{
			"etask.entity": "sc015859",
			"id": "F2045C28-94AC-34A8-87A8-978FA6C7BA4C"
		},
		{
			"etask.entity": "sc015861",
			"id": "ABBA3A5B-E694-1FAF-5512-324926C7685C"
		},
		{
			"etask.entity": "sc015862",
			"id": "F8EDA60D-D7FF-F4B3-FCBE-9665C6B67B6D"
		},
		{
			"etask.entity": "sc015863",
			"id": "9D5CE2CD-B185-C7EE-1761-5481EA28BEE9"
		},
		{
			"etask.entity": "sc015864",
			"id": "C4121EDF-E79E-3572-0FCC-E677603CD901"
		},
		{
			"etask.entity": "sc015866",
			"id": "59986D0D-6E06-261E-F4EA-09B39B60EEF4"
		},
		{
			"etask.entity": "sc015867",
			"id": "096FD38E-BB09-E573-DFE5-D55E297C3BDE"
		},
		{
			"etask.entity": "sc015868",
			"id": "A6A48538-4D63-DAC5-A16E-6D3F9F401A58"
		},
		{
			"etask.entity": "sc015869",
			"id": "75124172-70D4-2229-526B-6099C159FA18"
		},
		{
			"etask.entity": "sc015871",
			"id": "12D74636-6C11-626C-B01E-3A594681D01C"
		},
		{
			"etask.entity": "sc012670",
			"id": "CD24A36E-CF77-B254-04B9-1F4B73708BBB"
		},
		{
			"etask.entity": "sc012675",
			"id": "37B54EAA-BBC7-72E3-488D-3B733B9E3ED4"
		},
		{
			"etask.entity": "sc012680",
			"id": "AD260E84-8880-1C79-FF9F-273BA81C8AC5"
		},
		{
			"etask.entity": "sc012682",
			"id": "A3810E36-4089-880E-69D2-071D658A481A"
		},
		{
			"etask.entity": "sc012687",
			"id": "EDD848CE-AAFD-87BA-7056-9A6D206DDB93"
		},
		{
			"etask.entity": "sc012692",
			"id": "30556545-0119-9553-0D7D-76D4121F9D5C"
		},
		{
			"etask.entity": "sc012697",
			"id": "27A9376B-4F56-2D99-A70E-D4807C90EFD7"
		},
		{
			"etask.entity": "sc012702",
			"id": "6BBC4A40-50AB-E465-C072-B81BE785E1B8"
		},
		{
			"etask.entity": "sc012704",
			"id": "5243A417-DD49-0703-62F5-C75983CBC976"
		},
		{
			"etask.entity": "sc012709",
			"id": "2888CADF-EC74-F662-16F3-E626467C39A1"
		},
		{
			"etask.entity": "sc012714",
			"id": "29CFD881-634F-2566-3347-75FCC25A9838"
		},
		{
			"etask.entity": "sc012719",
			"id": "839DD131-57AD-DA93-5C8C-AE0A306F429C"
		},
		{
			"etask.entity": "sc012724",
			"id": "C25256A4-F03E-69BB-82DC-A8E2ED6BC4BD"
		},
		{
			"etask.entity": "sc012726",
			"id": "52F63AD1-3732-253D-FCAE-736ADEA5FC20"
		},
		{
			"etask.entity": "sc012731",
			"id": "97AFDD3B-1719-72F1-9706-EE1E125E2211"
		},
		{
			"etask.entity": "sc012736",
			"id": "6DD9ABDA-9972-E81C-C771-E7EA8998DB55"
		},
		{
			"etask.entity": "sc012741",
			"id": "E5A1EF6A-58DE-61F8-D6C6-2DCAF527084F"
		},
		{
			"etask.entity": "sc012746",
			"id": "28D9C125-4D62-FF23-575A-219DDE776C6B"
		},
		{
			"etask.entity": "sc023567",
			"id": "E251BF59-B45E-7DC3-CEBA-676C60E88BB5"
		},
		{
			"etask.entity": "sc015873",
			"id": "8FFEA840-4607-ECF5-C1A7-6AA4D546AE12"
		},
		{
			"etask.entity": "sc015874",
			"id": "2892FD76-3E43-5F3D-14A1-CFF9B68E7B95"
		},
		{
			"etask.entity": "sc015875",
			"id": "58353C20-3713-7FA3-30E6-C7A991A7BA1C"
		},
		{
			"etask.entity": "sc015876",
			"id": "39E8068C-4EE8-E5B3-05D9-A4FAF6B52B37"
		},
		{
			"etask.entity": "sc015878",
			"id": "C5230AA2-D183-95C2-47D1-358CDB5BAD3D"
		},
		{
			"etask.entity": "sc015879",
			"id": "56EAA3F6-9115-D82A-AE66-C2BB03266B93"
		},
		{
			"etask.entity": "sc015880",
			"id": "3ED4C72C-D508-F825-1FD4-017778A76BF1"
		},
		{
			"etask.entity": "sc015881",
			"id": "7CA2903F-B535-E887-7B5A-EA75622AF870"
		},
		{
			"etask.entity": "sc015883",
			"id": "67B6AB4F-7F26-22FA-53E1-FD3794A83670"
		},
		{
			"etask.entity": "sc015884",
			"id": "34C7FC2E-EE05-312A-0AC3-3AD314FD6F0B"
		},
		{
			"etask.entity": "sc015885",
			"id": "D2E2C9DD-ABDF-0425-4744-85AF722D96BB"
		},
		{
			"etask.entity": "sc015886",
			"id": "22AF5FF0-F4EE-FA8D-F750-4FE079832729"
		},
		{
			"etask.entity": "sc015888",
			"id": "EEA4A0ED-86FF-60BF-3285-E4A6E5B3CACE"
		},
		{
			"etask.entity": "sc015889",
			"id": "805064C8-711C-CCB2-D78E-DFC386E2E33D"
		},
		{
			"etask.entity": "sc015890",
			"id": "7FF268E9-67DE-0F78-9AEC-953752E411EE"
		},
		{
			"etask.entity": "sc015891",
			"id": "29815A1A-0C3C-61C4-900C-D96D76E5325E"
		},
		{
			"etask.entity": "sc015893",
			"id": "B13F15B0-AF97-F7C2-1E1A-977F4A30569D"
		},
		{
			"etask.entity": "sc023568",
			"id": "3841E33F-4137-1C17-37FB-E85D6C48D660"
		},
		{
			"etask.entity": "sc015895",
			"id": "F5B0A3DF-9272-C41E-0981-6132DEFCCB3D"
		},
		{
			"etask.entity": "sc015896",
			"id": "AA1DB164-0476-F18C-4080-E4BDACF7A25E"
		},
		{
			"etask.entity": "sc015897",
			"id": "C4633A44-78CC-056C-C48A-85B1AD9D7CA7"
		},
		{
			"etask.entity": "sc015898",
			"id": "20EFF44A-6976-D072-5E81-A79B48C83A02"
		},
		{
			"etask.entity": "sc015900",
			"id": "EE978F0A-4EF3-2CC6-F552-A1C3FE8795FE"
		},
		{
			"etask.entity": "sc015901",
			"id": "11E1AA9B-CEB6-8822-43EC-3806B3DD7E6D"
		},
		{
			"etask.entity": "sc015902",
			"id": "689710B7-8299-858A-342A-B1F7C2448B64"
		},
		{
			"etask.entity": "sc015903",
			"id": "54CCC808-12BF-816A-C57C-371C34AB831C"
		},
		{
			"etask.entity": "sc015905",
			"id": "B9B5603A-D156-4F55-81A3-7CE9CA5195F5"
		},
		{
			"etask.entity": "sc015906",
			"id": "07812E51-E9AB-14E3-5382-0688F38BC2BF"
		},
		{
			"etask.entity": "sc015907",
			"id": "04E45B7C-E121-F15D-69BC-12F684CD9372"
		},
		{
			"etask.entity": "sc015908",
			"id": "E30D65F1-3DF3-F19E-F3DB-835494476498"
		},
		{
			"etask.entity": "sc015910",
			"id": "64D99D6F-CC28-5360-B1E9-0E3E9BACDC7D"
		},
		{
			"etask.entity": "sc015911",
			"id": "64D18CEE-3F4D-F7FD-1AEE-A6D8A7FF8061"
		},
		{
			"etask.entity": "sc015912",
			"id": "9E9943C5-6D5E-054F-70DE-5C100DCC68DA"
		},
		{
			"etask.entity": "sc015913",
			"id": "09D132DF-9A5A-48B2-A998-22336042652C"
		},
		{
			"etask.entity": "sc015915",
			"id": "520B4EFF-8DD8-2E75-7D7A-884578FBC3C4"
		},
		{
			"etask.entity": "sc023569",
			"id": "A8955B92-6325-B470-DB73-DEAD24CDBFC0"
		},
		{
			"etask.entity": "sc015917",
			"id": "0849E554-FBA9-2DC6-4146-95871ECC5900"
		},
		{
			"etask.entity": "sc015918",
			"id": "8D259A4A-B389-EA7B-A6C9-8350F1D50347"
		},
		{
			"etask.entity": "sc015919",
			"id": "5C6E7823-9265-0086-93F1-A53FD7DFA245"
		},
		{
			"etask.entity": "sc015920",
			"id": "07CA489C-9644-BFB1-F263-45BD9B6939C4"
		},
		{
			"etask.entity": "sc015922",
			"id": "1E92A31D-FE55-9B63-9CF1-2F6890B0B281"
		},
		{
			"etask.entity": "sc015923",
			"id": "7715EF16-A338-ADF2-B494-33D65B6876D1"
		},
		{
			"etask.entity": "sc015924",
			"id": "6CB25924-17F0-52AB-D53F-2C0CE7D1B3E8"
		},
		{
			"etask.entity": "sc015925",
			"id": "7730AF26-A455-DCFD-C92C-EB0EFEC2DAA9"
		},
		{
			"etask.entity": "sc015927",
			"id": "F08A9C63-3ED2-FA71-7949-418EF0F24EA7"
		},
		{
			"etask.entity": "sc015928",
			"id": "FD477407-1266-7DE0-F9CD-FF0C0D6CF4AC"
		},
		{
			"etask.entity": "sc015929",
			"id": "D52F7628-18DD-D348-6184-C4658AC16EE3"
		},
		{
			"etask.entity": "sc015930",
			"id": "E3D529B5-69DF-74B5-45C5-92093B04FA3C"
		},
		{
			"etask.entity": "sc015932",
			"id": "9E239C5D-7789-89E5-92DE-7E80C5EA62C5"
		},
		{
			"etask.entity": "sc015933",
			"id": "BA968AA4-B9F9-34ED-383C-49281EBEE973"
		},
		{
			"etask.entity": "sc015934",
			"id": "750CB7AB-0FDF-09AE-252C-949D67C09F8A"
		},
		{
			"etask.entity": "sc015935",
			"id": "1CDEB838-2A0F-A7D5-C6EF-D13DEC37237D"
		},
		{
			"etask.entity": "sc015937",
			"id": "6BCCB875-BBD4-9581-4B5F-38FA593D656E"
		},
		{
			"etask.entity": "sc023570",
			"id": "0FB5F4D9-B941-1140-476C-FA6F7495934D"
		},
		{
			"etask.entity": "sc015939",
			"id": "518A98FC-AE83-FB9B-392A-E7B77B491B10"
		},
		{
			"etask.entity": "sc015940",
			"id": "BBDEB0D1-93AE-1676-3006-1320ACB5351A"
		},
		{
			"etask.entity": "sc015941",
			"id": "39FAF997-23EE-8743-B362-E1FDB09C71A2"
		},
		{
			"etask.entity": "sc015942",
			"id": "3830DB45-1EA2-D11D-7D51-99C7496760E6"
		},
		{
			"etask.entity": "sc015944",
			"id": "9AB7B10B-7F3D-273F-E7C6-D19017548DEF"
		},
		{
			"etask.entity": "sc015945",
			"id": "2C310F7A-FC76-1483-2737-9542B497631A"
		},
		{
			"etask.entity": "sc015946",
			"id": "76263796-0538-BE6D-13C0-E28567CE337E"
		},
		{
			"etask.entity": "sc015947",
			"id": "517CE49C-6981-ED5D-F25C-16865C07A47F"
		},
		{
			"etask.entity": "sc015949",
			"id": "DD500797-654E-C93F-8A9A-4AC194DC544C"
		},
		{
			"etask.entity": "sc015950",
			"id": "32B080C3-22A3-3927-83F6-7FBE5CFFCE4E"
		},
		{
			"etask.entity": "sc015951",
			"id": "59123039-DE55-26A5-3A38-210B938A24FA"
		},
		{
			"etask.entity": "sc015952",
			"id": "486FF422-2F66-E574-D4D5-EE16610CF52B"
		},
		{
			"etask.entity": "sc015954",
			"id": "680BF4BA-83E2-B0F7-48DC-CECBEBFF5886"
		},
		{
			"etask.entity": "sc015955",
			"id": "44AB63D8-B23C-89D0-1C80-C7F6F2FFC4EF"
		},
		{
			"etask.entity": "sc015956",
			"id": "D415C28E-BD7C-9A15-2906-55537C35A0E6"
		},
		{
			"etask.entity": "sc015957",
			"id": "D15975BE-B401-C078-A05B-80104823407A"
		},
		{
			"etask.entity": "sc015959",
			"id": "6A7670F5-C70E-E8BF-7235-080A9A85048B"
		},
		{
			"etask.entity": "sc012748",
			"id": "E8980F80-1C50-286C-7949-FF4640BF1797"
		},
		{
			"etask.entity": "sc012753",
			"id": "FCE66F58-F6B4-E9A9-7DBF-8123CBC89BB1"
		},
		{
			"etask.entity": "sc012758",
			"id": "3D5F03B7-C8E8-1E64-B3FA-1C1BBE6B891B"
		},
		{
			"etask.entity": "sc012763",
			"id": "160F46BD-0BDE-645E-9D52-63C2CA20AB29"
		},
		{
			"etask.entity": "sc012768",
			"id": "BF4530A8-345B-028A-1D33-CF662F951064"
		},
		{
			"etask.entity": "sc012770",
			"id": "819CB64F-D8B1-63E9-BFE6-F0EECBF88957"
		},
		{
			"etask.entity": "sc012775",
			"id": "03018E03-BA68-0F29-6092-D3E9BB664945"
		},
		{
			"etask.entity": "sc012780",
			"id": "10E1570D-4AF3-897F-E204-C2085B8B43DB"
		},
		{
			"etask.entity": "sc012785",
			"id": "F8D421CA-4F16-0F23-5250-0DFADF84D26B"
		},
		{
			"etask.entity": "sc012790",
			"id": "071ED0A7-EF2D-CDF2-ED5B-88BD7FEB2E75"
		},
		{
			"etask.entity": "sc012792",
			"id": "C112F91E-8547-891D-36BF-679CAA635896"
		},
		{
			"etask.entity": "sc012797",
			"id": "F7E74AA1-DA77-8E84-6205-E3C9613ECB89"
		},
		{
			"etask.entity": "sc012802",
			"id": "B3D33E03-24FC-2C3F-8249-C9567296C9D8"
		},
		{
			"etask.entity": "sc012807",
			"id": "97066D6C-5DAE-7B6E-9329-7078C8324402"
		},
		{
			"etask.entity": "sc012812",
			"id": "4EC75A17-CC59-DB23-DA77-0C1573FBF19F"
		},
		{
			"etask.entity": "sc012814",
			"id": "97EFA7BD-C2BC-FBD7-733E-A172156376B6"
		},
		{
			"etask.entity": "sc012819",
			"id": "74BE6B4A-A047-D7D3-8C31-B30E02DAB364"
		},
		{
			"etask.entity": "sc012824",
			"id": "74A58120-DC9F-D9B1-89B9-0E6BD2A21E9A"
		},
		{
			"etask.entity": "sc023571",
			"id": "73D7431A-E285-61F0-6745-E5D2CBDE174E"
		},
		{
			"etask.entity": "sc015961",
			"id": "93A36E02-7C1C-0E64-045E-2D58D9CFB723"
		},
		{
			"etask.entity": "sc015962",
			"id": "A7C6B260-F655-C6CD-06D5-AC9E5DAEDD2F"
		},
		{
			"etask.entity": "sc015963",
			"id": "6EF0B7F8-FF54-B28D-1351-D5B734652227"
		},
		{
			"etask.entity": "sc015964",
			"id": "3A5306E9-55DB-21DB-4241-0FEEB9B00A2C"
		},
		{
			"etask.entity": "sc015966",
			"id": "9BD5230E-0F2A-840C-BAC2-AAF12384972D"
		},
		{
			"etask.entity": "sc015967",
			"id": "402E73E5-D64B-E9BF-1041-F4426F1E5F21"
		},
		{
			"etask.entity": "sc015968",
			"id": "229CB62D-80FB-7ACC-CBB5-90004AF6C86D"
		},
		{
			"etask.entity": "sc015969",
			"id": "CFC18E77-B4F8-BCFB-3527-0621AE6E1DBC"
		},
		{
			"etask.entity": "sc015971",
			"id": "98E82D3B-5B4F-2D18-0A03-79FC1EDE0447"
		},
		{
			"etask.entity": "sc015972",
			"id": "BF81652D-D879-7D1E-E0F3-47BE2869DBA6"
		},
		{
			"etask.entity": "sc015973",
			"id": "F137C129-21A7-A92E-88C0-07F4B2789F12"
		},
		{
			"etask.entity": "sc015974",
			"id": "130FED86-C55C-5A6C-43A1-071348A8D5DD"
		},
		{
			"etask.entity": "sc015976",
			"id": "AEC6A479-9CC4-BE41-CB3C-77EE2EF13998"
		},
		{
			"etask.entity": "sc015977",
			"id": "216DBD70-CF91-5653-2EC1-1657A2235E8B"
		},
		{
			"etask.entity": "sc015978",
			"id": "96B430CE-86AD-925D-650B-CBBFF49B68E9"
		},
		{
			"etask.entity": "sc015979",
			"id": "221BD814-A824-94F9-6500-1960D2865C09"
		},
		{
			"etask.entity": "sc015981",
			"id": "F0B07B28-C3F5-8872-2054-F1C7DF4ACB00"
		},
		{
			"etask.entity": "sc023572",
			"id": "69015CAA-89BC-033C-E7A5-1A27AE31EE40"
		},
		{
			"etask.entity": "sc015983",
			"id": "8EDEF4D9-A5AE-F38D-D0F7-925DCE663E78"
		},
		{
			"etask.entity": "sc015984",
			"id": "7017DF6E-DA6A-1D1D-CF01-D9CA70B81A3E"
		},
		{
			"etask.entity": "sc015985",
			"id": "6F866513-395F-5D20-4B26-49CFE674748A"
		},
		{
			"etask.entity": "sc015986",
			"id": "523CB4BE-113A-0543-2387-065D1DACD7CA"
		},
		{
			"etask.entity": "sc015988",
			"id": "F6AD8FA8-BA60-017F-2FCC-37DA0AFE5CE8"
		},
		{
			"etask.entity": "sc015989",
			"id": "44552094-F380-8381-A9D2-A36A31EFE7DB"
		},
		{
			"etask.entity": "sc015990",
			"id": "68883B72-B671-1836-D9E0-8E2ABC88D42E"
		},
		{
			"etask.entity": "sc015991",
			"id": "3F64A456-63BF-ADC8-9164-61D34D7184BF"
		},
		{
			"etask.entity": "sc015993",
			"id": "3596A354-AA36-150A-21E2-2798075B3FE2"
		},
		{
			"etask.entity": "sc015994",
			"id": "B384A69B-B4A5-5A53-F3B6-1733782FAAE8"
		},
		{
			"etask.entity": "sc015995",
			"id": "CC37B491-9112-7386-A0FB-EF4A1BC7593C"
		},
		{
			"etask.entity": "sc015996",
			"id": "7F5C6BF9-B547-84FF-BBC7-2B1BFB8B5394"
		},
		{
			"etask.entity": "sc015998",
			"id": "CEE32B0D-1E40-C561-605D-45C41D2BF241"
		},
		{
			"etask.entity": "sc015999",
			"id": "1FA11160-8D79-63AF-9728-0B9632D6CC33"
		},
		{
			"etask.entity": "sc016000",
			"id": "14015243-EB8B-26B1-103C-1A5BDE3E653E"
		},
		{
			"etask.entity": "sc016001",
			"id": "309194EB-7162-DEAE-6479-34506E3BEB04"
		},
		{
			"etask.entity": "sc016003",
			"id": "371D858A-3EFB-BDA8-B65F-76FCA478DF0D"
		},
		{
			"etask.entity": "sc023573",
			"id": "545962EC-7DBA-99F4-B72D-45A21529FEB8"
		},
		{
			"etask.entity": "sc016005",
			"id": "3FC9C426-EBBA-2A35-CA10-7C373A0C3284"
		},
		{
			"etask.entity": "sc016006",
			"id": "3D1D23E3-FA87-2C66-099A-079A7AC8F756"
		},
		{
			"etask.entity": "sc016007",
			"id": "B4497F1C-4ED9-F56F-F378-F03CF2C50EE6"
		},
		{
			"etask.entity": "sc016008",
			"id": "2414A780-B6E8-7AF8-0606-5501C7AC51CE"
		},
		{
			"etask.entity": "sc016265",
			"id": "1B14023B-23B0-85F9-02C0-815B586A10E6"
		},
		{
			"etask.entity": "sc016266",
			"id": "3A06ADEB-3F01-7395-DB60-D90A869A0BC3"
		},
		{
			"etask.entity": "sc016267",
			"id": "0F2FA1CC-193A-79A8-76D9-CBD1713739B5"
		},
		{
			"etask.entity": "sc016268",
			"id": "00E7BF28-4519-C97D-978E-2EC40A817C74"
		},
		{
			"etask.entity": "sc016270",
			"id": "2A2735B6-CED6-8AC3-BFEC-D6EB096FDA64"
		},
		{
			"etask.entity": "sc016271",
			"id": "A6CD6411-110E-8D77-7263-3F765F21A3AB"
		},
		{
			"etask.entity": "sc016272",
			"id": "530C7045-DAB5-B665-A6C6-6DAF08124C0D"
		},
		{
			"etask.entity": "sc016273",
			"id": "EADBE7D5-3F48-53F3-D002-C78AAD20122D"
		},
		{
			"etask.entity": "sc016275",
			"id": "AAAC0FB6-6F8A-97BF-C81C-D4718FFA227E"
		},
		{
			"etask.entity": "sc016276",
			"id": "F98FC218-E147-4B0A-9FE9-543DDE97232C"
		},
		{
			"etask.entity": "sc016277",
			"id": "19044DFC-E8FE-8A65-C0C0-2E6B5FFEFA8C"
		},
		{
			"etask.entity": "sc016278",
			"id": "CB29E9AC-4B44-E620-6982-CC91DB069CAC"
		},
		{
			"etask.entity": "sc016280",
			"id": "D6C65944-1FFC-A0D7-12A7-57C09DF3D25D"
		},
		{
			"etask.entity": "sc023574",
			"id": "8EE042E4-061E-0B8E-2A7A-ACD15D342B34"
		},
		{
			"etask.entity": "sc016287",
			"id": "0F0922AE-B083-4C60-7178-4AEC1947972A"
		},
		{
			"etask.entity": "sc016288",
			"id": "DD3D4E9A-70FA-1371-A2CF-15DAA8A13496"
		},
		{
			"etask.entity": "sc016289",
			"id": "B78ED974-E27F-EC02-CAD2-6B8B14BFDA59"
		},
		{
			"etask.entity": "sc016290",
			"id": "C20B61EC-A7E1-E258-82B7-A0A0642156F2"
		},
		{
			"etask.entity": "sc016292",
			"id": "F700A765-6013-3AF8-7CBF-6D66D60F268B"
		},
		{
			"etask.entity": "sc016293",
			"id": "C1759F2C-30B3-3ED5-CF3C-93787144D9A1"
		},
		{
			"etask.entity": "sc016294",
			"id": "F1F23993-C784-C217-9811-CF4EF384237A"
		},
		{
			"etask.entity": "sc016295",
			"id": "739D8A06-5C38-042C-3884-4C893014D047"
		},
		{
			"etask.entity": "sc016297",
			"id": "1295CA56-4FF9-9338-215C-7C66AA415330"
		},
		{
			"etask.entity": "sc016298",
			"id": "4BCBC446-3FC0-F15D-2F7E-842DE7FD6231"
		},
		{
			"etask.entity": "sc016299",
			"id": "0C6A9BC1-7CEA-62C5-D463-E3E6639A37A1"
		},
		{
			"etask.entity": "sc016300",
			"id": "48604B33-7BDE-5C36-A182-385E3EB06702"
		},
		{
			"etask.entity": "sc016302",
			"id": "3BF8C354-8138-39F9-8F9C-9658082DCF06"
		},
		{
			"etask.entity": "sc016303",
			"id": "ED977C7A-7C8F-4681-CA43-3D337F78F63B"
		},
		{
			"etask.entity": "sc016304",
			"id": "62CB4454-0465-EDF1-E3AE-1027A92DF1A8"
		},
		{
			"etask.entity": "sc016305",
			"id": "353F4E9F-D3A2-1875-7654-EA937F070281"
		},
		{
			"etask.entity": "sc016307",
			"id": "5E5D508A-0121-E61C-4BAD-CE0344DBBBFE"
		},
		{
			"etask.entity": "sc013120",
			"id": "F4705D73-F918-3296-5597-D78250FE09BC"
		},
		{
			"etask.entity": "sc013122",
			"id": "95395BC5-CB24-1812-A451-3B6BDA2C0AEE"
		},
		{
			"etask.entity": "sc013127",
			"id": "00255068-9F77-83EA-A248-D2313AA73FF2"
		},
		{
			"etask.entity": "sc013132",
			"id": "A0263188-EDAD-36E2-C1C4-95E3D4EB8FB1"
		},
		{
			"etask.entity": "sc013137",
			"id": "D6227ADE-5D89-682E-2BC5-3409CFD4B106"
		},
		{
			"etask.entity": "sc013142",
			"id": "0FE2D7CD-C0E7-7BA6-8999-0E40DCCF614B"
		},
		{
			"etask.entity": "sc013144",
			"id": "C9381384-1BDA-A41D-163D-EADBE3F05ED0"
		},
		{
			"etask.entity": "sc013149",
			"id": "74A79E87-E599-6332-7F8C-20A9200531E0"
		},
		{
			"etask.entity": "sc013154",
			"id": "3D62F19E-EA13-D58A-D466-ACB6A3EB541A"
		},
		{
			"etask.entity": "sc013159",
			"id": "FFBEA2C6-A02E-B1CF-DDDA-BA633DBCF311"
		},
		{
			"etask.entity": "sc013164",
			"id": "C77386BD-0B86-0E13-5421-F17C27D1B0A3"
		},
		{
			"etask.entity": "sc013166",
			"id": "E957C0FC-827A-5ACB-0DDB-5A2C4B893EE2"
		},
		{
			"etask.entity": "sc013171",
			"id": "856D10F8-8F0C-4C4F-760B-58C8740F13BD"
		},
		{
			"etask.entity": "sc013176",
			"id": "D4FBC818-23BD-8634-1BB0-119C8933F619"
		},
		{
			"etask.entity": "sc013181",
			"id": "25F0ABA9-AB16-501D-CC0E-7005FE9EC385"
		},
		{
			"etask.entity": "sc013186",
			"id": "DFF85CE0-5335-5594-6689-EA64CB78955D"
		},
		{
			"etask.entity": "sc013188",
			"id": "DFDEB85D-1E60-278B-C100-CFDF1980A332"
		},
		{
			"etask.entity": "sc013193",
			"id": "A8A12F0D-3CE1-E49E-114A-41DF57A02A30"
		},
		{
			"etask.entity": "sc023575",
			"id": "9B1431C4-F5B3-2F89-22CF-0ABD6CA9E0E0"
		},
		{
			"etask.entity": "sc016309",
			"id": "D7068090-38D5-1323-150E-3315A9BCEB85"
		},
		{
			"etask.entity": "sc016310",
			"id": "9BB52627-51F5-A74A-B2C1-631E4FEC7103"
		},
		{
			"etask.entity": "sc016311",
			"id": "D72258C1-8C39-194E-AE6E-58611D0926AF"
		},
		{
			"etask.entity": "sc016312",
			"id": "D2FCD797-891F-91B4-BEC8-FEBBD0355A1E"
		},
		{
			"etask.entity": "sc016314",
			"id": "52970D68-3979-35CD-B03C-75A48C74B6BC"
		},
		{
			"etask.entity": "sc016315",
			"id": "2C696B44-CF0F-27D7-9653-3CDAEB1ABFA6"
		},
		{
			"etask.entity": "sc016316",
			"id": "6B352E18-8DFE-33B7-72F0-06D919CB01DC"
		},
		{
			"etask.entity": "sc016317",
			"id": "14708E94-606F-BB2A-A614-0A02046D38B2"
		},
		{
			"etask.entity": "sc016319",
			"id": "D591B19E-8FCD-7FEA-A53D-C93825F90938"
		},
		{
			"etask.entity": "sc016320",
			"id": "B55C9996-65F6-EBD5-0BF6-3D6EF11E7E77"
		},
		{
			"etask.entity": "sc016321",
			"id": "C4FED6C5-7A8B-28FF-C563-69F1B0BF8004"
		},
		{
			"etask.entity": "sc016322",
			"id": "C5B8B451-DA13-E462-89BA-C745657BB83B"
		},
		{
			"etask.entity": "sc016324",
			"id": "B067DFE0-3E39-89F4-B1BA-AAB849761EBE"
		},
		{
			"etask.entity": "sc016325",
			"id": "3DBD5BC8-8E3C-C697-3D2D-8364BBBA215A"
		},
		{
			"etask.entity": "sc016326",
			"id": "47BE76FD-D058-88A8-5D03-7A685FE1CC3A"
		},
		{
			"etask.entity": "sc016327",
			"id": "3DD5C0F1-C430-C971-AFD7-830A619CAFA6"
		},
		{
			"etask.entity": "sc016329",
			"id": "B23B6CA2-58BB-B05B-DD30-5FA1BC2EC1C0"
		},
		{
			"etask.entity": "sc023576",
			"id": "8719589D-79EA-0B6B-59DF-E778FA5384AF"
		},
		{
			"etask.entity": "sc016331",
			"id": "AC5D9B77-AC71-2D0F-A3D5-F699E8898DED"
		},
		{
			"etask.entity": "sc016332",
			"id": "6E2A5FD9-CE1A-CF45-B43C-FB54028AE759"
		},
		{
			"etask.entity": "sc016333",
			"id": "D2DBCACE-2C70-3766-DCAD-2CCDAF6A920C"
		},
		{
			"etask.entity": "sc016334",
			"id": "33751594-5A76-DBD9-78E7-180ABFEC8962"
		},
		{
			"etask.entity": "sc016336",
			"id": "958496D0-D2ED-E105-382A-6A47FC532725"
		},
		{
			"etask.entity": "sc016337",
			"id": "A9F4273A-D302-5914-7B0A-1601E3DA8D4E"
		},
		{
			"etask.entity": "sc016338",
			"id": "65D93614-798A-2E6F-422C-50AC6603772F"
		},
		{
			"etask.entity": "sc016339",
			"id": "3892A80A-E67C-5F9F-BA6C-9BCB29539DFE"
		},
		{
			"etask.entity": "sc016341",
			"id": "8EA2F075-3E45-AF18-8349-47A89BB9EBAB"
		},
		{
			"etask.entity": "sc016342",
			"id": "0A6FD4A1-9E03-A024-A80D-9CC70B6E8E6A"
		},
		{
			"etask.entity": "sc016343",
			"id": "08666D44-EA29-9B87-431F-2CEA39246B53"
		},
		{
			"etask.entity": "sc016344",
			"id": "6B3149A0-9811-AAD4-82F0-0448E67A26B6"
		},
		{
			"etask.entity": "sc016346",
			"id": "5B8055CE-88C4-BF00-B563-FE00B0DF87A6"
		},
		{
			"etask.entity": "sc016347",
			"id": "C72FA0BF-F8A5-C575-DB97-D5AA7AC1ACD4"
		},
		{
			"etask.entity": "sc016348",
			"id": "A6FB3E0F-D675-BDD9-3531-B0CA7852978C"
		},
		{
			"etask.entity": "sc016349",
			"id": "C4CA0A6E-9FBD-C97B-D5D6-154E4B441F43"
		},
		{
			"etask.entity": "sc016351",
			"id": "D85408A6-E8DB-FF80-EC32-AF3DD4D79959"
		},
		{
			"etask.entity": "sc023577",
			"id": "32E0E9DB-0C18-3D67-D619-89ED46A3AF75"
		},
		{
			"etask.entity": "sc016353",
			"id": "97B5A271-5411-FF50-4D63-5A2C8EADE725"
		},
		{
			"etask.entity": "sc016354",
			"id": "B26E12D8-BBAF-C54C-E7E6-B2C8C457DDBE"
		},
		{
			"etask.entity": "sc016355",
			"id": "CD56CE59-1EEC-E979-FF9E-364DD5D3AFA6"
		},
		{
			"etask.entity": "sc016356",
			"id": "2EDAC93D-04DD-700A-10C4-BEE1A307BBCC"
		},
		{
			"etask.entity": "sc016358",
			"id": "77CA6616-FDA0-9667-AB11-6AC0AEE30765"
		},
		{
			"etask.entity": "sc016359",
			"id": "5FB9D6B8-2C3A-321A-1646-88C9389E8456"
		},
		{
			"etask.entity": "sc016360",
			"id": "7D7E5EED-42E0-9850-647E-F3192C28106B"
		},
		{
			"etask.entity": "sc016361",
			"id": "D97A2054-0120-F8B9-1256-082FED3B676E"
		},
		{
			"etask.entity": "sc016363",
			"id": "488A1885-819A-C2C7-26C1-F7D6A712BE90"
		},
		{
			"etask.entity": "sc016364",
			"id": "B8A7A6C7-7520-BCC8-9004-442E72D0B8E6"
		},
		{
			"etask.entity": "sc016365",
			"id": "DCF11DF5-0761-6992-9D76-4C0821D8BD1E"
		},
		{
			"etask.entity": "sc016366",
			"id": "C53921DA-6FDD-9AB7-5A16-30071F582EF2"
		},
		{
			"etask.entity": "sc016368",
			"id": "0C7DF154-EB12-F795-64EF-AE9994899327"
		},
		{
			"etask.entity": "sc016369",
			"id": "1940016D-7233-CBF0-F7CC-31B207111033"
		},
		{
			"etask.entity": "sc016370",
			"id": "9FEB0731-23B1-08BA-37AE-7EC0B33CDBF8"
		},
		{
			"etask.entity": "sc016371",
			"id": "9C26784E-8F28-30D4-BC01-ECE0249B573A"
		},
		{
			"etask.entity": "sc016373",
			"id": "EBCF65BC-CCBC-6F98-462D-79981F795DF6"
		},
		{
			"etask.entity": "sc013198",
			"id": "E9C8EEDB-8945-FB50-7DFB-608E64CA80AD"
		},
		{
			"etask.entity": "sc013203",
			"id": "45B95529-9711-0184-91A2-8D07BEB2C54D"
		},
		{
			"etask.entity": "sc013208",
			"id": "AD87D54C-8F3F-45C7-E8E4-B0B4FA62C3E7"
		},
		{
			"etask.entity": "sc013210",
			"id": "506B8D4D-00E7-3343-904D-AAA10F0517C4"
		},
		{
			"etask.entity": "sc013215",
			"id": "70F1A4CA-A88D-7108-19CB-53E328BDECA8"
		},
		{
			"etask.entity": "sc013220",
			"id": "2B24BCD2-E6B0-5763-00A4-29355B66DC02"
		},
		{
			"etask.entity": "sc013225",
			"id": "EBAC222A-473D-050F-AC4D-4DACB0E66A46"
		},
		{
			"etask.entity": "sc013230",
			"id": "373E8890-B02F-4AA4-8F1B-08C7CBE38CD7"
		},
		{
			"etask.entity": "sc013232",
			"id": "EC8431F5-DDA1-3F68-16A5-EDC115FB43ED"
		},
		{
			"etask.entity": "sc013237",
			"id": "01FF8A0C-FE55-2BE7-FBF0-271D240869FB"
		},
		{
			"etask.entity": "sc013242",
			"id": "7FF8ED29-1E6E-5155-1E4F-521EA1401600"
		},
		{
			"etask.entity": "sc013247",
			"id": "B9DFD8F9-ACBB-CE34-EA10-BD65419F342A"
		},
		{
			"etask.entity": "sc013252",
			"id": "C3415C6F-CD76-DAEF-164F-51B084F5A39B"
		},
		{
			"etask.entity": "sc013254",
			"id": "28A67875-F15C-156A-5B75-6CA7F00E4FCC"
		},
		{
			"etask.entity": "sc013259",
			"id": "FD15BB28-F2A1-A084-BD53-EC9481057A92"
		},
		{
			"etask.entity": "sc013264",
			"id": "B8167C69-E764-C451-611C-56E08F38BC53"
		},
		{
			"etask.entity": "sc013269",
			"id": "BAC40F73-847E-2680-8DCC-59D9BB2810C1"
		},
		{
			"etask.entity": "sc013274",
			"id": "50AE1BFE-54F6-A0D6-8D76-C38572C27DDE"
		},
		{
			"etask.entity": "sc023578",
			"id": "E18D2A9D-ADA3-B374-DFF9-6C4BF8E3ED82"
		},
		{
			"etask.entity": "sc016375",
			"id": "BBDD93BF-F7CF-BA7F-ED63-05D624807CED"
		},
		{
			"etask.entity": "sc016376",
			"id": "496B232C-510F-1639-474A-7700A94671DD"
		},
		{
			"etask.entity": "sc016377",
			"id": "F849D410-37E3-F97E-C6A3-8150B5C7424E"
		},
		{
			"etask.entity": "sc016378",
			"id": "73E4AFF4-93B3-0F76-B920-B8DDEA809D07"
		},
		{
			"etask.entity": "sc016380",
			"id": "A9C985F9-116E-6B58-12B4-23CF4801CB03"
		},
		{
			"etask.entity": "sc016381",
			"id": "E56B9481-1093-5ADE-9B0A-8720F2A59AE1"
		},
		{
			"etask.entity": "sc016382",
			"id": "935C80AA-5D87-D312-34F8-5C4EB749A75E"
		},
		{
			"etask.entity": "sc016383",
			"id": "D61D8E12-75AF-B98F-4D1B-3834CA25784B"
		},
		{
			"etask.entity": "sc016385",
			"id": "655388C5-4668-FFCE-2EAA-FE720F51E21A"
		},
		{
			"etask.entity": "sc016386",
			"id": "5FCD2359-7490-46DC-FDB2-82B05E5F3A5E"
		},
		{
			"etask.entity": "sc016387",
			"id": "DEAC0CFF-2CFF-4F0F-5C90-C977A3E503D8"
		},
		{
			"etask.entity": "sc016388",
			"id": "778DD78E-5200-61AD-928D-AC538B7461C4"
		},
		{
			"etask.entity": "sc016390",
			"id": "0B914972-9BC9-B66A-769F-3FBCA1F8C61B"
		},
		{
			"etask.entity": "sc016391",
			"id": "ED34BDCA-7CB0-8F55-750B-862D544F3928"
		},
		{
			"etask.entity": "sc016392",
			"id": "D80C1D6C-DEE2-EDEE-CEA1-32E1841C6AA0"
		},
		{
			"etask.entity": "sc016393",
			"id": "1988FF91-6D42-49B5-04D0-25339495E33F"
		},
		{
			"etask.entity": "sc016395",
			"id": "74975778-A8EA-8D9F-1B82-E2B29DCE3C3A"
		},
		{
			"etask.entity": "sc023579",
			"id": "6A3C9A73-92B7-AF5D-9128-0DD8F99FABBF"
		},
		{
			"etask.entity": "sc016397",
			"id": "7A221E7F-28F9-9542-B789-432C1F2603C9"
		},
		{
			"etask.entity": "sc016398",
			"id": "43BF4F80-1944-2581-85AC-7E70ED6E6A42"
		},
		{
			"etask.entity": "sc016399",
			"id": "9184E892-ECC6-C19F-72FA-E05A76DBC4D7"
		},
		{
			"etask.entity": "sc016400",
			"id": "E81FE2E8-16E2-B1E9-B831-7F27FE620ED3"
		},
		{
			"etask.entity": "sc016402",
			"id": "A025443F-87AF-B73A-820C-36EA655E10A5"
		},
		{
			"etask.entity": "sc016403",
			"id": "1EB642C9-94D7-D108-9403-9230701DC986"
		},
		{
			"etask.entity": "sc016404",
			"id": "BE3E73D1-99AC-D6B0-96DF-81E54BA21DFE"
		},
		{
			"etask.entity": "sc016405",
			"id": "4EA48600-8CBD-7624-DCF8-DB7CE7AEFD14"
		},
		{
			"etask.entity": "sc016407",
			"id": "45C4E77E-481E-F254-C689-6812FB477461"
		},
		{
			"etask.entity": "sc016408",
			"id": "BC6CF66C-30F8-EA6C-51C5-8075D38CE8DD"
		},
		{
			"etask.entity": "sc016409",
			"id": "0A82D6BF-3D34-F401-6FD5-96A820FD4B11"
		},
		{
			"etask.entity": "sc016410",
			"id": "C134ED34-9A6D-8660-1074-B33B44F875C9"
		},
		{
			"etask.entity": "sc016412",
			"id": "614258C4-5331-BF1E-B263-3E270B58D2E3"
		},
		{
			"etask.entity": "sc016413",
			"id": "53E1EF0B-09B1-E302-16F0-9DE4546A3904"
		},
		{
			"etask.entity": "sc016414",
			"id": "4C7B9385-2311-E088-9742-A233E580DA26"
		},
		{
			"etask.entity": "sc016415",
			"id": "A31C3924-1E03-3924-4985-149E855E5A99"
		},
		{
			"etask.entity": "sc016417",
			"id": "1B4F306B-BB47-6F8A-410A-0BF15676F376"
		},
		{
			"etask.entity": "sc023580",
			"id": "E4F070A0-00FE-A5E3-3947-B47D0B4B76E1"
		},
		{
			"etask.entity": "sc016419",
			"id": "6EE6BA23-53E1-6BE7-F793-1B3945C95903"
		},
		{
			"etask.entity": "sc016420",
			"id": "FB8DE4DB-49DB-C593-2796-53E7EC483CAA"
		},
		{
			"etask.entity": "sc016421",
			"id": "80C7C04F-DDFE-1012-016B-21D700A10FAA"
		},
		{
			"etask.entity": "sc016422",
			"id": "2A0117C7-C026-5B6A-EDB7-82AA15E0CDE1"
		},
		{
			"etask.entity": "sc016424",
			"id": "5699D231-EE39-EBEC-67E7-BB3CEC4A7B4C"
		},
		{
			"etask.entity": "sc016425",
			"id": "BDB49B27-CBE8-5489-E5F4-24F79EB9518D"
		},
		{
			"etask.entity": "sc016426",
			"id": "03824C19-B4F6-7CCD-5381-3CBFEE2F00C4"
		},
		{
			"etask.entity": "sc016427",
			"id": "9E164B39-250F-26B9-597F-91F27BDFFC66"
		},
		{
			"etask.entity": "sc016429",
			"id": "656A262D-A6D6-B8F1-3E47-2403F3B40779"
		},
		{
			"etask.entity": "sc016430",
			"id": "106F1FBF-B24A-3264-6280-AE0F2A34808E"
		},
		{
			"etask.entity": "sc016431",
			"id": "B4EBC4FA-9F13-8793-3CD3-0D4F5CCEF10A"
		},
		{
			"etask.entity": "sc016432",
			"id": "88502E9A-B33F-139F-631D-79199DD28FC2"
		},
		{
			"etask.entity": "sc016434",
			"id": "B66627DC-78AE-A2A2-E476-DD75441036B2"
		},
		{
			"etask.entity": "sc016435",
			"id": "DC4C3CC7-F583-FBE2-4957-90F775C71027"
		},
		{
			"etask.entity": "sc016436",
			"id": "41D9E398-9475-C372-AAD6-B125037313A2"
		},
		{
			"etask.entity": "sc016437",
			"id": "E9E3EF08-833B-A607-7F50-B9735164F0F0"
		},
		{
			"etask.entity": "sc016439",
			"id": "C1345BD0-5391-4D62-E987-75FC914CB89D"
		},
		{
			"etask.entity": "sc023581",
			"id": "E11EB2E6-A208-B33C-7F79-D390B9AFFC9F"
		},
		{
			"etask.entity": "sc016441",
			"id": "9AA40234-5290-BC01-9AE5-0DD9EF347C9B"
		},
		{
			"etask.entity": "sc016442",
			"id": "4B1F5E61-1998-EED6-9956-65A27BB4E6B6"
		},
		{
			"etask.entity": "sc016443",
			"id": "0BEA9A2C-400C-CDF7-DDBD-96E134D2BB13"
		},
		{
			"etask.entity": "sc016444",
			"id": "A6284BFE-0862-00FC-808E-871FA2613158"
		},
		{
			"etask.entity": "sc016446",
			"id": "AB3F5D7E-A997-A8FE-B35D-7BB599BAD933"
		},
		{
			"etask.entity": "sc016447",
			"id": "9EA70542-5168-DAFE-E3AD-D75B1527940C"
		},
		{
			"etask.entity": "sc016448",
			"id": "625AB1D3-1DA4-4D97-53B2-293ADFAA64CD"
		},
		{
			"etask.entity": "sc016449",
			"id": "1C3AD652-F27D-49BA-462B-AFA800AAA98E"
		},
		{
			"etask.entity": "sc016451",
			"id": "9698813B-2745-8EFC-3D26-F8DB4C172B6C"
		},
		{
			"etask.entity": "sc016452",
			"id": "785C67B8-37D0-EF5C-FCB8-5D092CC781F4"
		},
		{
			"etask.entity": "sc016453",
			"id": "BB17E5C2-1A76-4F53-251A-9790D147B18C"
		},
		{
			"etask.entity": "sc016454",
			"id": "7C277620-521F-A5C0-8436-2E6084D4248F"
		},
		{
			"etask.entity": "sc016456",
			"id": "11CCDE7C-E14F-7CFF-FA71-3D7F054D646B"
		},
		{
			"etask.entity": "sc016457",
			"id": "D3ECD486-9DA5-0D73-DBD9-DA4811E00DFF"
		},
		{
			"etask.entity": "sc016458",
			"id": "41014205-7EA1-8A4E-A430-8B5A3D03591E"
		},
		{
			"etask.entity": "sc016459",
			"id": "489B8FDC-94A3-CA14-378F-6FBC6A348DE1"
		},
		{
			"etask.entity": "sc016461",
			"id": "55CB5E68-9269-7B44-2616-1309DCCF6FB1"
		},
		{
			"etask.entity": "sc013276",
			"id": "3D517EB2-D654-E694-9771-277DDF960EB7"
		},
		{
			"etask.entity": "sc013281",
			"id": "A7499232-7760-FA30-4F65-C7136E75FA95"
		},
		{
			"etask.entity": "sc013286",
			"id": "09C357AE-35C3-7ED9-E671-2ECF8893CA26"
		},
		{
			"etask.entity": "sc013291",
			"id": "A5CE4926-E71C-E02C-21E2-4C3618C45FB6"
		},
		{
			"etask.entity": "sc013296",
			"id": "56AE9CB6-6E13-1025-FBC4-C6E463C4C19D"
		},
		{
			"etask.entity": "sc013298",
			"id": "CE1BE02F-B2BE-5F72-2513-DD0D590824F6"
		},
		{
			"etask.entity": "sc013303",
			"id": "5743B6AA-B7C9-A8CD-4BED-C03E51DCA448"
		},
		{
			"etask.entity": "sc013308",
			"id": "B8030AA7-0A28-E377-681C-1D30E4AEFD58"
		},
		{
			"etask.entity": "sc013313",
			"id": "EB393361-5E3B-D188-BAE6-6C52C4F1E672"
		},
		{
			"etask.entity": "sc013318",
			"id": "E3673757-0C18-2208-E529-CD51215A0C99"
		},
		{
			"etask.entity": "sc013320",
			"id": "85751CA8-575E-DBB6-EED4-908E14F89C8C"
		},
		{
			"etask.entity": "sc013325",
			"id": "67C388CD-CB6C-4C24-461B-860E519C64DA"
		},
		{
			"etask.entity": "sc013330",
			"id": "109A860C-E84D-43A6-FD21-08336B0E624A"
		},
		{
			"etask.entity": "sc013335",
			"id": "5EB4E6C5-044B-CE63-7AD8-317753B8E831"
		},
		{
			"etask.entity": "sc013340",
			"id": "2643EF2B-F68F-1AEC-6D3D-8ACAE0029DCB"
		},
		{
			"etask.entity": "sc013342",
			"id": "BCD27F9E-A78C-B78E-24ED-3C646BC1C81A"
		},
		{
			"etask.entity": "sc013347",
			"id": "CE7B18F6-FE3B-B6C5-15F7-0D27146DA71D"
		},
		{
			"etask.entity": "sc013352",
			"id": "69F95FAB-A575-9904-3DE8-E4AE07B2E542"
		},
		{
			"etask.entity": "sc023582",
			"id": "9DEC9B42-F536-12A8-C169-073026C213F0"
		},
		{
			"etask.entity": "sc016463",
			"id": "DD394EF2-C2ED-EDD0-9541-EDBDB025307C"
		},
		{
			"etask.entity": "sc016464",
			"id": "CE9E75B9-0D39-7DF4-3EF0-BBAB849A0D27"
		},
		{
			"etask.entity": "sc016465",
			"id": "BBDDA28E-61C3-743A-47B3-5298D634075D"
		},
		{
			"etask.entity": "sc016466",
			"id": "74EAC8D7-BBA4-1DE6-2DA1-5FEF36B12BCD"
		},
		{
			"etask.entity": "sc016468",
			"id": "939268FE-E6A6-A9D3-0DD7-4D775C077326"
		},
		{
			"etask.entity": "sc016469",
			"id": "A45671E2-B0DE-F8F4-8BDE-4589E971B9BE"
		},
		{
			"etask.entity": "sc016470",
			"id": "7DFF8745-5238-4435-B75B-56E6F6F0033A"
		},
		{
			"etask.entity": "sc016471",
			"id": "B8D0EC0D-5131-2801-ED70-E115001C73E0"
		},
		{
			"etask.entity": "sc016473",
			"id": "2A3C4B53-66F2-DAF6-6465-C10AFC8606D7"
		},
		{
			"etask.entity": "sc016474",
			"id": "B9257924-4290-E999-EA91-5AAC06B6E856"
		},
		{
			"etask.entity": "sc016475",
			"id": "59798BE6-C907-8D36-7373-594E5CA66E7A"
		},
		{
			"etask.entity": "sc016476",
			"id": "3A897BD9-DA10-B1A2-EB7A-0218F3A6E415"
		},
		{
			"etask.entity": "sc016478",
			"id": "63B4748D-1010-F2FC-A96A-18D612FFB64C"
		},
		{
			"etask.entity": "sc016479",
			"id": "E78D03DA-1272-8AAD-D440-B054B041E694"
		},
		{
			"etask.entity": "sc016480",
			"id": "9D69F20C-AD5F-F40F-BD63-BB2DFFD2BAFD"
		},
		{
			"etask.entity": "sc016481",
			"id": "8C7580E3-8238-6B87-8EEA-3A4D052C33B6"
		},
		{
			"etask.entity": "sc016483",
			"id": "4BE5AE1C-4089-5776-E217-3861EFCE9C17"
		},
		{
			"etask.entity": "sc023583",
			"id": "16B118E4-1939-2923-A7D8-7936D1EF775A"
		},
		{
			"etask.entity": "sc016485",
			"id": "3200F270-8B95-620C-C646-4615ACF11647"
		},
		{
			"etask.entity": "sc016486",
			"id": "861D6FC4-A9E8-0DBC-745E-39B22AF3476A"
		},
		{
			"etask.entity": "sc016487",
			"id": "7E2288A8-FCE3-062E-E314-8F0E977942D1"
		},
		{
			"etask.entity": "sc016488",
			"id": "5576D451-AC36-95F3-27A8-BD7A58EAAF8A"
		},
		{
			"etask.entity": "sc016490",
			"id": "0B3F48EE-4941-CA21-258E-F7CFA7B662E1"
		},
		{
			"etask.entity": "sc016491",
			"id": "1A074977-DFA7-506B-E509-1E0A672BD67A"
		},
		{
			"etask.entity": "sc016492",
			"id": "065DC2A8-A0AA-AE19-5C65-A892539E1509"
		},
		{
			"etask.entity": "sc016493",
			"id": "3C691DCD-C210-5BEE-14A6-0E061853522A"
		},
		{
			"etask.entity": "sc016495",
			"id": "707D4D1F-2AB2-5B1E-3883-96E18834D6E4"
		},
		{
			"etask.entity": "sc016496",
			"id": "801F2FB1-F8A5-3574-8290-AA4D3617FB80"
		},
		{
			"etask.entity": "sc016497",
			"id": "E7446DB7-E343-537C-0BE2-575E4CDB2A7D"
		},
		{
			"etask.entity": "sc016498",
			"id": "FEC0380C-76B0-3CC6-5343-3C264BC616D0"
		},
		{
			"etask.entity": "sc016500",
			"id": "BDCEDFAD-819D-E0ED-65CB-C5B7BF2B4E4A"
		},
		{
			"etask.entity": "sc016501",
			"id": "FEC457D1-F2AF-CFFF-21C2-0CE793E7B148"
		},
		{
			"etask.entity": "sc016502",
			"id": "C0343E27-3DA7-C95B-F199-65DB3D34CE4E"
		},
		{
			"etask.entity": "sc016503",
			"id": "BDF84258-D1FA-F063-FFA0-2D92D5860EEA"
		},
		{
			"etask.entity": "sc016505",
			"id": "361F06D2-5FCF-9CA7-EA38-D1C63131A277"
		},
		{
			"etask.entity": "sc023584",
			"id": "078BE960-A683-D951-5F43-BAD123B629B4"
		},
		{
			"etask.entity": "sc016507",
			"id": "124E6B89-3FD9-F9B5-23F8-A3ED878ECD22"
		},
		{
			"etask.entity": "sc016508",
			"id": "65BF3D84-5A90-B6B1-9BAC-884CC3B05B16"
		},
		{
			"etask.entity": "sc016509",
			"id": "38B3B0B8-EC69-5D78-D15B-2C4F3CFDD0B1"
		},
		{
			"etask.entity": "sc016510",
			"id": "7A166B0F-826C-60B3-E3BD-875B3D10C06B"
		},
		{
			"etask.entity": "sc016512",
			"id": "19E22051-F3D3-44B9-8660-6390A278B102"
		},
		{
			"etask.entity": "sc016513",
			"id": "1EAEF4EC-8AA4-C741-843C-17061AFE111C"
		},
		{
			"etask.entity": "sc016514",
			"id": "ED818E2A-48AF-D00D-CC7D-1E249DA6219A"
		},
		{
			"etask.entity": "sc016515",
			"id": "9ED0751B-6938-16D6-4A64-191FE823AA81"
		},
		{
			"etask.entity": "sc016517",
			"id": "33A3A8C5-0BE9-C273-FE5E-1009C33C1687"
		},
		{
			"etask.entity": "sc016518",
			"id": "F3633355-DA9F-9C57-37DB-FB7DFE235056"
		},
		{
			"etask.entity": "sc016519",
			"id": "F0231664-3DB2-AB7D-8895-CDB697EF0C70"
		},
		{
			"etask.entity": "sc016520",
			"id": "E4F4BD76-59E2-8AD1-2F2D-73BA51FAD6FF"
		},
		{
			"etask.entity": "sc016522",
			"id": "39598E3D-E32D-A253-AC08-A47028D62447"
		},
		{
			"etask.entity": "sc016523",
			"id": "B2843320-DAD5-2C01-C7E1-4F28B2E35614"
		},
		{
			"etask.entity": "sc016524",
			"id": "118AB5B3-E04C-DACF-82EF-4B7D8533BE45"
		},
		{
			"etask.entity": "sc016525",
			"id": "36A0F334-6C72-D401-EBCD-C0C14FBD47C8"
		},
		{
			"etask.entity": "sc016527",
			"id": "6BC3E089-72A2-A0A1-F768-F368F09B5F65"
		},
		{
			"etask.entity": "sc013357",
			"id": "38805BC9-9D17-AAF6-55D8-5B0EEE4FF5F7"
		},
		{
			"etask.entity": "sc013362",
			"id": "0A11A4BA-95C4-9ABD-E467-256AF1CA96CE"
		},
		{
			"etask.entity": "sc013364",
			"id": "B575C340-7381-EC8C-C31A-78B04DED5DDA"
		},
		{
			"etask.entity": "sc013369",
			"id": "F3DB7DA6-F721-AD2D-B2C1-D04EB259B664"
		},
		{
			"etask.entity": "sc013374",
			"id": "A9808CE9-1DC0-F705-DF75-E3A976E92AC0"
		},
		{
			"etask.entity": "sc013379",
			"id": "1722EAE6-8CA9-7A0F-35B9-BD9A89B23E29"
		},
		{
			"etask.entity": "sc013384",
			"id": "261B4AA1-FEA3-9032-45AD-4A4CD9482CDE"
		},
		{
			"etask.entity": "sc013386",
			"id": "C578E11C-5507-A066-C8A4-601C05C2370C"
		},
		{
			"etask.entity": "sc013391",
			"id": "2678FD5B-F945-5CAF-272A-3B00F6FF60F6"
		},
		{
			"etask.entity": "sc013396",
			"id": "569E74D3-D82F-BF56-2FC7-AA4756712D6B"
		},
		{
			"etask.entity": "sc013401",
			"id": "4138A97C-AF0F-6C88-4288-199DC43088EB"
		},
		{
			"etask.entity": "sc013406",
			"id": "34E8E9FA-6AF5-4669-EE51-3959C44C49AC"
		},
		{
			"etask.entity": "sc013408",
			"id": "C9537808-4205-05DF-8325-E7983F17F12F"
		},
		{
			"etask.entity": "sc013413",
			"id": "C323BD4A-C338-7E0E-D6F2-B148791F9F04"
		},
		{
			"etask.entity": "sc013418",
			"id": "F1A4EFB1-6F9D-9C4F-07E1-8D90E5E2750B"
		},
		{
			"etask.entity": "sc013423",
			"id": "7C3213B2-B95D-CC4D-BA37-8ACE388DB266"
		},
		{
			"etask.entity": "sc013428",
			"id": "E4405FC0-85E7-8627-02AA-2E915A4C1A96"
		},
		{
			"etask.entity": "sc013430",
			"id": "AFF2E089-8280-5657-0111-568E5C05C6F8"
		},
		{
			"etask.entity": "sc023585",
			"id": "5A2CB4EA-817F-E8B8-D17D-E3DF76536F8A"
		},
		{
			"etask.entity": "sc016529",
			"id": "7514FEAA-B37A-28D0-E549-045F4DAD9152"
		},
		{
			"etask.entity": "sc016530",
			"id": "87DF1D62-3EE5-7A7F-B0A9-F6FFC6894667"
		},
		{
			"etask.entity": "sc016531",
			"id": "7876B1D6-5891-243E-C30E-5F8D757D72BB"
		},
		{
			"etask.entity": "sc016532",
			"id": "186D70B8-AFDA-BD10-7F82-A4D51A7DCA88"
		},
		{
			"etask.entity": "sc016534",
			"id": "E479468D-92DE-6AA7-A93A-39B104EFAAD3"
		},
		{
			"etask.entity": "sc016535",
			"id": "AE15016B-33E5-D977-86C0-FAB88D0AFD6C"
		},
		{
			"etask.entity": "sc016536",
			"id": "745F1577-529E-B60D-6E4B-379EAAAE68B6"
		},
		{
			"etask.entity": "sc016537",
			"id": "5C9ECE3A-7415-AF18-1366-D9CBD0B8D146"
		},
		{
			"etask.entity": "sc016539",
			"id": "B3471F0B-AADD-D873-3E2D-5DCBE55B561C"
		},
		{
			"etask.entity": "sc016540",
			"id": "D351D62D-851E-9F61-D01D-B059654E69ED"
		},
		{
			"etask.entity": "sc016541",
			"id": "4669D51B-B9A2-8CE1-4916-708B3B2CC4DD"
		},
		{
			"etask.entity": "sc016542",
			"id": "264A2B8D-29F8-E168-A3D1-44F2AC721052"
		},
		{
			"etask.entity": "sc016544",
			"id": "7CBA57EA-5DED-D9DB-F6CA-84184483E717"
		},
		{
			"etask.entity": "sc016545",
			"id": "9A577DBE-FE7F-CDF2-4906-020CF1B3AA0B"
		},
		{
			"etask.entity": "sc016546",
			"id": "1C536471-BDE7-36C2-DA32-F737455EE0E7"
		},
		{
			"etask.entity": "sc016547",
			"id": "44121924-9535-9C25-50E5-937730C8E297"
		},
		{
			"etask.entity": "sc016549",
			"id": "2514926A-3279-3188-61F8-55C8A6792ECD"
		},
		{
			"etask.entity": "sc023586",
			"id": "141A8C4B-8399-DF3E-0D3E-D940732DE17E"
		},
		{
			"etask.entity": "sc016551",
			"id": "CF88319F-F007-7591-0F6D-E18502EBC39A"
		},
		{
			"etask.entity": "sc016552",
			"id": "C29B8C88-683E-217A-33CA-2F4ECF637678"
		},
		{
			"etask.entity": "sc016553",
			"id": "71D0BE16-2E1C-FC82-3C3F-715DF3D87EF7"
		},
		{
			"etask.entity": "sc016554",
			"id": "A3006381-2937-0734-8257-45DD3B1316E5"
		},
		{
			"etask.entity": "sc016556",
			"id": "5C25F114-91F2-8561-C428-F94809E5A2CB"
		},
		{
			"etask.entity": "sc016557",
			"id": "F737D0E2-203A-9568-877D-8C44DE7D0203"
		},
		{
			"etask.entity": "sc016558",
			"id": "81A5F7E1-DEDC-7AF4-80DA-52BA19C26216"
		},
		{
			"etask.entity": "sc016559",
			"id": "89B19DD2-F867-7C5A-C256-06EE8AEB8186"
		},
		{
			"etask.entity": "sc016561",
			"id": "9BBBEC96-ED17-18A4-D817-9F386FAA2144"
		},
		{
			"etask.entity": "sc016562",
			"id": "FEDB6C4B-F54F-04DC-35ED-EBD8302FC712"
		},
		{
			"etask.entity": "sc016563",
			"id": "8CFBE0CA-F068-D35D-8E9C-83A307956E61"
		},
		{
			"etask.entity": "sc016564",
			"id": "5EB1AD98-C3D1-5D07-5933-9B38FFD088F3"
		},
		{
			"etask.entity": "sc016566",
			"id": "E981CA72-694B-23C6-6061-0270A47C1ABF"
		},
		{
			"etask.entity": "sc016567",
			"id": "BB760FE5-1503-BD0E-B889-7028215A10AC"
		},
		{
			"etask.entity": "sc016568",
			"id": "7AC75F27-241A-8B76-F0E0-77A4FAFE2FA1"
		},
		{
			"etask.entity": "sc016569",
			"id": "5DBAB84C-AEE2-5EB9-1D3A-F5F350980AA0"
		},
		{
			"etask.entity": "sc016571",
			"id": "A10E64C6-8767-714C-A3F4-D3FA1D1A9631"
		},
		{
			"etask.entity": "sc023587",
			"id": "FFCC281D-FDA8-0145-76D7-4946E867B06D"
		},
		{
			"etask.entity": "sc016573",
			"id": "0F7A5E5B-FCA4-671D-6A2B-58217F0B9BCE"
		},
		{
			"etask.entity": "sc016574",
			"id": "D74E77FD-38AD-FDBB-090B-06970E3E392C"
		},
		{
			"etask.entity": "sc016575",
			"id": "3746BAE8-8655-D8E6-C4C9-C2C23F6C7D6B"
		},
		{
			"etask.entity": "sc016576",
			"id": "37D35BD7-1AE9-2E6F-6403-AE75445FFDCF"
		},
		{
			"etask.entity": "sc016578",
			"id": "57B31AB1-4A79-6D3D-9B1F-462D513DC36E"
		},
		{
			"etask.entity": "sc016579",
			"id": "90D3EC79-986A-9856-CF1E-362138F2FE5B"
		},
		{
			"etask.entity": "sc016580",
			"id": "856DD142-89C5-436C-3C92-716D326136B1"
		},
		{
			"etask.entity": "sc016581",
			"id": "87306FF7-C3AF-5CA5-783A-BB837C31F34D"
		},
		{
			"etask.entity": "sc016583",
			"id": "2679BD3B-1846-2A52-3385-28073F45E51E"
		},
		{
			"etask.entity": "sc016584",
			"id": "7900ED68-E065-49CD-DC06-54BDADF87294"
		},
		{
			"etask.entity": "sc016585",
			"id": "F2ECC3D0-7BDD-021B-24AC-33B48C0F6F5F"
		},
		{
			"etask.entity": "sc016586",
			"id": "88A2C633-6396-5267-67EA-A7550C73170B"
		},
		{
			"etask.entity": "sc016588",
			"id": "384912C1-81FB-CC2D-0282-AB703CDFB988"
		},
		{
			"etask.entity": "sc016589",
			"id": "3A1BD399-671A-7CDE-7F6E-1461E9D186CD"
		},
		{
			"etask.entity": "sc016590",
			"id": "AE6DE742-81F1-1167-5ED7-4F0320384433"
		},
		{
			"etask.entity": "sc016591",
			"id": "B018D93B-C1A4-855F-6DD6-F8E41D48719E"
		},
		{
			"etask.entity": "sc016593",
			"id": "4E4090F2-3948-6382-B700-3C5F627CBB39"
		},
		{
			"etask.entity": "sc023588",
			"id": "9B2029DB-0FFB-4188-3F23-B8301040C55B"
		},
		{
			"etask.entity": "sc016595",
			"id": "EFB8566A-387D-6E76-A15E-FE450CA5C923"
		},
		{
			"etask.entity": "sc016596",
			"id": "80273DEA-7A0A-DE89-5222-D6126A784C7C"
		},
		{
			"etask.entity": "sc016597",
			"id": "03BAD855-D412-E6F8-9390-5A60BC07AE9C"
		},
		{
			"etask.entity": "sc016598",
			"id": "F47BB2E2-4ADA-3300-851A-8E7229526DA2"
		},
		{
			"etask.entity": "sc016600",
			"id": "8C4D4E0F-C0D0-C21E-EA72-7E388EA59B35"
		},
		{
			"etask.entity": "sc016601",
			"id": "6D16F275-983E-C9F6-C192-1BE27E139C6A"
		},
		{
			"etask.entity": "sc016602",
			"id": "8A848B51-F1AD-8DA6-4FD2-B7B0079B6D09"
		},
		{
			"etask.entity": "sc016603",
			"id": "07A2155D-328D-ABB8-D4FA-BA6DFD48B40E"
		},
		{
			"etask.entity": "sc016605",
			"id": "647C2BAE-F142-B6C9-E7E0-FFA84F479B0B"
		},
		{
			"etask.entity": "sc016606",
			"id": "E126D095-FDA1-290E-8CD6-150920CE37C4"
		},
		{
			"etask.entity": "sc016607",
			"id": "3CF33226-A17F-BDFF-1EC2-BEE5A8D22A0D"
		},
		{
			"etask.entity": "sc016608",
			"id": "5F21DAC1-5C07-09F5-D3BC-650970A3B7FC"
		},
		{
			"etask.entity": "sc016610",
			"id": "DABA3362-73A6-8B3E-0C87-5C6682D6A162"
		},
		{
			"etask.entity": "sc016611",
			"id": "2A648A15-964E-CCE4-A476-E34E37095F93"
		},
		{
			"etask.entity": "sc016612",
			"id": "B04F4E8C-89B1-9955-44E4-C43202BF9DCE"
		},
		{
			"etask.entity": "sc016613",
			"id": "CE9D02CA-9EDB-2EAC-6BFD-810D68F24A4B"
		},
		{
			"etask.entity": "sc016615",
			"id": "651A5C39-398B-C22A-9470-35B2D01FA4B8"
		},
		{
			"etask.entity": "sc013435",
			"id": "A9B03C61-FACF-91E5-427C-EEB6C924535C"
		},
		{
			"etask.entity": "sc013440",
			"id": "D368396F-F57E-1A69-BF93-F94C28744225"
		},
		{
			"etask.entity": "sc013445",
			"id": "3E69F3B8-4D22-5134-DD51-32F03C1ED433"
		},
		{
			"etask.entity": "sc013450",
			"id": "1D024E9F-0853-E51B-05C4-E39DF9A98462"
		},
		{
			"etask.entity": "sc013452",
			"id": "0F6DCE13-61A4-6449-856B-4CD9CB411B49"
		},
		{
			"etask.entity": "sc013457",
			"id": "5CAF1D6C-51B6-D69C-7A8D-4E2AFD02D169"
		},
		{
			"etask.entity": "sc013462",
			"id": "8B6AAE38-244E-950D-7B4F-4BCD1F2548F3"
		},
		{
			"etask.entity": "sc013467",
			"id": "AD51A263-794F-24B7-D420-3F5D00C2098B"
		},
		{
			"etask.entity": "sc013472",
			"id": "E9D523F1-D1D6-C709-84AE-1A224FD6D626"
		},
		{
			"etask.entity": "sc013474",
			"id": "984DA9AD-1D46-04E7-FAEB-EF06B6E32E45"
		},
		{
			"etask.entity": "sc013479",
			"id": "F7375E76-7171-12FD-B940-E7099E8A22EA"
		},
		{
			"etask.entity": "sc013484",
			"id": "2767EE05-6043-F91A-A000-28DB75C46F3C"
		},
		{
			"etask.entity": "sc013489",
			"id": "B0AFEED0-FC10-8DAD-5F63-3E80202F01B8"
		},
		{
			"etask.entity": "sc013494",
			"id": "8EB89817-B3DA-2E90-4116-6E8E5414C60E"
		},
		{
			"etask.entity": "sc013496",
			"id": "D170E244-52CD-641F-1725-B3A864203150"
		},
		{
			"etask.entity": "sc013501",
			"id": "8F71DAE1-152F-06AC-0DE9-7681343E86D8"
		},
		{
			"etask.entity": "sc013506",
			"id": "96AF7BD6-7208-B3AF-D12E-3D19EEC4CF07"
		},
		{
			"etask.entity": "sc013511",
			"id": "DB1C9519-D049-28AC-C5BB-219F5E351485"
		},
		{
			"etask.entity": "sc023589",
			"id": "48F4D549-478E-779A-2E3C-3F64E7B1FDAA"
		},
		{
			"etask.entity": "sc016617",
			"id": "F13C8886-C780-D411-246B-6C78A4B7A73F"
		},
		{
			"etask.entity": "sc016618",
			"id": "DACF3843-9200-F0A1-B27F-7879B0EF00A3"
		},
		{
			"etask.entity": "sc016619",
			"id": "C160DA3C-1D60-2D8C-08B5-592717DDC286"
		},
		{
			"etask.entity": "sc016620",
			"id": "DECDA2AF-14B9-0848-E59B-DD488ABFFFDB"
		},
		{
			"etask.entity": "sc016622",
			"id": "2C43EEC8-B43E-12F9-0B23-4E23A91BB86A"
		},
		{
			"etask.entity": "sc016623",
			"id": "B02A2400-A906-8604-61C1-7D7243E2B112"
		},
		{
			"etask.entity": "sc016624",
			"id": "45F8EFEA-E713-F666-2B58-29073BD3ACF1"
		},
		{
			"etask.entity": "sc016625",
			"id": "4687FBD4-8128-579A-09EF-46DE02F0F158"
		},
		{
			"etask.entity": "sc016627",
			"id": "A99104FB-F2B4-3775-A715-A4C6899B82A5"
		},
		{
			"etask.entity": "sc016628",
			"id": "52A2AC76-8529-CF0C-9437-357F0AA70F5F"
		},
		{
			"etask.entity": "sc016629",
			"id": "5FE80F9A-AF5D-1242-27FA-17C9B12672EF"
		},
		{
			"etask.entity": "sc016630",
			"id": "1E12CFC9-A2B9-1FE2-3FB6-2113FB25F1F6"
		},
		{
			"etask.entity": "sc016632",
			"id": "04743DAA-6FFC-7B99-2A26-D4ADD71D0AAF"
		},
		{
			"etask.entity": "sc016633",
			"id": "8D302414-A8EE-FAEA-29E4-5A4212DB33BA"
		},
		{
			"etask.entity": "sc016634",
			"id": "075D4F1D-8B20-75D9-7766-D5F122D3F231"
		},
		{
			"etask.entity": "sc016635",
			"id": "7D70948C-B28B-4FC0-F312-510A9A943A00"
		},
		{
			"etask.entity": "sc016637",
			"id": "5E70F31B-DF1A-4122-9B25-C65F173A9510"
		},
		{
			"etask.entity": "sc023590",
			"id": "D71107EA-589D-31BA-018E-4DDE50F34AB3"
		},
		{
			"etask.entity": "sc016639",
			"id": "35966130-8481-34D7-E98E-9D671F6F38F6"
		},
		{
			"etask.entity": "sc016640",
			"id": "5FC0DDA0-FA79-117B-D2D0-45E1C6ABF5D9"
		},
		{
			"etask.entity": "sc016641",
			"id": "0DE93B3B-6585-2642-9346-39C95CD1FA71"
		},
		{
			"etask.entity": "sc016642",
			"id": "0A130D92-B5C0-4898-203E-13DE4F7FFDA0"
		},
		{
			"etask.entity": "sc016644",
			"id": "6B12DFA3-579C-AD15-B213-6FBBBC2D3360"
		},
		{
			"etask.entity": "sc016645",
			"id": "7696A3A4-15F3-56B6-00DF-882577134600"
		},
		{
			"etask.entity": "sc016646",
			"id": "D5CE2A66-8EA7-505D-873C-BD00BDB2960D"
		},
		{
			"etask.entity": "sc016647",
			"id": "6A787837-0023-FD29-3886-C87050FAECFE"
		},
		{
			"etask.entity": "sc016649",
			"id": "EC3F837B-4256-03AF-B6E7-239F43020E5E"
		},
		{
			"etask.entity": "sc016650",
			"id": "D45BF885-AA6D-1A25-56BD-1739D94C0624"
		},
		{
			"etask.entity": "sc016651",
			"id": "7EEA5C52-33C1-8FBF-CD57-6A5C3AABD222"
		},
		{
			"etask.entity": "sc016652",
			"id": "BD3A51C4-B2D4-5166-BB23-82ADEACC48F6"
		},
		{
			"etask.entity": "sc016654",
			"id": "16320630-4E38-049C-4769-9AE9C448113E"
		},
		{
			"etask.entity": "sc016655",
			"id": "A970A049-A82A-3B3F-221B-99E325DC87B1"
		},
		{
			"etask.entity": "sc016656",
			"id": "D3D6F2EB-F11E-00F8-3066-FEA5B71B0327"
		},
		{
			"etask.entity": "sc016657",
			"id": "1DC8BD39-AD56-823A-2FDA-B34D848DA152"
		},
		{
			"etask.entity": "sc016659",
			"id": "7896A240-85AC-FAA5-2984-B4652941799E"
		},
		{
			"etask.entity": "sc023591",
			"id": "E7B91D5F-FE18-C4C5-D6AD-F777033F0F96"
		},
		{
			"etask.entity": "sc016661",
			"id": "C91161D5-AF9A-A378-CB97-055E56CC8F2A"
		},
		{
			"etask.entity": "sc016662",
			"id": "647E74EF-4AEC-43CD-E652-98F0676384F5"
		},
		{
			"etask.entity": "sc016663",
			"id": "729B6786-5322-B7AF-F652-48D1DFE4148D"
		},
		{
			"etask.entity": "sc016664",
			"id": "B1759973-EBEB-A4C3-5BD5-3ED9E00DDA69"
		},
		{
			"etask.entity": "sc016666",
			"id": "7E527A9A-1A7E-21ED-EE5A-D79C74F35E10"
		},
		{
			"etask.entity": "sc016667",
			"id": "73683D03-180D-3FE0-7C84-905100752EC0"
		},
		{
			"etask.entity": "sc016668",
			"id": "1168951E-3187-9BF5-26B1-E22CA6D4C0FD"
		},
		{
			"etask.entity": "sc016669",
			"id": "2718C50D-533C-AF01-1C4F-08EF415D3164"
		},
		{
			"etask.entity": "sc016671",
			"id": "D71EA28D-7997-61D8-DA86-2CE0883CD5F3"
		},
		{
			"etask.entity": "sc016672",
			"id": "C91C4E28-8237-1943-83EF-BBAE5F94AFC9"
		},
		{
			"etask.entity": "sc016673",
			"id": "F498F75C-29F3-9AF7-C880-C77DE3AC4998"
		},
		{
			"etask.entity": "sc016674",
			"id": "3852D456-8893-FC4D-4776-3705DDAB9AAD"
		},
		{
			"etask.entity": "sc016676",
			"id": "858CAA49-05EB-1819-9844-437EF6E4CD23"
		},
		{
			"etask.entity": "sc016677",
			"id": "96908B09-61D0-E5BA-6AA8-A54B583AD26C"
		},
		{
			"etask.entity": "sc016678",
			"id": "3868E93F-1070-9F64-86D3-9DE799A1F78E"
		},
		{
			"etask.entity": "sc016679",
			"id": "035DA024-A747-9FF5-A607-1E5828E050A5"
		},
		{
			"etask.entity": "sc016681",
			"id": "1350AAF5-4AD3-346A-422D-A2A958A33673"
		},
		{
			"etask.entity": "sc013516",
			"id": "8901133F-739A-BAD4-C1D1-ABED9F30EEEA"
		},
		{
			"etask.entity": "sc013518",
			"id": "4131B750-CCAF-2E99-DFBA-44D265B3F433"
		},
		{
			"etask.entity": "sc013523",
			"id": "0689CBF6-7BE7-ABDC-E6AA-5A086F6DE6E4"
		},
		{
			"etask.entity": "sc013528",
			"id": "45B7A14A-A39A-8C74-6FDE-9577F600A441"
		},
		{
			"etask.entity": "sc013533",
			"id": "9942667B-8377-2786-5FFE-28B8273A9689"
		},
		{
			"etask.entity": "sc013538",
			"id": "FA006D9A-17F8-3F57-9F88-538FF118EA3F"
		},
		{
			"etask.entity": "sc013540",
			"id": "EB04F011-99AB-5522-3FB7-179225617B21"
		},
		{
			"etask.entity": "sc013545",
			"id": "B2210479-978F-6D66-AD31-B4468EFC072D"
		},
		{
			"etask.entity": "sc013550",
			"id": "55653A8A-7671-751A-8983-4DEA1170FBEC"
		},
		{
			"etask.entity": "sc013555",
			"id": "C564184F-482A-DA33-DD7C-EBCE5745A134"
		},
		{
			"etask.entity": "sc013560",
			"id": "E550BDA0-5ACA-67D0-0EF0-AA4D494A29D0"
		},
		{
			"etask.entity": "sc013562",
			"id": "CD010620-8078-6889-DB19-86A93DE6AB36"
		},
		{
			"etask.entity": "sc013567",
			"id": "8D16DEA6-BDCB-8580-48D7-AE0337FBE031"
		},
		{
			"etask.entity": "sc013572",
			"id": "F2848116-E325-5E9C-9B88-6EF805F58626"
		},
		{
			"etask.entity": "sc013577",
			"id": "BCB9728E-97AB-0D32-DDBE-14A28811149E"
		},
		{
			"etask.entity": "sc013582",
			"id": "6BC44264-974D-A51A-F100-056ACE3F0F2F"
		},
		{
			"etask.entity": "sc013584",
			"id": "8B3AA5B2-432C-42F8-B161-1C9C21659A5F"
		},
		{
			"etask.entity": "sc013589",
			"id": "C802162C-D926-B2DA-16D0-65B31FDABB56"
		},
		{
			"etask.entity": "sc023592",
			"id": "DA282F8C-C66F-87C5-8167-4FC400633462"
		},
		{
			"etask.entity": "sc016683",
			"id": "E41B6998-4D1F-7548-75A6-9D32951B3658"
		},
		{
			"etask.entity": "sc016684",
			"id": "1361A60F-1628-EC5E-443F-C2B5533C1873"
		},
		{
			"etask.entity": "sc016685",
			"id": "4BEDC769-E43E-A56D-BB6B-1DF5DCB7AF31"
		},
		{
			"etask.entity": "sc016686",
			"id": "94E18C72-E6A0-05E8-6321-F58645279A7B"
		},
		{
			"etask.entity": "sc016688",
			"id": "73457E91-6C2F-0492-997C-16AFC62E22B7"
		},
		{
			"etask.entity": "sc016689",
			"id": "016585F8-781C-36F7-E810-7B8508EA9723"
		},
		{
			"etask.entity": "sc016690",
			"id": "D2101580-75B6-5AB8-83E6-040BE0C129C9"
		},
		{
			"etask.entity": "sc016691",
			"id": "BC299E43-0CFF-DC71-037D-9355CCE58E09"
		},
		{
			"etask.entity": "sc016693",
			"id": "E9C11759-2E15-82D6-DB3E-693FB417266E"
		},
		{
			"etask.entity": "sc016694",
			"id": "CF1D06F5-E1A2-B784-9299-1E51DC3664FC"
		},
		{
			"etask.entity": "sc016695",
			"id": "AC01DD06-C6EA-91DD-CB5F-E13164F0C21D"
		},
		{
			"etask.entity": "sc016696",
			"id": "EC3EA10B-4E7B-E59A-D71E-DAFFF95A65BA"
		},
		{
			"etask.entity": "sc016698",
			"id": "3CF8DA6A-09E0-56B8-208D-39F8CCAC6C10"
		},
		{
			"etask.entity": "sc016699",
			"id": "A05709AF-DB02-5C91-D4AD-CE3C31D753E6"
		},
		{
			"etask.entity": "sc016700",
			"id": "3C150803-677A-1AFB-0E37-F7638DA893EC"
		},
		{
			"etask.entity": "sc016701",
			"id": "2527038F-FEE4-AD2F-D0DF-1F402763C155"
		},
		{
			"etask.entity": "sc016703",
			"id": "D5135F8C-1726-7631-37AA-0430ED477DB6"
		},
		{
			"etask.entity": "sc023593",
			"id": "8D765273-25CF-357B-964E-153C8633FFC9"
		},
		{
			"etask.entity": "sc016705",
			"id": "4D536869-BCDD-50A6-E5B7-B41520E3E114"
		},
		{
			"etask.entity": "sc016706",
			"id": "783802F1-D8A6-32E0-4F7A-FCE9AE0975A6"
		},
		{
			"etask.entity": "sc016707",
			"id": "CCC6A5BD-2F86-BF9E-B8BF-DFF9F0312FB3"
		},
		{
			"etask.entity": "sc016708",
			"id": "0D21C0C0-8504-E3D2-D7FC-4E6A925FEDCE"
		},
		{
			"etask.entity": "sc016710",
			"id": "35B6F990-D2FE-BACD-EB2E-EEC6E0AC0745"
		},
		{
			"etask.entity": "sc016711",
			"id": "E0CD067E-7555-2D95-771E-95AB6554B147"
		},
		{
			"etask.entity": "sc016712",
			"id": "12F735E3-2350-50E5-B57A-C3BE10EDAE3F"
		},
		{
			"etask.entity": "sc016713",
			"id": "770473F9-6D7C-967A-08C1-8AD5DC606B5A"
		},
		{
			"etask.entity": "sc016715",
			"id": "572C2875-1366-A784-D748-3F236566B948"
		},
		{
			"etask.entity": "sc016716",
			"id": "4C4FE24A-495D-7443-E34F-07CF81FFC7BE"
		},
		{
			"etask.entity": "sc016717",
			"id": "46B79606-877A-4DCC-11BF-EB86017F3E67"
		},
		{
			"etask.entity": "sc016718",
			"id": "AA9A7E9B-E861-AEAF-6355-F64F948D22CA"
		},
		{
			"etask.entity": "sc016720",
			"id": "324D7F57-8AEB-AC56-6289-6C38397093BB"
		},
		{
			"etask.entity": "sc016721",
			"id": "A5374297-29E5-F0B0-BC33-A238E0B66CFA"
		},
		{
			"etask.entity": "sc016722",
			"id": "2D98EB3E-05B8-A3C9-15CA-3DBFF0735F47"
		},
		{
			"etask.entity": "sc016723",
			"id": "A67330EF-29D1-CFB7-EB09-ED98061CFA7D"
		},
		{
			"etask.entity": "sc016725",
			"id": "2DC317EE-7381-22B2-D5CC-7BE26D81A7D2"
		},
		{
			"etask.entity": "sc023594",
			"id": "A8C46079-047D-E71C-98C3-560756DC130B"
		},
		{
			"etask.entity": "sc016727",
			"id": "5105D9B0-36A2-16AC-4663-7BBA771585BB"
		},
		{
			"etask.entity": "sc016728",
			"id": "313FE8C8-0103-69F4-5830-F6B6C93DB249"
		},
		{
			"etask.entity": "sc016729",
			"id": "8BCC21AD-005A-0A65-6D63-666F4CE2C18E"
		},
		{
			"etask.entity": "sc016730",
			"id": "90E78761-6AD1-FCFC-6CAE-0E150779023C"
		},
		{
			"etask.entity": "sc016732",
			"id": "805AA744-AF4E-C0AE-F3A1-0F97327F0C55"
		},
		{
			"etask.entity": "sc016733",
			"id": "661BAB93-A3C5-4077-D849-2AB2778E4F87"
		},
		{
			"etask.entity": "sc016734",
			"id": "96F1157D-D198-52A4-9BBB-1B81E3550C70"
		},
		{
			"etask.entity": "sc016735",
			"id": "E9C91269-7082-5F7F-9FC7-CE1D2993E25F"
		},
		{
			"etask.entity": "sc016737",
			"id": "16D732E7-C5F0-ED3F-5755-81F6F9911B1B"
		},
		{
			"etask.entity": "sc016738",
			"id": "0A07FC0A-0114-13DE-354D-A78BD5766D47"
		},
		{
			"etask.entity": "sc016739",
			"id": "3950EA0F-D231-A092-99F0-39CCBAEAEA84"
		},
		{
			"etask.entity": "sc016740",
			"id": "0D30F8E3-777E-85C8-8355-E2760D7FC1F6"
		},
		{
			"etask.entity": "sc016742",
			"id": "EA3FB827-2014-A9D1-3F8E-DB67D90F6542"
		},
		{
			"etask.entity": "sc016743",
			"id": "DBAEF91E-7820-8BB4-DD31-385C24B3E2E6"
		},
		{
			"etask.entity": "sc016744",
			"id": "5F5071D4-98A4-6029-CF55-3D23F53C2EBD"
		},
		{
			"etask.entity": "sc016745",
			"id": "D1F85BC4-E1B6-DDED-F17F-30B4AAA07F99"
		},
		{
			"etask.entity": "sc016747",
			"id": "7A38C9FD-FA05-F875-BAC8-F91FE6F2281A"
		},
		{
			"etask.entity": "sc023595",
			"id": "891C30F1-1241-9012-5B83-758D93D107E1"
		},
		{
			"etask.entity": "sc016749",
			"id": "61B6C636-71EC-00A6-79B0-0A7C314F7B85"
		},
		{
			"etask.entity": "sc016750",
			"id": "3CDB47EB-2A07-7F9C-EB4D-5337E17ACF32"
		},
		{
			"etask.entity": "sc016751",
			"id": "8A217265-F005-101F-A5BA-41507B0236AC"
		},
		{
			"etask.entity": "sc016752",
			"id": "60825302-91B6-9C53-0620-06C28D10CA7A"
		},
		{
			"etask.entity": "sc016754",
			"id": "ADAE9A8D-6D73-2CE4-4D6E-AEC9800FB2D1"
		},
		{
			"etask.entity": "sc016755",
			"id": "38B5DC9A-EA26-FFC6-9621-2B45D9F24E17"
		},
		{
			"etask.entity": "sc016756",
			"id": "DB246D68-7EC6-C425-B911-88BA9DE1E98E"
		},
		{
			"etask.entity": "sc016757",
			"id": "F7FA2183-A170-B991-5150-0F503C9EFF14"
		},
		{
			"etask.entity": "sc016759",
			"id": "A368DA43-554A-1878-95F7-962ABD97F958"
		},
		{
			"etask.entity": "sc016760",
			"id": "4BF43B29-A0BD-0690-AAFA-D3209DDBADA0"
		},
		{
			"etask.entity": "sc016761",
			"id": "F72BEF56-D893-9E89-6F42-69B2865DE82E"
		},
		{
			"etask.entity": "sc016762",
			"id": "AC07488C-1DE7-7713-5C35-65DCD30B8C69"
		},
		{
			"etask.entity": "sc016764",
			"id": "36D17308-48F7-1428-EC98-3FADE2D0185E"
		},
		{
			"etask.entity": "sc016765",
			"id": "98AFDCC4-0568-1967-D954-0DA6A00FADC5"
		},
		{
			"etask.entity": "sc016766",
			"id": "B4D3BBC3-5ED4-70A1-AF22-E91905AD2D9A"
		},
		{
			"etask.entity": "sc016767",
			"id": "0F660AA2-B42C-456F-C707-7FBD6D82409B"
		},
		{
			"etask.entity": "sc016769",
			"id": "66E59B0A-E889-A4E9-71C6-6A3E5C442A7E"
		},
		{
			"etask.entity": "sc013594",
			"id": "910197ED-8CC5-A72B-15CA-339835E2AB83"
		},
		{
			"etask.entity": "sc013599",
			"id": "78105A95-08CB-7B75-6CB1-E6DB137CA425"
		},
		{
			"etask.entity": "sc013604",
			"id": "187AB8FA-BBDA-32D0-6BBB-13BB2C132E4A"
		},
		{
			"etask.entity": "sc013606",
			"id": "8BC64BBD-562B-A08D-9101-04B67BD49F31"
		},
		{
			"etask.entity": "sc013611",
			"id": "E2EF79EB-2487-96EF-7E06-BAE1B8EE459F"
		},
		{
			"etask.entity": "sc013616",
			"id": "266B3152-0C54-5BEA-039E-C4244CF95DFD"
		},
		{
			"etask.entity": "sc013621",
			"id": "5D6D2402-C3AC-149B-5929-62A7D3B65AB7"
		},
		{
			"etask.entity": "sc013626",
			"id": "FBC528C9-E9F4-18C3-BAE5-6F65ECF500E6"
		},
		{
			"etask.entity": "sc013628",
			"id": "F9FB997E-7A64-5A45-8961-0CAA462AE378"
		},
		{
			"etask.entity": "sc013633",
			"id": "B8F153DC-10B7-9318-2326-EBD85B054EC0"
		},
		{
			"etask.entity": "sc013638",
			"id": "32BE8657-CB94-B3C1-0347-518643CAF331"
		},
		{
			"etask.entity": "sc013643",
			"id": "1DA1F92A-4D86-8D7C-47FA-F805AFD21B88"
		},
		{
			"etask.entity": "sc013648",
			"id": "D264192D-55BF-3FD5-FCC8-191AA3A755F8"
		},
		{
			"etask.entity": "sc013650",
			"id": "5F0B457B-D020-53F5-99BA-EB9B92763636"
		},
		{
			"etask.entity": "sc013655",
			"id": "83373188-F0D0-740A-8F43-83B02A87CC49"
		},
		{
			"etask.entity": "sc013660",
			"id": "3C7EF76B-0757-99EC-8D04-BD31C513AD76"
		},
		{
			"etask.entity": "sc013665",
			"id": "9B077354-B397-CDB7-38F1-ED643989651A"
		},
		{
			"etask.entity": "sc013670",
			"id": "F5D24741-4EDD-1E2C-1910-6F60800887DA"
		},
		{
			"etask.entity": "sc023596",
			"id": "78C0AB78-FE19-F1C4-9354-C4A2D25F7163"
		},
		{
			"etask.entity": "sc016771",
			"id": "D1F5A111-B08F-FCCC-85A6-71B1998CF3BE"
		},
		{
			"etask.entity": "sc016772",
			"id": "C1DF0136-A41D-C489-44B7-B4BB6EA93BAF"
		},
		{
			"etask.entity": "sc016773",
			"id": "D6839829-455F-2268-EBDF-E8B41C147F6F"
		},
		{
			"etask.entity": "sc016774",
			"id": "3B584EFE-933B-E584-6131-7AE5B39AD1F6"
		},
		{
			"etask.entity": "sc016776",
			"id": "5372DFF4-6472-27AA-A55B-861CC0D36E85"
		},
		{
			"etask.entity": "sc016777",
			"id": "1B66DE6A-4897-C3A1-0A6F-D185DAD9AE2D"
		},
		{
			"etask.entity": "sc016778",
			"id": "C44C693A-055F-B645-0B0C-0F12003CAA2C"
		},
		{
			"etask.entity": "sc016779",
			"id": "6C41D5B2-37BC-B3FA-B8B7-60B526B02A77"
		},
		{
			"etask.entity": "sc016781",
			"id": "494D61FF-D87A-A855-533F-133C2100EA50"
		},
		{
			"etask.entity": "sc016782",
			"id": "0DD164C2-FC6A-59C3-E56A-B32C54E68506"
		},
		{
			"etask.entity": "sc016783",
			"id": "FD074443-E557-7FFE-2914-3B04DCBB7412"
		},
		{
			"etask.entity": "sc016784",
			"id": "146A77CF-814F-301F-7D2C-6C795440D735"
		},
		{
			"etask.entity": "sc016786",
			"id": "803C4BE5-85E6-F3D1-C314-4C807C608046"
		},
		{
			"etask.entity": "sc016787",
			"id": "DA6D7286-42EC-DE4A-56B7-AD8F15A4BAED"
		},
		{
			"etask.entity": "sc016788",
			"id": "51D766D4-54C0-9888-699B-AEE71B40C527"
		},
		{
			"etask.entity": "sc016789",
			"id": "3B3E0BE8-1D59-FFB1-21A7-93BD53C4095D"
		},
		{
			"etask.entity": "sc016791",
			"id": "02F93CA9-70AE-1F20-AD28-DED3BF47E01C"
		},
		{
			"etask.entity": "sc023597",
			"id": "3C823AF2-9A73-FDF6-B5A5-A6CB33CB7C7F"
		},
		{
			"etask.entity": "sc023598",
			"id": "287D6CAD-6621-B21D-1619-7DFBEE4698EC"
		},
		{
			"etask.entity": "sc023599",
			"id": "CA885216-C8C8-60AE-EB49-634FE1CF7C06"
		},
		{
			"etask.entity": "sc016793",
			"id": "6A31075E-8E8D-81F5-1966-779396B1A629"
		},
		{
			"etask.entity": "sc016794",
			"id": "7D893394-098C-B4A8-9997-D20BBE0EF7F7"
		},
		{
			"etask.entity": "sc016795",
			"id": "398E072E-64FE-41E1-45B5-722B83C7C3BD"
		},
		{
			"etask.entity": "sc016796",
			"id": "29F9F17B-A27C-6811-E508-397EB247E782"
		},
		{
			"etask.entity": "sc016798",
			"id": "FFB4B93C-9201-2156-7D8F-3A6979D33CF6"
		},
		{
			"etask.entity": "sc016799",
			"id": "8C53220D-4579-B4BC-4F28-040F6CCDD8CF"
		},
		{
			"etask.entity": "sc016800",
			"id": "16DA6F31-917E-2781-97F0-C1DF088E35F2"
		},
		{
			"etask.entity": "sc016801",
			"id": "4EF26C44-45B3-4E72-2CCA-C89C4C2C6611"
		},
		{
			"etask.entity": "sc016803",
			"id": "30893A97-BB3E-4F99-CA4E-5D0F4321220B"
		},
		{
			"etask.entity": "sc016804",
			"id": "B2EAB84B-16EA-BD62-8305-D74E9129631B"
		},
		{
			"etask.entity": "sc016805",
			"id": "A46E0E18-9C14-C578-91AE-925272326E8C"
		},
		{
			"etask.entity": "sc016806",
			"id": "055FDD4B-92D5-9929-3AD2-87C954C7B933"
		},
		{
			"etask.entity": "sc016808",
			"id": "59C6382F-0BEB-9E90-962E-F3BA8E578D0C"
		},
		{
			"etask.entity": "sc016811",
			"id": "F0D351E2-8573-B474-04CD-3FF0002B6371"
		},
		{
			"etask.entity": "sc016812",
			"id": "6876206F-4A81-950C-1E0A-2FB72975AF6E"
		},
		{
			"etask.entity": "sc016813",
			"id": "99E76D75-886C-292F-056C-A68D86E51A5E"
		},
		{
			"etask.entity": "sc023600",
			"id": "699C1901-6893-6C97-4F65-2CD2BC2E4161"
		},
		{
			"etask.entity": "sc016815",
			"id": "9B714297-CFFD-6946-454B-060C3FBC3331"
		},
		{
			"etask.entity": "sc016816",
			"id": "33B14146-FEDE-A102-E3F0-3FE3F25FD4BA"
		},
		{
			"etask.entity": "sc016817",
			"id": "3A8DDF21-09C2-7C90-0F0B-C3C6826EF144"
		},
		{
			"etask.entity": "sc016818",
			"id": "5D4F46EE-00B4-FA8F-884F-32CF15A21CD2"
		},
		{
			"etask.entity": "sc016820",
			"id": "81A3A487-5D49-A5D5-43CF-2395638A94B3"
		},
		{
			"etask.entity": "sc016821",
			"id": "EF682AE4-C60C-36B1-34F5-C5A1EE11B6C7"
		},
		{
			"etask.entity": "sc016822",
			"id": "FA05A8C4-F634-5E5E-A95A-DAD64E50E9EC"
		},
		{
			"etask.entity": "sc016823",
			"id": "6C8B56A8-A52F-38A8-C6D0-E238A1D7C085"
		},
		{
			"etask.entity": "sc016825",
			"id": "EF02981E-932F-47FF-9B79-BCC8F5B2A5E6"
		},
		{
			"etask.entity": "sc016826",
			"id": "7A155243-0DA1-C93D-4E2F-236063F80518"
		},
		{
			"etask.entity": "sc016827",
			"id": "BAC7DDEC-692B-9274-778C-C4C80CD0EB1A"
		},
		{
			"etask.entity": "sc016828",
			"id": "5442B690-5CB7-F88E-02C2-E0D835306B9B"
		},
		{
			"etask.entity": "sc016830",
			"id": "474E40D2-ECE9-C1F9-BBD6-17253747640E"
		},
		{
			"etask.entity": "sc016831",
			"id": "97BB1314-8D26-4666-C050-84B05D9FEE8C"
		},
		{
			"etask.entity": "sc016832",
			"id": "8111795F-A978-2F35-A43F-B0231E9F1D75"
		},
		{
			"etask.entity": "sc016833",
			"id": "3FFCF0C0-2398-AA78-E461-B160C1B5CDDF"
		},
		{
			"etask.entity": "sc016835",
			"id": "64950C9F-341C-4BDA-109A-133DF2574EF4"
		},
		{
			"etask.entity": "sc013672",
			"id": "9A955C98-6F3D-854A-D927-A4C8366B9D25"
		},
		{
			"etask.entity": "sc013677",
			"id": "0D7484D5-1B19-EF97-F9FE-B43755A51C92"
		},
		{
			"etask.entity": "sc013682",
			"id": "BCE46B74-3034-73BB-3296-C0BE3DF04713"
		},
		{
			"etask.entity": "sc013687",
			"id": "D40AA61A-FDFF-EEFC-9C86-6F039620E623"
		},
		{
			"etask.entity": "sc013692",
			"id": "20C49B32-C5C0-9A06-469A-48AC532BEDF5"
		},
		{
			"etask.entity": "sc013694",
			"id": "D7194159-3C54-6099-EDE7-91762E480E31"
		},
		{
			"etask.entity": "sc013699",
			"id": "7AEC1C05-FEAD-BDFA-E1F3-BB4FB58B0AC2"
		},
		{
			"etask.entity": "sc013704",
			"id": "54E95525-181F-5691-22A3-4D1594BD38FB"
		},
		{
			"etask.entity": "sc013709",
			"id": "D99C26FC-786D-AD4B-E317-17CE33662E1B"
		},
		{
			"etask.entity": "sc013714",
			"id": "E8DC165D-A343-4D6A-09A8-A5E0C2F749A7"
		},
		{
			"etask.entity": "sc013716",
			"id": "05AD51B7-F9DF-7C53-B4FA-32C42B06F997"
		},
		{
			"etask.entity": "sc013721",
			"id": "BE5A3C2E-41F3-C6CA-B755-0C432E100068"
		},
		{
			"etask.entity": "sc013726",
			"id": "C538D470-F46E-8A7C-F449-7536D0023377"
		},
		{
			"etask.entity": "sc013731",
			"id": "332CD052-0ACC-6022-57A8-BC891895416D"
		},
		{
			"etask.entity": "sc013736",
			"id": "8A0E0679-DD2A-FCEE-7910-B8D318500279"
		},
		{
			"etask.entity": "sc013738",
			"id": "A76743C2-0F5C-B68C-7AB2-BE5EA050ACEF"
		},
		{
			"etask.entity": "sc013743",
			"id": "EEA03047-67F1-8B70-05A4-1D4BAC790AC3"
		},
		{
			"etask.entity": "sc013748",
			"id": "7FCCB00D-CDAB-D156-28D8-2AF336E7D17D"
		},
		{
			"etask.entity": "sc023601",
			"id": "8EDD8890-9795-887B-1FFA-06B164AED7C1"
		},
		{
			"etask.entity": "sc016837",
			"id": "0EBCD745-BCAA-FBF6-046D-66ACD8F351C7"
		},
		{
			"etask.entity": "sc016838",
			"id": "9997CED8-6563-FF7D-DB52-1F53FCD0F299"
		},
		{
			"etask.entity": "sc016839",
			"id": "824C734E-0E04-5BC1-F917-994AF7566467"
		},
		{
			"etask.entity": "sc016840",
			"id": "D8C201B2-0FF1-D53C-3986-7587FF632DC2"
		},
		{
			"etask.entity": "sc016843",
			"id": "D15A6D24-2D9B-CE42-756E-1E2384D61040"
		},
		{
			"etask.entity": "sc016844",
			"id": "E1DA288C-F861-15A8-F9CD-741654EE2608"
		},
		{
			"etask.entity": "sc016845",
			"id": "B45740B4-147D-73CE-7F87-355BF2BE0818"
		},
		{
			"etask.entity": "sc016846",
			"id": "60856AEF-F9EB-1F9C-ED9D-29D17B8BBCE8"
		},
		{
			"etask.entity": "sc016847",
			"id": "F77DBB3B-C1F2-9016-37DF-FCB26098ED85"
		},
		{
			"etask.entity": "sc016848",
			"id": "8B2702C9-2287-25F5-2B18-5B9AD6576204"
		},
		{
			"etask.entity": "sc016849",
			"id": "F50DAF04-81C9-E993-AC90-2277B492FB8B"
		},
		{
			"etask.entity": "sc016850",
			"id": "0A5367B4-C1A5-33FA-F2E8-BC04C163B801"
		},
		{
			"etask.entity": "sc016852",
			"id": "7270C0B0-FEB5-F712-EE88-3D1F944C77C8"
		},
		{
			"etask.entity": "sc016853",
			"id": "72E2D990-4E04-1E78-0429-71CC8291844C"
		},
		{
			"etask.entity": "sc016854",
			"id": "3007BA3B-87BA-7372-1F67-85DD55D524A1"
		},
		{
			"etask.entity": "sc016855",
			"id": "601ED137-2A0B-5082-276D-E2ABDB63A6E5"
		},
		{
			"etask.entity": "sc016857",
			"id": "E298413F-B2C9-7D37-0AB7-297DE76D56CA"
		},
		{
			"etask.entity": "sc023602",
			"id": "008C01BE-6AA7-AD05-29B0-11314A7BFF08"
		},
		{
			"etask.entity": "sc016859",
			"id": "8E3AA898-AB43-8422-1718-CF2E10081512"
		},
		{
			"etask.entity": "sc016860",
			"id": "C7683F47-04D9-EA00-E5FF-71148674410D"
		},
		{
			"etask.entity": "sc016861",
			"id": "02710502-751C-6D34-EBC7-80A71F7C088A"
		},
		{
			"etask.entity": "sc016862",
			"id": "350C9EEF-86B0-A5EA-B7B3-45E3610DCBBA"
		},
		{
			"etask.entity": "sc016864",
			"id": "0B09CBFB-DC00-B980-C513-F3408DF493C6"
		},
		{
			"etask.entity": "sc016865",
			"id": "9E26E1BD-E8FB-180F-77BA-EB64B06F97D3"
		},
		{
			"etask.entity": "sc016866",
			"id": "FD7CDC15-50F6-9357-70D3-1B5A94AACBBF"
		},
		{
			"etask.entity": "sc016867",
			"id": "831C22BB-ACF5-B5F2-0FA6-74CAEDC64ADB"
		},
		{
			"etask.entity": "sc016869",
			"id": "DBA3D4DA-7B5B-61C4-34C1-761B00076F6A"
		},
		{
			"etask.entity": "sc016872",
			"id": "288E4D68-C0E3-F7E3-5C86-19A419A83B61"
		},
		{
			"etask.entity": "sc016873",
			"id": "0D5118A0-D15F-9328-EC2F-73F94F858AD6"
		},
		{
			"etask.entity": "sc016874",
			"id": "E1929186-78FA-9537-48AA-1148479DBA0C"
		},
		{
			"etask.entity": "sc016875",
			"id": "1A57A544-8591-F518-0A2E-04F2F5CE79D7"
		},
		{
			"etask.entity": "sc016876",
			"id": "F7CBB494-924A-E08C-05B9-C4C7DAE381A2"
		},
		{
			"etask.entity": "sc016877",
			"id": "C0F4FAA8-1239-5DC2-0615-C48E185EDE47"
		},
		{
			"etask.entity": "sc016878",
			"id": "1AFDAB93-54C4-754D-613C-7622AACD0FAE"
		},
		{
			"etask.entity": "sc016879",
			"id": "674350E6-E54A-2900-DE97-4661613AE832"
		},
		{
			"etask.entity": "sc023603",
			"id": "F13C9242-690A-0EA7-787A-178836A908C5"
		},
		{
			"etask.entity": "sc016881",
			"id": "19037B8F-7F56-15F3-8269-C3D059168219"
		},
		{
			"etask.entity": "sc016882",
			"id": "9942D802-B773-5533-9BE2-D86B6085C35C"
		},
		{
			"etask.entity": "sc016883",
			"id": "5F8218E0-071C-4D18-474B-A2CA148C443E"
		},
		{
			"etask.entity": "sc016884",
			"id": "9ABD1D15-6953-B52A-F8FD-07B089D3EBE9"
		},
		{
			"etask.entity": "sc016886",
			"id": "1E7BECCC-F9F4-FAFB-13CA-42568699510B"
		},
		{
			"etask.entity": "sc016887",
			"id": "AAE5E484-C905-9D43-32C2-9CF70C430591"
		},
		{
			"etask.entity": "sc016888",
			"id": "F669C66E-D7AD-1375-35CA-7F08D3065DD2"
		},
		{
			"etask.entity": "sc016889",
			"id": "F5E42301-0520-C6F6-6391-8EF01DF3EF8C"
		},
		{
			"etask.entity": "sc016891",
			"id": "566621E0-9D66-8F9A-0DC8-3E5794E2AF3B"
		},
		{
			"etask.entity": "sc016892",
			"id": "58CFC2F1-D8EB-4344-1610-5440B341C4A5"
		},
		{
			"etask.entity": "sc016893",
			"id": "8E64D211-0C33-1415-E2D3-CEB8153AFE28"
		},
		{
			"etask.entity": "sc016896",
			"id": "110B3D18-2A8C-8FE7-4D81-6E81B719D39B"
		},
		{
			"etask.entity": "sc016897",
			"id": "E56509E5-2997-3E09-1DA7-8989752CFA35"
		},
		{
			"etask.entity": "sc016898",
			"id": "1F407F34-FCBC-D6C6-B221-0B56ECB028F0"
		},
		{
			"etask.entity": "sc016899",
			"id": "1491622B-AF9C-7492-0895-237CBA436A6A"
		},
		{
			"etask.entity": "sc016900",
			"id": "06AFCB46-2545-4009-68EE-15FF9B34D94D"
		},
		{
			"etask.entity": "sc016901",
			"id": "C6BBF438-DEBB-4D22-EF1A-8908EC314B64"
		},
		{
			"etask.entity": "sc023604",
			"id": "A97900C5-95FC-D48C-F8C3-0104C3855564"
		},
		{
			"etask.entity": "sc016903",
			"id": "1FCAE760-766F-45C3-0C7E-AC88A1E9C1DF"
		},
		{
			"etask.entity": "sc016904",
			"id": "4D832EAA-273E-017B-CBFF-59AE82D65A7E"
		},
		{
			"etask.entity": "sc016905",
			"id": "12764323-22FF-475C-B7AD-FE3940D17B9E"
		},
		{
			"etask.entity": "sc016906",
			"id": "21BF06D3-5B9B-C530-B067-7343EAB24352"
		},
		{
			"etask.entity": "sc016908",
			"id": "D199E52E-A514-FAB6-8C16-BC449E6A2877"
		},
		{
			"etask.entity": "sc016909",
			"id": "B85FCF98-DE30-C170-04D1-029E33588878"
		},
		{
			"etask.entity": "sc016910",
			"id": "382C3531-A0F6-CCF1-D384-EC4EE780D8A7"
		},
		{
			"etask.entity": "sc016911",
			"id": "90C65BBD-78A1-D2C3-1AF9-8EE4CFB08FA5"
		},
		{
			"etask.entity": "sc016913",
			"id": "806FDC68-2F06-F434-BE51-2AD474CBD7E1"
		},
		{
			"etask.entity": "sc016914",
			"id": "36AFFE74-C2AB-195F-38FD-8E91715E8BFD"
		},
		{
			"etask.entity": "sc016915",
			"id": "EC0639BD-E458-1D31-F9D7-9FA9E1BD34F3"
		},
		{
			"etask.entity": "sc016916",
			"id": "80E1C334-954B-5373-7ADE-C672004B7339"
		},
		{
			"etask.entity": "sc016918",
			"id": "A6925E9F-A091-507C-7ECA-94CB404D962F"
		},
		{
			"etask.entity": "sc016920",
			"id": "A4F2A0AD-7AAF-FBA1-D174-9C97EA443187"
		},
		{
			"etask.entity": "sc016921",
			"id": "7E591FD0-63AE-FC83-B094-A1002ABEF4C8"
		},
		{
			"etask.entity": "sc016922",
			"id": "20A759E1-AB73-C94A-C9E2-C01038796FFA"
		},
		{
			"etask.entity": "sc016923",
			"id": "89034B98-5C56-E861-EF65-4AF61EDA8A96"
		},
		{
			"etask.entity": "sc013753",
			"id": "94A576B9-053A-D1F7-46DB-3CB0408EDDC7"
		},
		{
			"etask.entity": "sc013758",
			"id": "EFD0D8C1-7DC0-53DD-472B-2E757FE8BC3C"
		},
		{
			"etask.entity": "sc013760",
			"id": "1ECAF5CC-C3E9-A724-994B-C097A3A28548"
		},
		{
			"etask.entity": "sc013765",
			"id": "8DC541BB-442A-84F3-7CE2-4C0615DE7644"
		},
		{
			"etask.entity": "sc013770",
			"id": "C72B52DF-9D2D-74AC-4A08-4B48B8883A0B"
		},
		{
			"etask.entity": "sc013775",
			"id": "FA5CD4AD-289E-BCFB-E6DC-9D25E5CF9782"
		},
		{
			"etask.entity": "sc013780",
			"id": "AD60EB7A-1C45-BFC2-0C92-FA12B0C3F38B"
		},
		{
			"etask.entity": "sc013782",
			"id": "CC6AD5E7-AF68-316D-EE1C-6611999A13FA"
		},
		{
			"etask.entity": "sc013787",
			"id": "A7CD20FA-5511-2A40-2537-AC28AD32AA02"
		},
		{
			"etask.entity": "sc013792",
			"id": "6B881120-5FAB-84B7-B01D-00857811C948"
		},
		{
			"etask.entity": "sc013797",
			"id": "4A05EDB7-78F2-D649-7AD8-A0EDFB076DF1"
		},
		{
			"etask.entity": "sc013802",
			"id": "CB8EC2DE-EE6D-76B7-5C3A-282549383BF6"
		},
		{
			"etask.entity": "sc013804",
			"id": "D182CA29-6B43-D61F-D6C6-0874E7C82EEF"
		},
		{
			"etask.entity": "sc013809",
			"id": "B29BDC36-E443-11E9-B62B-0EA054E345AF"
		},
		{
			"etask.entity": "sc013814",
			"id": "E91C5349-D562-025E-4978-11664378558F"
		},
		{
			"etask.entity": "sc013819",
			"id": "E542D3DA-9C43-BA53-3790-C3CE88BFDC85"
		},
		{
			"etask.entity": "sc013824",
			"id": "D404F9C6-119A-86E5-5407-CA96D934068E"
		},
		{
			"etask.entity": "sc013826",
			"id": "DB8EE0D7-06F5-2B28-3E47-7F848030DC43"
		},
		{
			"etask.entity": "sc023605",
			"id": "63742F9E-BFE9-4C11-9879-48B31C480FB2"
		},
		{
			"etask.entity": "sc023606",
			"id": "D1886D84-6968-AD51-4269-0EF0405BA935"
		},
		{
			"etask.entity": "sc023607",
			"id": "50F76598-A914-E152-4F9E-6FBC0060DE7E"
		},
		{
			"etask.entity": "sc016925",
			"id": "CA55E8D9-B3FF-7640-40B3-D546486AC70C"
		},
		{
			"etask.entity": "sc016926",
			"id": "784D4FB3-5C56-3BF1-5868-1DA24D59DB71"
		},
		{
			"etask.entity": "sc016927",
			"id": "896D696C-72DF-8785-CA5A-8F0DB56852BB"
		},
		{
			"etask.entity": "sc016928",
			"id": "9E6B4ED9-4201-854F-0C30-DAED25FEBDE6"
		},
		{
			"etask.entity": "sc016930",
			"id": "29A70AEA-F87F-2B3A-A3D7-E94381955EA8"
		},
		{
			"etask.entity": "sc016931",
			"id": "36CD90EC-EFB3-F3BA-B26C-6A80E7E64D1F"
		},
		{
			"etask.entity": "sc016932",
			"id": "C0BA58DA-4051-7D01-ACE9-150E70C06905"
		},
		{
			"etask.entity": "sc016933",
			"id": "F4C95B15-DB5D-F026-FCB6-B9ECC4C42B35"
		},
		{
			"etask.entity": "sc016935",
			"id": "7E922AA1-CFA3-DA81-4DBA-62D4E640E15E"
		},
		{
			"etask.entity": "sc016936",
			"id": "EAF5E24D-2972-97EE-6C02-FE9B8074AE37"
		},
		{
			"etask.entity": "sc016937",
			"id": "06702A8F-0D51-2D1A-A6BE-80F78143738A"
		},
		{
			"etask.entity": "sc016938",
			"id": "618BAF49-5176-184C-AB29-26FC02FE93A3"
		},
		{
			"etask.entity": "sc016942",
			"id": "6356954C-22EE-B5A2-D8B9-DB3F8DF1F283"
		},
		{
			"etask.entity": "sc016943",
			"id": "3F0468A4-F54D-F2EE-1A26-BD5E5DE64D5A"
		},
		{
			"etask.entity": "sc016944",
			"id": "1A94B2C3-70BE-98F8-BC3F-E2535CAFABD2"
		},
		{
			"etask.entity": "sc016945",
			"id": "3E6AAE84-3B3E-89C9-9DF9-CF8F094318AD"
		},
		{
			"etask.entity": "sc023608",
			"id": "444A7C64-3A15-4C8F-AC46-873EDB8B2EED"
		},
		{
			"etask.entity": "sc016947",
			"id": "42BD432D-AFDB-6884-C3CA-0F875140CD9D"
		},
		{
			"etask.entity": "sc016948",
			"id": "235C865E-BBE9-78A5-6C4C-DD975B2D1463"
		},
		{
			"etask.entity": "sc016949",
			"id": "CCC89BC5-50E8-8EA6-6F42-C20079A9B57E"
		},
		{
			"etask.entity": "sc016950",
			"id": "19A22C4E-DEE4-4B05-F81F-095B2D991484"
		},
		{
			"etask.entity": "sc016952",
			"id": "BD6E5E36-71C9-7623-900F-4A4BE1E86288"
		},
		{
			"etask.entity": "sc016953",
			"id": "66425398-F0C4-14E3-2D46-139A89B6A073"
		},
		{
			"etask.entity": "sc016954",
			"id": "36CA01F4-1643-2022-1CC4-87E7D6EEF6BA"
		},
		{
			"etask.entity": "sc016955",
			"id": "EE2C1450-0C76-3A88-D0B8-B1602543BBF4"
		},
		{
			"etask.entity": "sc016957",
			"id": "720D5F96-08A7-3E0A-A41C-0A67E95FBBD9"
		},
		{
			"etask.entity": "sc016960",
			"id": "7D6F3118-1AE8-B3D8-B42E-9081D20EC3A2"
		},
		{
			"etask.entity": "sc016961",
			"id": "86A5A082-8291-F604-8112-E02D3B970CE2"
		},
		{
			"etask.entity": "sc016962",
			"id": "96DFAA9F-1913-9143-5568-7B104E7AA965"
		},
		{
			"etask.entity": "sc016963",
			"id": "AB41F000-A04A-C384-97FC-18DA512CF175"
		},
		{
			"etask.entity": "sc016964",
			"id": "C965728B-7FE5-2A2E-AC25-DC83F08ED4E1"
		},
		{
			"etask.entity": "sc016965",
			"id": "39788AAF-D3F6-3119-D011-1F617F254AC5"
		},
		{
			"etask.entity": "sc016966",
			"id": "5D5A9E6D-9890-943C-DE77-0371CEF15832"
		},
		{
			"etask.entity": "sc016967",
			"id": "8B1456CB-8743-E38A-5FCA-0CDA969A2FA0"
		},
		{
			"etask.entity": "sc023609",
			"id": "498683F1-7524-A5FE-D16C-BAEB8BB43F35"
		},
		{
			"etask.entity": "sc016969",
			"id": "B5FF0D5C-60CD-5A43-7AA4-4C7DC2E4A5AC"
		},
		{
			"etask.entity": "sc016970",
			"id": "C37E4A3B-8299-F39E-D4C6-63DD2DB4A537"
		},
		{
			"etask.entity": "sc016971",
			"id": "577EDDC4-EBD6-E6E2-E17D-7AC884273A51"
		},
		{
			"etask.entity": "sc016972",
			"id": "B74F5C8E-4FB5-BE27-8F8E-F1F146C77DD1"
		},
		{
			"etask.entity": "sc016974",
			"id": "A91FB59D-09D5-ECC3-50FC-55AFDA2A8CC8"
		},
		{
			"etask.entity": "sc016975",
			"id": "460EEAA6-7899-AAB7-F0BC-AE60472FEB7D"
		},
		{
			"etask.entity": "sc016978",
			"id": "70732C9B-9BDA-3572-5770-C40256E37466"
		},
		{
			"etask.entity": "sc016979",
			"id": "5ABFBFF7-8A51-97F1-FCB8-774BBF519695"
		},
		{
			"etask.entity": "sc016980",
			"id": "9CA0BCF2-8542-39F2-E40E-13C6F65D1F4E"
		},
		{
			"etask.entity": "sc016981",
			"id": "AEF6FD6F-9DB9-5173-05D8-D941F6362773"
		},
		{
			"etask.entity": "sc016982",
			"id": "11826C65-5C25-135F-1C0F-CCC04647447F"
		},
		{
			"etask.entity": "sc016983",
			"id": "F79EF177-0406-CC52-0E19-9966CEA985EB"
		},
		{
			"etask.entity": "sc016984",
			"id": "14B2DA8A-8C24-B72E-3163-5F6D8D08D266"
		},
		{
			"etask.entity": "sc016985",
			"id": "E7433D01-C34E-2055-BB65-A8D192D3843A"
		},
		{
			"etask.entity": "sc016986",
			"id": "D6388AB0-22AD-A495-19F9-C7F5D6C091EA"
		},
		{
			"etask.entity": "sc016987",
			"id": "81F45FDA-F966-7D2F-4F9B-D1B0A3EFB5F4"
		},
		{
			"etask.entity": "sc016989",
			"id": "A58F4986-D10B-797E-2324-6436668BE195"
		},
		{
			"etask.entity": "sc013831",
			"id": "B69D8F26-D2D4-2D27-E62C-6D5EE1C67C8B"
		},
		{
			"etask.entity": "sc013836",
			"id": "14A53F20-47B3-96C8-BAE9-E175E609B21C"
		},
		{
			"etask.entity": "sc013841",
			"id": "44EE9C7A-5EDD-51E5-25F8-FA4DCA575975"
		},
		{
			"etask.entity": "sc013846",
			"id": "961116F4-E2A6-2232-E991-783EB74C6CB1"
		},
		{
			"etask.entity": "sc013848",
			"id": "1B1047EA-0037-9ACB-FD67-A935992CC819"
		},
		{
			"etask.entity": "sc013853",
			"id": "4332A2C9-8507-FC1A-9598-1C8FA49E95BF"
		},
		{
			"etask.entity": "sc013858",
			"id": "4AA392A7-F6AC-D60E-17D7-2E80E737F8AF"
		},
		{
			"etask.entity": "sc013863",
			"id": "DB081EE1-9B4C-C5F6-85AA-3A32BBCE1318"
		},
		{
			"etask.entity": "sc013868",
			"id": "BFDF4369-5ABB-BBD7-EEDB-A388049D485D"
		},
		{
			"etask.entity": "sc013870",
			"id": "C577F0F9-FFBD-939D-8021-3990AF1825FF"
		},
		{
			"etask.entity": "sc013875",
			"id": "A9F71058-1146-8A49-3F70-660A3B4BDD8C"
		},
		{
			"etask.entity": "sc013880",
			"id": "6539CF4C-E625-06A2-1D31-67CDC5FFCE6C"
		},
		{
			"etask.entity": "sc013885",
			"id": "7956A71D-72CD-0972-B796-ED0A12D553F1"
		},
		{
			"etask.entity": "sc013890",
			"id": "644E1013-0F6E-49D9-AE15-CACB970DAEB1"
		},
		{
			"etask.entity": "sc013892",
			"id": "C8E41D2E-1C87-D474-3891-C03222A82657"
		},
		{
			"etask.entity": "sc013897",
			"id": "ED783ED2-0C4D-450C-5CA0-1EAB0D784D06"
		},
		{
			"etask.entity": "sc013902",
			"id": "38BCA5D8-58DB-D3DA-6098-622FCACCD64C"
		},
		{
			"etask.entity": "sc013907",
			"id": "F9C60976-216C-D35F-0B05-2838BCA9F7AC"
		},
		{
			"etask.entity": "sc023610",
			"id": "ED467ACA-DC71-FBF9-ED34-C6D19BCEDAAC"
		},
		{
			"etask.entity": "sc016991",
			"id": "D20DE382-DC5B-7002-3219-029CE3C2CC38"
		},
		{
			"etask.entity": "sc016992",
			"id": "AD2CBE70-127E-1EFB-59AC-3BFCF8B47814"
		},
		{
			"etask.entity": "sc016993",
			"id": "0C6DBD58-AC64-CB0D-7ECF-4A1472637F1C"
		},
		{
			"etask.entity": "sc016996",
			"id": "1FB71B82-6A34-4E75-380E-E564D2599866"
		},
		{
			"etask.entity": "sc016997",
			"id": "42A8F2F7-6D55-9BBC-F997-5CBD97278CD9"
		},
		{
			"etask.entity": "sc016998",
			"id": "C00FEBA8-43DC-7355-18FB-A65E104F7372"
		},
		{
			"etask.entity": "sc016999",
			"id": "6966E610-ACE6-F5DB-2341-11EA4EF1242A"
		},
		{
			"etask.entity": "sc017000",
			"id": "A9C13830-C2B7-5386-23B0-7CE03AFB1AB1"
		},
		{
			"etask.entity": "sc017001",
			"id": "82DA70CC-F3B0-D297-2635-074ED2C42962"
		},
		{
			"etask.entity": "sc017002",
			"id": "302324F6-5D31-4C8A-F032-B2BE5FC52B5E"
		},
		{
			"etask.entity": "sc017003",
			"id": "A1767E26-7CD5-CA09-39CB-892D536EF3F6"
		},
		{
			"etask.entity": "sc017005",
			"id": "CBAD8CDE-EB6F-502B-257E-33C1DB696251"
		},
		{
			"etask.entity": "sc017006",
			"id": "378404FE-ED73-3742-99DF-93F20FF7FCF4"
		},
		{
			"etask.entity": "sc017007",
			"id": "34653628-E60D-997A-4EC4-FA97A9E0561C"
		},
		{
			"etask.entity": "sc017008",
			"id": "0E82E9FB-D570-E8DB-C212-688B2267BB47"
		},
		{
			"etask.entity": "sc017009",
			"id": "FB317EE6-FD61-C8BF-BE02-DFF523C95F97"
		},
		{
			"etask.entity": "sc017011",
			"id": "A0C661D4-DF1A-E2C0-F760-8EE8BE9EB519"
		},
		{
			"etask.entity": "sc023611",
			"id": "72BEAA5D-5367-3EF4-6192-FC37C2BB0C4C"
		},
		{
			"etask.entity": "sc017013",
			"id": "B22E38EA-FDA7-E66C-15EE-90EBDC43F2EE"
		},
		{
			"etask.entity": "sc017014",
			"id": "BD3975AC-0F23-BA96-9DAE-308BD65388CE"
		},
		{
			"etask.entity": "sc017017",
			"id": "8AFA8A55-42FC-9E6F-BF5A-6D12EE9BEA6E"
		},
		{
			"etask.entity": "sc017018",
			"id": "0C0A400D-F991-E167-3BF1-2005FC25B5C7"
		},
		{
			"etask.entity": "sc017019",
			"id": "897761B1-3031-3EFB-5D73-5E7872610319"
		},
		{
			"etask.entity": "sc017020",
			"id": "6DB3ACDF-9F22-16AB-9318-B3E6537EE64C"
		},
		{
			"etask.entity": "sc017021",
			"id": "CAB76FA2-5E0B-12CF-FA2B-660858632344"
		},
		{
			"etask.entity": "sc017022",
			"id": "024517F1-F7D0-E301-C95C-947CF5613D87"
		},
		{
			"etask.entity": "sc017023",
			"id": "ACEC1D70-F908-6D1D-0DB8-ACD65B3425B2"
		},
		{
			"etask.entity": "sc017024",
			"id": "66F7AE2D-1806-F806-E3A1-FDC0CEFD4EC3"
		},
		{
			"etask.entity": "sc017025",
			"id": "180572F3-CCEA-B959-CA4D-B4A144B83121"
		},
		{
			"etask.entity": "sc017026",
			"id": "211440F1-3A49-741C-6F68-EA8052E25E5B"
		},
		{
			"etask.entity": "sc017028",
			"id": "0AEA5422-BAD1-F18F-A561-1F2936CE5127"
		},
		{
			"etask.entity": "sc017030",
			"id": "B345CC09-C676-858F-45B7-E502CFD7E894"
		},
		{
			"etask.entity": "sc017031",
			"id": "6FD20EC8-11EB-5E44-FF17-6A7810B8CB7A"
		},
		{
			"etask.entity": "sc017032",
			"id": "936E73F8-6146-15FA-7AF7-447C7905D13E"
		},
		{
			"etask.entity": "sc017033",
			"id": "AFFAA5AC-D96B-39EF-F2C9-338155639C4D"
		},
		{
			"etask.entity": "sc023612",
			"id": "1C073657-D401-12B9-2457-E27ABE681541"
		},
		{
			"etask.entity": "sc017035",
			"id": "0928E38A-C371-A9B7-1E51-BB156A8B7A93"
		},
		{
			"etask.entity": "sc017036",
			"id": "81C5B61A-9476-A476-4586-4AE4DA0BF052"
		},
		{
			"etask.entity": "sc017037",
			"id": "697E3400-7CFB-0798-CCA6-CC4E5112D6F0"
		},
		{
			"etask.entity": "sc017038",
			"id": "F5E4314F-BA79-8A6B-C8AE-A7E470E515DF"
		},
		{
			"etask.entity": "sc017040",
			"id": "6828791D-E5CC-3B7D-500E-54301A5EEE0F"
		},
		{
			"etask.entity": "sc017041",
			"id": "05008A07-1ACB-717A-AEF8-A4E3A4D70AD2"
		},
		{
			"etask.entity": "sc017042",
			"id": "83852DCE-D9E2-2CB4-5E8B-E881E88C1857"
		},
		{
			"etask.entity": "sc017045",
			"id": "073AE218-4F31-A49A-D0FE-05E36E20A7C9"
		},
		{
			"etask.entity": "sc017046",
			"id": "8C84B81E-BCD5-0BAA-8841-4B3F78B4CD6E"
		},
		{
			"etask.entity": "sc017047",
			"id": "517836F7-AE08-AE90-B8FB-3725D9748AC4"
		},
		{
			"etask.entity": "sc017048",
			"id": "1B8365A7-87A4-E39F-3FDC-F7DB2CEFAD60"
		},
		{
			"etask.entity": "sc017049",
			"id": "3FE03FC8-525B-82E2-9CEC-44F4809F4593"
		},
		{
			"etask.entity": "sc017050",
			"id": "D8557EE6-6BE6-65B2-950B-C9E3F5A94C55"
		},
		{
			"etask.entity": "sc017051",
			"id": "9D99C9E9-B3E3-2D13-8A43-6CF4A8C79C55"
		},
		{
			"etask.entity": "sc017052",
			"id": "E5B9A31E-7C8C-B5E5-AFFE-3B5E53425525"
		},
		{
			"etask.entity": "sc017053",
			"id": "F98CAB2D-C602-2290-E790-014E4F7613B8"
		},
		{
			"etask.entity": "sc017055",
			"id": "64984071-6121-8AD7-BF89-C12B51601A7C"
		},
		{
			"etask.entity": "sc023613",
			"id": "4C74E622-5980-7BFA-CA3D-9D4947A1CE9E"
		},
		{
			"etask.entity": "sc017057",
			"id": "FDE1ADF9-0D10-2858-6C06-EB4B11594C65"
		},
		{
			"etask.entity": "sc017058",
			"id": "397B5549-A1E8-B46E-367C-65E904E7855D"
		},
		{
			"etask.entity": "sc017059",
			"id": "36A0FECD-4095-AEB5-E06C-E5EE0833F870"
		},
		{
			"etask.entity": "sc017060",
			"id": "5684AA50-CB6B-A65D-DAB0-1FCD58F54661"
		},
		{
			"etask.entity": "sc017062",
			"id": "7BCC1E83-EBBA-EF00-6970-1BBA4A26C855"
		},
		{
			"etask.entity": "sc017063",
			"id": "82B60E04-53AF-C0DE-D31D-F3045F01D7CA"
		},
		{
			"etask.entity": "sc017064",
			"id": "5193C17B-F293-CE5C-F8EE-4CF73D7964C3"
		},
		{
			"etask.entity": "sc017065",
			"id": "63A6FCC3-42B3-5FB4-010A-1EEE6D259755"
		},
		{
			"etask.entity": "sc017067",
			"id": "FE74C7BC-0354-C06C-584A-34B9C07DCF6F"
		},
		{
			"etask.entity": "sc017068",
			"id": "7E3ADCFA-D54D-BE4A-20DE-A76CF5C0C27A"
		},
		{
			"etask.entity": "sc017069",
			"id": "74160A46-674D-2519-B92C-46CACEDB654E"
		},
		{
			"etask.entity": "sc017070",
			"id": "C69FEE03-3CF3-24A0-0777-4561467484CD"
		},
		{
			"etask.entity": "sc017072",
			"id": "A347B75A-6D36-A25E-5DA8-2288101E7813"
		},
		{
			"etask.entity": "sc017073",
			"id": "A0978ABD-5B6B-8AC9-9B31-6CF17B6428F8"
		},
		{
			"etask.entity": "sc017074",
			"id": "30AB2EE7-DAEA-320E-DC6B-AD596106EAC2"
		},
		{
			"etask.entity": "sc017075",
			"id": "643D3BF3-AF73-DD16-EB51-C29B710E035C"
		},
		{
			"etask.entity": "sc017077",
			"id": "9D6FCC80-1718-76FE-B9DF-C293AA92C742"
		},
		{
			"etask.entity": "sc013912",
			"id": "CAAC99C5-674D-A5ED-D2BC-FA6A4C73C9B1"
		},
		{
			"etask.entity": "sc013914",
			"id": "8760BE7E-F109-E6A6-CE66-748B25DA6CF5"
		},
		{
			"etask.entity": "sc013919",
			"id": "AAAB1A87-7C2E-0A01-22B7-387BC9AFAC12"
		},
		{
			"etask.entity": "sc013924",
			"id": "B0487918-F075-AFC5-5A8B-AE614B9AA74F"
		},
		{
			"etask.entity": "sc013929",
			"id": "8C0E0A86-4764-BDC4-4E63-E2A8F60AD4E0"
		},
		{
			"etask.entity": "sc013934",
			"id": "CC4B998C-5DF2-E7BC-BAD0-680A50140392"
		},
		{
			"etask.entity": "sc013936",
			"id": "8E1179DE-F169-5A5A-F172-ABDCC24019CB"
		},
		{
			"etask.entity": "sc013941",
			"id": "9A059146-F6F8-2824-71A5-0812F2D3CE51"
		},
		{
			"etask.entity": "sc013946",
			"id": "5F2B35D0-9AF5-6F63-8500-A9CE6B37BF2B"
		},
		{
			"etask.entity": "sc013951",
			"id": "231F239B-65E1-517F-8AA9-4D949D4A77A2"
		},
		{
			"etask.entity": "sc013956",
			"id": "0E2D88D1-8B51-196C-FE61-72D209A6B745"
		},
		{
			"etask.entity": "sc013958",
			"id": "AF891D4E-8199-FE64-F37C-4EE5890D4F17"
		},
		{
			"etask.entity": "sc013963",
			"id": "40EE38B6-7C89-1558-3F99-3DCB9D29C7BF"
		},
		{
			"etask.entity": "sc013968",
			"id": "7CDCDD5F-AA06-FD77-F3B5-8B0FECFDE4D5"
		},
		{
			"etask.entity": "sc013973",
			"id": "342FAAC3-757E-8FFA-3DCF-F0D78030591D"
		},
		{
			"etask.entity": "sc013978",
			"id": "0A95DB72-58E6-EEFD-D72F-5DC75704E4FF"
		},
		{
			"etask.entity": "sc013980",
			"id": "C83F78AE-0EDE-0CAD-08D1-0A91834DDA64"
		},
		{
			"etask.entity": "sc013985",
			"id": "8DCB252F-00AD-00E3-3375-8AF3A3F9D6BA"
		},
		{
			"etask.entity": "sc023614",
			"id": "8C58B3F6-3C7D-ACCD-36E0-8F82EB638BAD"
		},
		{
			"etask.entity": "sc017079",
			"id": "565E2390-5F43-E840-DC59-A2BA6FE0A1C3"
		},
		{
			"etask.entity": "sc017080",
			"id": "CC7A401F-3FE6-3CF7-A927-7E1D7B45985B"
		},
		{
			"etask.entity": "sc017081",
			"id": "C1250FAF-2BD8-E141-6263-F6962075F594"
		},
		{
			"etask.entity": "sc017082",
			"id": "6415ED95-A4B1-89C0-F644-CEC8EEAFEB28"
		},
		{
			"etask.entity": "sc017084",
			"id": "B9A20B60-3663-248D-750E-977AD9F502C6"
		},
		{
			"etask.entity": "sc017085",
			"id": "F896D751-8E98-3625-0C91-A89870251911"
		},
		{
			"etask.entity": "sc017086",
			"id": "14E0F6F5-448E-BE3C-D6EE-76D4796CD388"
		},
		{
			"etask.entity": "sc017087",
			"id": "6A83D351-2E5E-4CA9-4E44-D13857A54C6D"
		},
		{
			"etask.entity": "sc017089",
			"id": "EDC663A4-45AB-B4B5-244F-AD9E98C575A6"
		},
		{
			"etask.entity": "sc017090",
			"id": "24343BE9-412A-F5CA-BBC3-672D5EC9CD94"
		},
		{
			"etask.entity": "sc017091",
			"id": "0C76E140-878B-C73A-5419-6FEFCB561B83"
		},
		{
			"etask.entity": "sc017092",
			"id": "3E7260AF-009F-64D2-750A-9B26654AF613"
		},
		{
			"etask.entity": "sc017094",
			"id": "CBC25C76-951C-852A-CB5A-B6201AC4D41A"
		},
		{
			"etask.entity": "sc017095",
			"id": "FA758D69-9218-C1C1-5193-F8C4C72163D0"
		},
		{
			"etask.entity": "sc017096",
			"id": "3749A0DD-374F-AFBC-5750-744580B52E1D"
		},
		{
			"etask.entity": "sc017097",
			"id": "7A6BA24D-9F49-BFAE-1AC2-665478FCE2F7"
		},
		{
			"etask.entity": "sc017099",
			"id": "FBF58A28-AA8A-0821-9174-C0ABD18D8BA9"
		},
		{
			"etask.entity": "sc023615",
			"id": "24078CC8-A9A6-1AB0-F95B-8FE199B5D15C"
		},
		{
			"etask.entity": "sc017101",
			"id": "6B3AF88D-3EED-3280-09EB-86BA132C84D0"
		},
		{
			"etask.entity": "sc017102",
			"id": "5F788F9C-5F14-2884-18E4-18E0475211C7"
		},
		{
			"etask.entity": "sc017103",
			"id": "1F9C21D8-72DB-910E-ABD2-981EDB1780E2"
		},
		{
			"etask.entity": "sc017104",
			"id": "68B60FD0-D640-2D6B-91C0-CBB045F71805"
		},
		{
			"etask.entity": "sc017106",
			"id": "7BF00F50-8B13-CA32-C185-88D78CFA3500"
		},
		{
			"etask.entity": "sc017107",
			"id": "5AD5E1DA-C73D-366A-AD29-C04C18A6FEE5"
		},
		{
			"etask.entity": "sc017108",
			"id": "C67EB820-B0E5-8B04-1355-810C03ADD022"
		},
		{
			"etask.entity": "sc017109",
			"id": "136A8808-0CD4-E5A4-3131-91DC8E28C497"
		},
		{
			"etask.entity": "sc017111",
			"id": "36260AD0-CED7-95B0-6C68-173D882C3D77"
		},
		{
			"etask.entity": "sc017112",
			"id": "E1861455-DA71-5F96-EC20-49B97493D4A1"
		},
		{
			"etask.entity": "sc017113",
			"id": "5549638F-4870-1921-A2C5-67E38DAC4C58"
		},
		{
			"etask.entity": "sc017114",
			"id": "36DB128C-8C19-59C8-9B05-5B49E1B75634"
		},
		{
			"etask.entity": "sc017116",
			"id": "767F5FA8-A15D-6107-A6B9-E661FDB50AB3"
		},
		{
			"etask.entity": "sc017117",
			"id": "2FB3E2E4-A45E-9687-BF32-72AF49233767"
		},
		{
			"etask.entity": "sc017118",
			"id": "8110BC4E-BBC3-5C94-6BC7-CC542E7CF3CD"
		},
		{
			"etask.entity": "sc017119",
			"id": "EBD7CC13-3906-B293-B269-AC7DA708635B"
		},
		{
			"etask.entity": "sc017121",
			"id": "B92D5C5F-5421-2356-E22B-0250C197D57C"
		},
		{
			"etask.entity": "sc023616",
			"id": "78EDEE41-D146-59DE-3DA9-3556807BF273"
		},
		{
			"etask.entity": "sc017123",
			"id": "536A1907-889B-5053-CC72-84AAC4DEDF4F"
		},
		{
			"etask.entity": "sc017124",
			"id": "94D98008-62DE-E3CC-F2D3-53C638EA19AA"
		},
		{
			"etask.entity": "sc017125",
			"id": "9A459039-AC63-0A2A-A5C0-69D72F18CE7F"
		},
		{
			"etask.entity": "sc017126",
			"id": "7DFC7431-E70D-5B7A-A659-80893E8329B1"
		},
		{
			"etask.entity": "sc017128",
			"id": "E841DF79-32E0-0E3E-D55B-20100A617405"
		},
		{
			"etask.entity": "sc017129",
			"id": "4420CE73-178C-0D04-0F51-74942A64611D"
		},
		{
			"etask.entity": "sc017130",
			"id": "BDA17B68-FAFE-0144-0123-6A16168AA541"
		},
		{
			"etask.entity": "sc017131",
			"id": "243CB349-2CED-4A69-FC21-023E6B4B5C34"
		},
		{
			"etask.entity": "sc017133",
			"id": "FF19CC7D-8A60-E532-327B-BA80AE87CCBB"
		},
		{
			"etask.entity": "sc017134",
			"id": "95CC96FE-E852-C142-59D9-890FA5417C24"
		},
		{
			"etask.entity": "sc017135",
			"id": "9990E432-B654-850A-5D21-C79F4C4F4241"
		},
		{
			"etask.entity": "sc017136",
			"id": "AF573788-9D59-208C-E431-E85B48E57E2B"
		},
		{
			"etask.entity": "sc017138",
			"id": "FAFFD231-FFAC-D187-8673-023FA0372E3C"
		},
		{
			"etask.entity": "sc017139",
			"id": "7152A2E5-6A21-CE62-A751-15EC0827C680"
		},
		{
			"etask.entity": "sc017140",
			"id": "9A50678F-8D68-0EEF-2FFC-ED7FA2DB31A5"
		},
		{
			"etask.entity": "sc017141",
			"id": "CA0912BB-1CF9-1F9F-B9C5-AC7D8D2F7972"
		},
		{
			"etask.entity": "sc017143",
			"id": "2099E62F-CF1C-3EA8-E6FF-C324037BB657"
		},
		{
			"etask.entity": "sc013990",
			"id": "98794768-4629-620F-2F47-4BE1A95BA188"
		},
		{
			"etask.entity": "sc013995",
			"id": "F675A170-7304-3DE0-490F-C22EEF89F3CA"
		},
		{
			"etask.entity": "sc014000",
			"id": "FC1696E1-B849-3A7F-2AA3-6E21D8A6A78B"
		},
		{
			"etask.entity": "sc014002",
			"id": "229B446A-A75D-C1E5-03CB-C8F4A578F24B"
		},
		{
			"etask.entity": "sc014007",
			"id": "797FC17A-DD82-C2E8-055B-A8481D968802"
		},
		{
			"etask.entity": "sc014012",
			"id": "06E834FB-FECC-B98B-22D0-E6F9212F0A70"
		},
		{
			"etask.entity": "sc014017",
			"id": "7F7E819F-9273-9F06-1B87-BB75ED276F5A"
		},
		{
			"etask.entity": "sc014022",
			"id": "A91B58D2-7CB7-F52F-7602-691991F4D0B3"
		},
		{
			"etask.entity": "sc014024",
			"id": "2E1A4C26-8943-B07F-8EC9-E560177CB1F7"
		},
		{
			"etask.entity": "sc014029",
			"id": "992FB366-8115-CD79-4F56-08E0367056D9"
		},
		{
			"etask.entity": "sc014034",
			"id": "1236A13A-C8E3-AFB3-95A3-6E633DC6532E"
		},
		{
			"etask.entity": "sc014039",
			"id": "BDEDD6D3-C16E-87DF-F0C9-F4F268E462AF"
		},
		{
			"etask.entity": "sc014044",
			"id": "07FC6F9B-BD5E-0338-2E14-0A0F1061798F"
		},
		{
			"etask.entity": "sc014046",
			"id": "053DAC69-323C-4793-5EE8-C45217BB63BD"
		},
		{
			"etask.entity": "sc014051",
			"id": "BA67C9C6-846E-15FB-10E6-11F9B2F241EC"
		},
		{
			"etask.entity": "sc014056",
			"id": "9D310528-A6CB-E19A-8106-DED639B678A1"
		},
		{
			"etask.entity": "sc014061",
			"id": "B2A83869-547B-FEB5-77D1-9BDC8836FA82"
		},
		{
			"etask.entity": "sc014066",
			"id": "D7CEE2F7-B75E-220D-7AF7-4081AF3FF38F"
		},
		{
			"etask.entity": "sc023617",
			"id": "A2AE5C0B-5891-807F-7398-59405CEDA8AF"
		},
		{
			"etask.entity": "sc017145",
			"id": "C2AFBC69-BD38-9CE6-4635-F89F1F40B12B"
		},
		{
			"etask.entity": "sc017146",
			"id": "A1F87353-E873-E473-0904-8FDEB2C77ACB"
		},
		{
			"etask.entity": "sc017147",
			"id": "EA67261A-3566-2E2D-F065-F991E07D2D7B"
		},
		{
			"etask.entity": "sc017148",
			"id": "BDEE891E-DA7A-95FF-826F-D39A42112594"
		},
		{
			"etask.entity": "sc017150",
			"id": "6087C883-75C8-C6CF-C3F3-28EBB6889128"
		},
		{
			"etask.entity": "sc017151",
			"id": "6F2A5F23-C131-CC3C-6247-024C36B5AA12"
		},
		{
			"etask.entity": "sc017152",
			"id": "01A2544D-4A2E-29AD-75C6-22A322302B74"
		},
		{
			"etask.entity": "sc017153",
			"id": "B4969394-8386-7142-3260-771B6851C67E"
		},
		{
			"etask.entity": "sc017155",
			"id": "40FFEE95-06EB-C70A-583D-F12EE8856F86"
		},
		{
			"etask.entity": "sc017156",
			"id": "6454CF76-C330-2661-E51B-156538E37F86"
		},
		{
			"etask.entity": "sc017157",
			"id": "E71A990F-A3B6-2DD4-749E-A0C0E8C4686B"
		},
		{
			"etask.entity": "sc017158",
			"id": "64D11DDD-DE35-8769-FE8F-E46CBA135B16"
		},
		{
			"etask.entity": "sc017160",
			"id": "AB9824FE-F4DF-C47E-964B-0A3342AFC8BC"
		},
		{
			"etask.entity": "sc017161",
			"id": "141B186E-0520-D6EE-A028-FC352D7A7FA5"
		},
		{
			"etask.entity": "sc017162",
			"id": "E9FD5A23-EA3A-FA18-8B77-74D3455FE027"
		},
		{
			"etask.entity": "sc017163",
			"id": "39D2A77A-1DFB-AB83-08A1-E0A89499879D"
		},
		{
			"etask.entity": "sc017165",
			"id": "1FE86F86-EDB0-38FE-E7EB-AE0B55A781BD"
		},
		{
			"etask.entity": "sc023618",
			"id": "B30B42E1-5DCD-08A1-3229-0CDF2BFDA763"
		},
		{
			"etask.entity": "sc017167",
			"id": "CFE8DD14-C777-D233-F7F5-4B7557E0DF66"
		},
		{
			"etask.entity": "sc017168",
			"id": "B6E0B145-7732-18F5-2171-F01291FFBDDC"
		},
		{
			"etask.entity": "sc017169",
			"id": "ADAB79E9-3D16-8ADD-3006-03139B3B7CD1"
		},
		{
			"etask.entity": "sc017170",
			"id": "AC411AE5-B627-A165-4F28-F0967232524A"
		},
		{
			"etask.entity": "sc017172",
			"id": "699EA112-D3B5-3A0C-1838-3C0A65A533A9"
		},
		{
			"etask.entity": "sc017173",
			"id": "A5588732-61D6-E940-F3F0-60A668046ACC"
		},
		{
			"etask.entity": "sc017174",
			"id": "D6CA982B-810D-8CD6-E7B8-3C675AC40F7D"
		},
		{
			"etask.entity": "sc017175",
			"id": "C050D016-2D71-19B2-F1DC-726A9FBA2C7A"
		},
		{
			"etask.entity": "sc017177",
			"id": "640251D4-C7CF-02B4-F80A-5393C662AE72"
		},
		{
			"etask.entity": "sc017178",
			"id": "41F279D8-83D4-A0FF-608D-01033060A562"
		},
		{
			"etask.entity": "sc017179",
			"id": "311F3C8C-2D61-3855-E1D9-96BF60D366C0"
		},
		{
			"etask.entity": "sc017180",
			"id": "DB61010E-3513-2446-7286-36E18D56E2B1"
		},
		{
			"etask.entity": "sc017182",
			"id": "B764F6D4-0569-12C7-4F08-6EEA68761A7A"
		},
		{
			"etask.entity": "sc017183",
			"id": "9ECDD8E3-3491-0D42-52AD-49055BC54ED7"
		},
		{
			"etask.entity": "sc017184",
			"id": "69EF42C8-FF08-B874-7349-C7E76964BCF3"
		},
		{
			"etask.entity": "sc017185",
			"id": "4A1C40EE-271D-3D7F-F1D2-025316218CC0"
		},
		{
			"etask.entity": "sc017187",
			"id": "A2D50834-D4F6-57EA-ECFF-FC6F155739F4"
		},
		{
			"etask.entity": "sc023619",
			"id": "C50084AE-CBF4-8B45-E4DE-7492B6B5C00E"
		},
		{
			"etask.entity": "sc017189",
			"id": "1F12E4AD-B357-8403-7A60-7531033E1F4D"
		},
		{
			"etask.entity": "sc017190",
			"id": "810CF21B-9670-76B8-1DB7-84162234AAAE"
		},
		{
			"etask.entity": "sc017191",
			"id": "FD4CDFF5-5FAD-6F3F-AF09-CB7C7AC29A86"
		},
		{
			"etask.entity": "sc017192",
			"id": "BD77C0BA-4E3E-3C90-5502-CA72BEDBF4EB"
		},
		{
			"etask.entity": "sc017194",
			"id": "98D600DE-5611-9FCC-75DE-5D2C71E155E2"
		},
		{
			"etask.entity": "sc017195",
			"id": "B906A60D-719C-4D8F-6821-FEC630F09C99"
		},
		{
			"etask.entity": "sc017196",
			"id": "4A82D034-D141-309D-DA8A-E195CEE6F21D"
		},
		{
			"etask.entity": "sc017197",
			"id": "A13DE701-ECAA-86CE-BC64-480D048F734B"
		},
		{
			"etask.entity": "sc017199",
			"id": "2DE7DC59-8640-8772-91B5-8A42AC5A61AA"
		},
		{
			"etask.entity": "sc017200",
			"id": "41FBF7C5-35BA-9197-73F1-83E2540F911B"
		},
		{
			"etask.entity": "sc017201",
			"id": "6A829A72-8C89-A58B-0344-3C6E4A5033CD"
		},
		{
			"etask.entity": "sc017202",
			"id": "45F272A9-7F9E-281B-6054-ACABC093B60A"
		},
		{
			"etask.entity": "sc017204",
			"id": "04730118-1EF9-AC3D-E118-963F32EE6FF4"
		},
		{
			"etask.entity": "sc017205",
			"id": "8C992051-1EF5-E580-27F4-3E991F1DCA20"
		},
		{
			"etask.entity": "sc017206",
			"id": "103F782D-96E5-262D-54BC-5468F94BFC4C"
		},
		{
			"etask.entity": "sc017207",
			"id": "CD4BCF61-5CDC-F5FE-6D71-2311EFEF6924"
		},
		{
			"etask.entity": "sc017209",
			"id": "9446F5F9-968C-FFB3-D46F-981F5F879998"
		},
		{
			"etask.entity": "sc023620",
			"id": "A8137047-1CA9-EB23-1D0F-352A01242ED8"
		},
		{
			"etask.entity": "sc017211",
			"id": "3D15F1CB-E1A9-45BE-07F9-5B47FB833ECD"
		},
		{
			"etask.entity": "sc017212",
			"id": "7F575576-B5A9-38EA-8CDF-F75594DE6434"
		},
		{
			"etask.entity": "sc017213",
			"id": "AE9F108E-C580-F066-5A13-3CE0AB2CFFAC"
		},
		{
			"etask.entity": "sc017214",
			"id": "A3855C7A-5BDF-E288-7516-71651E279D91"
		},
		{
			"etask.entity": "sc017216",
			"id": "EE55448C-8233-0977-696F-7EE3CC07A5FB"
		},
		{
			"etask.entity": "sc017217",
			"id": "FCB48B90-DD42-9AA3-7599-498BA86EA201"
		},
		{
			"etask.entity": "sc017218",
			"id": "5BC3B653-AC2A-4E81-EE60-7C8481028603"
		},
		{
			"etask.entity": "sc017219",
			"id": "04CBEC68-D7D2-FE62-5DC2-07080CCA030B"
		},
		{
			"etask.entity": "sc017221",
			"id": "F674D862-84BF-8002-DF7D-3F986BE531A6"
		},
		{
			"etask.entity": "sc017222",
			"id": "4322F51C-91D9-A82B-B3B6-9519CE993C18"
		},
		{
			"etask.entity": "sc017223",
			"id": "D230BE47-D2CA-9377-C523-8C40820456BB"
		},
		{
			"etask.entity": "sc017224",
			"id": "E4B2FD94-E318-0A62-01C0-E35E05D8C934"
		},
		{
			"etask.entity": "sc017226",
			"id": "B3664C48-55FD-4B7B-997F-2BA0FD065441"
		},
		{
			"etask.entity": "sc017227",
			"id": "37BE98BE-E2D1-1F5F-3911-18C10B3B5906"
		},
		{
			"etask.entity": "sc017228",
			"id": "0E611E6E-903A-E4F2-EA83-5B641D73C6E1"
		},
		{
			"etask.entity": "sc017229",
			"id": "B6B6C47B-AF1B-0A56-4096-8F5D30E47074"
		},
		{
			"etask.entity": "sc017231",
			"id": "0ED2D0A4-7FB0-A4FE-8D8E-03E7CB8A75F4"
		},
		{
			"etask.entity": "sc014068",
			"id": "5E5AB640-5830-44A4-B560-7138467C5F4C"
		},
		{
			"etask.entity": "sc014073",
			"id": "9BCB0826-CA40-44A9-8C45-EA54A06CD7D1"
		},
		{
			"etask.entity": "sc014078",
			"id": "DC925765-DC9D-7EEA-F88E-9C4B45857E11"
		},
		{
			"etask.entity": "sc014083",
			"id": "2A5ECF6B-02D3-6BAE-32B8-D0CCF90E9E2F"
		},
		{
			"etask.entity": "sc014088",
			"id": "C28DC84A-0DB8-A2DE-2568-F7165D05B522"
		},
		{
			"etask.entity": "sc014090",
			"id": "1AC5B1E7-96D2-49C6-81A4-7D37B6F70459"
		},
		{
			"etask.entity": "sc014095",
			"id": "7BF957FE-A988-9D85-CBA5-AFED88D02854"
		},
		{
			"etask.entity": "sc014100",
			"id": "3F4407AF-2D00-A757-E441-D10FFB63B4B1"
		},
		{
			"etask.entity": "sc014105",
			"id": "D4CF361F-C2B1-F4BC-05AD-16F1F8B77154"
		},
		{
			"etask.entity": "sc014110",
			"id": "BC0156A7-98C5-24BE-0985-59C0D16663C2"
		},
		{
			"etask.entity": "sc014112",
			"id": "11FDD145-B932-923E-9693-D18EDBDB928E"
		},
		{
			"etask.entity": "sc014117",
			"id": "BE87ECD4-AF31-2C91-F177-BF9CDF59EDAE"
		},
		{
			"etask.entity": "sc014122",
			"id": "5DC25620-0ABD-4203-1662-27694ADA2538"
		},
		{
			"etask.entity": "sc014127",
			"id": "0CA0A13E-F676-28FE-2CB1-9DE24FE91147"
		},
		{
			"etask.entity": "sc014132",
			"id": "3FB3D502-A288-0F56-6FCA-BE4AA54CACFF"
		},
		{
			"etask.entity": "sc014134",
			"id": "21E458BE-BD99-5725-4F3D-48102B02BE39"
		},
		{
			"etask.entity": "sc014139",
			"id": "E4591ED2-45C8-0E9B-20B9-72CDF76ECCED"
		},
		{
			"etask.entity": "sc014144",
			"id": "EE59A692-DE8C-821F-E8D0-7D8686B1BAC8"
		},
		{
			"etask.entity": "sc023621",
			"id": "DBEFB31D-A5D7-993F-B028-B36D5E3D54DF"
		},
		{
			"etask.entity": "sc017233",
			"id": "B64A6B0A-4057-E18F-F962-45034FA92DDB"
		},
		{
			"etask.entity": "sc017234",
			"id": "2932752A-60EA-6E49-BFE4-E9E66CB3464C"
		},
		{
			"etask.entity": "sc017235",
			"id": "A408B5B1-F5DF-D890-490F-53288AEF2902"
		},
		{
			"etask.entity": "sc017236",
			"id": "70919334-AAF2-3577-97CC-20C2CA1B44C7"
		},
		{
			"etask.entity": "sc017238",
			"id": "6992FF31-BE39-B1EC-F5C0-8AF4BA96F24C"
		},
		{
			"etask.entity": "sc017239",
			"id": "AD7B7888-8481-054B-211A-9A94318F9847"
		},
		{
			"etask.entity": "sc017240",
			"id": "E89A0018-770A-8723-B4B8-BD377A79D7A5"
		},
		{
			"etask.entity": "sc017241",
			"id": "49F0AD0F-8B2A-71B2-7E4B-16BC9B02E43A"
		},
		{
			"etask.entity": "sc017243",
			"id": "3D73DCA1-EE65-B4E2-1F0F-EA3B0AB5C3DA"
		},
		{
			"etask.entity": "sc017244",
			"id": "A0574657-2D0D-9322-4C3A-DC9C6FCDC36C"
		},
		{
			"etask.entity": "sc017245",
			"id": "BCD2FFAD-23D3-2AB6-D6E4-8460195F5349"
		},
		{
			"etask.entity": "sc017246",
			"id": "7C9242B7-D430-6908-EAE4-CE039FFA2B61"
		},
		{
			"etask.entity": "sc017248",
			"id": "A49F1CF8-3A33-D344-8065-6AFD1D80FCB1"
		},
		{
			"etask.entity": "sc017249",
			"id": "10D6BBC9-A62E-EE7A-4BD0-B8823AB3A8DC"
		},
		{
			"etask.entity": "sc017250",
			"id": "5A8695AE-F553-6F41-F1C0-9C6DA54D952C"
		},
		{
			"etask.entity": "sc017251",
			"id": "E044A71D-4F18-25A9-C56E-044CDFABF708"
		},
		{
			"etask.entity": "sc017253",
			"id": "5028EB12-8DC9-DC35-57C5-3B4D9BE93443"
		},
		{
			"etask.entity": "sc023622",
			"id": "1899F83C-8206-114E-FB07-3F3E00F45081"
		},
		{
			"etask.entity": "sc017255",
			"id": "F6F77DB2-C12B-FA81-FE89-55694DFAF7E8"
		},
		{
			"etask.entity": "sc017256",
			"id": "E8C9E29A-61B8-FE42-3084-B9644C25778A"
		},
		{
			"etask.entity": "sc017257",
			"id": "7624D5CA-3D96-CC17-C758-3ED6F919AF3E"
		},
		{
			"etask.entity": "sc017258",
			"id": "8029475C-9032-1628-6092-2AADE6C326BD"
		},
		{
			"etask.entity": "sc017260",
			"id": "0BADC51E-FCCE-04AB-3EF7-CA8368AA3CAC"
		},
		{
			"etask.entity": "sc017261",
			"id": "C162DA0C-1FD0-CC62-FAEA-1B8A2F368F16"
		},
		{
			"etask.entity": "sc017262",
			"id": "B8A9C2AA-ED37-0824-90D0-935B6FA5B9A1"
		},
		{
			"etask.entity": "sc017263",
			"id": "E4F66D39-C7C7-F1CE-7E59-A933964DC6C5"
		},
		{
			"etask.entity": "sc017265",
			"id": "99843352-060E-A059-A2E5-CA454FF31703"
		},
		{
			"etask.entity": "sc017266",
			"id": "93593FD3-491A-EB78-400E-D21F71A2CE35"
		},
		{
			"etask.entity": "sc017267",
			"id": "2A45E95A-2A7A-4747-7B87-786C40CAA770"
		},
		{
			"etask.entity": "sc017268",
			"id": "3FF4BBBB-EF7C-295C-2308-113FFE06F050"
		},
		{
			"etask.entity": "sc017270",
			"id": "72FC5D71-837D-7EB2-AF3D-83E8425E731E"
		},
		{
			"etask.entity": "sc017271",
			"id": "696E9195-FD73-296B-AF64-8413853151B5"
		},
		{
			"etask.entity": "sc017272",
			"id": "5C541C08-4F77-DE73-3ED2-F8C39896FF19"
		},
		{
			"etask.entity": "sc017273",
			"id": "C3373C76-8A7B-F35F-45A2-14D3ACBB3501"
		},
		{
			"etask.entity": "sc017275",
			"id": "92EEDC58-98B5-3FEB-C94C-1C0183680B4A"
		},
		{
			"etask.entity": "sc023623",
			"id": "919A3A80-4B63-BCF2-A1AF-A95BE17360D7"
		},
		{
			"etask.entity": "sc017277",
			"id": "4C19A316-84FF-C91B-4C36-DF3A1DF93994"
		},
		{
			"etask.entity": "sc017278",
			"id": "B53AEE91-E243-2F66-6CE2-1E7F491DCCAF"
		},
		{
			"etask.entity": "sc017279",
			"id": "A7DD24E3-832D-FD2B-84D7-00B7163C769B"
		},
		{
			"etask.entity": "sc017280",
			"id": "DEC80EE7-B591-F5CF-5B5D-16E55F3EAF58"
		},
		{
			"etask.entity": "sc017282",
			"id": "7FCF8475-BAD9-6BC1-E9BC-FE5C47AA0EAA"
		},
		{
			"etask.entity": "sc017283",
			"id": "0E195EAE-AC78-5DE4-F32A-6127693C2909"
		},
		{
			"etask.entity": "sc017284",
			"id": "B43B5027-6B7B-DF0F-C39F-2EEE5BFA2AB9"
		},
		{
			"etask.entity": "sc017285",
			"id": "314CEE8B-7C57-598B-B7A5-8D1D557E9C1A"
		},
		{
			"etask.entity": "sc017287",
			"id": "5C79C043-C2BD-09FE-3D8B-42DF6D477A48"
		},
		{
			"etask.entity": "sc017288",
			"id": "BB981CE6-515E-0508-2B0B-B859B1F2216A"
		},
		{
			"etask.entity": "sc017289",
			"id": "D2E79EEF-FFC6-054F-1A84-F326F4CFB578"
		},
		{
			"etask.entity": "sc017290",
			"id": "A388C2A3-EC8D-7ED6-63C9-4F1B9B6E34CD"
		},
		{
			"etask.entity": "sc017292",
			"id": "FDC2A3AF-0CA2-922A-94DA-F6360B532AAB"
		},
		{
			"etask.entity": "sc017293",
			"id": "15DFDF96-19CA-7AEB-6446-C72518E4C743"
		},
		{
			"etask.entity": "sc017294",
			"id": "38B46383-2B1C-48ED-E0F6-20DD92775294"
		},
		{
			"etask.entity": "sc017295",
			"id": "D570E2BD-CA63-DB51-6E3A-029EC56575EF"
		},
		{
			"etask.entity": "sc017297",
			"id": "A47E75B0-73CE-2320-47A3-7BAE4F9AA0AC"
		},
		{
			"etask.entity": "sc023624",
			"id": "530F57A2-BF5C-AC4C-F9BD-542634430178"
		},
		{
			"etask.entity": "sc017299",
			"id": "D7D671B0-916D-51F7-96B0-60E65F0327EB"
		},
		{
			"etask.entity": "sc017300",
			"id": "013707B7-C2BF-67C3-3706-EF16F3F2F0B9"
		},
		{
			"etask.entity": "sc017301",
			"id": "70569B60-49A7-79AE-44BA-70A20431615B"
		},
		{
			"etask.entity": "sc017302",
			"id": "AF9F2B85-A095-D33B-EE11-EC79532D3CBA"
		},
		{
			"etask.entity": "sc017304",
			"id": "8E2D88EE-6433-F731-AABF-6F9652EDFFB7"
		},
		{
			"etask.entity": "sc017305",
			"id": "F241AC57-78AA-1343-5670-7DF389B2FAA4"
		},
		{
			"etask.entity": "sc017306",
			"id": "583F5C7A-24D0-1398-8CAE-9EE56A686DB3"
		},
		{
			"etask.entity": "sc017307",
			"id": "9E55E3DF-175E-C887-44A3-43EDF00A5267"
		},
		{
			"etask.entity": "sc017309",
			"id": "A50B5B75-1A71-BA20-1607-C9BC5582AB8F"
		},
		{
			"etask.entity": "sc017310",
			"id": "5A69BB49-381E-B8CC-AC43-67090E9006DD"
		},
		{
			"etask.entity": "sc017311",
			"id": "9AB9837C-0605-D925-3774-EA9749258D66"
		},
		{
			"etask.entity": "sc017312",
			"id": "519E1929-20A1-8FA8-0B02-A63DF4CDA2C6"
		},
		{
			"etask.entity": "sc017314",
			"id": "6905F0AA-BF33-40F4-6C9B-614A96DC63CF"
		},
		{
			"etask.entity": "sc017315",
			"id": "3BA04AD6-4D6A-857F-6337-58BE19ED9EAE"
		},
		{
			"etask.entity": "sc017316",
			"id": "CA26EE3F-290C-8C31-316E-42B0DD51220D"
		},
		{
			"etask.entity": "sc017317",
			"id": "D7BC9229-2B25-A998-25D3-9E4FC121A977"
		},
		{
			"etask.entity": "sc017319",
			"id": "AF255BF4-B5FF-5475-423F-A98D64459B8D"
		},
		{
			"etask.entity": "sc014149",
			"id": "8D35B8E0-8E3F-2F58-066D-A55F67BB05FB"
		},
		{
			"etask.entity": "sc014154",
			"id": "E345FACE-5306-35CC-E461-99EE2D2E9DF0"
		},
		{
			"etask.entity": "sc014156",
			"id": "47BC752C-E207-35D0-12A5-C187D283B204"
		},
		{
			"etask.entity": "sc014161",
			"id": "703C3E4F-761E-2106-A797-4606A05BE3C4"
		},
		{
			"etask.entity": "sc014166",
			"id": "0BC93DD2-9DB3-8D92-9168-647B81D3E42A"
		},
		{
			"etask.entity": "sc014171",
			"id": "2EF0A1CF-F0AC-0A06-611F-A62F5EDA5EA4"
		},
		{
			"etask.entity": "sc014176",
			"id": "C7530B70-7492-7634-8E57-7630ED5FC4ED"
		},
		{
			"etask.entity": "sc014178",
			"id": "A995DC61-9B63-C7A3-E4B6-E587FFA1C8A1"
		},
		{
			"etask.entity": "sc014183",
			"id": "61F4024E-FE19-D272-04AC-A7C414C685C0"
		},
		{
			"etask.entity": "sc014188",
			"id": "C7156564-CA02-4E3C-5747-D1172B70156D"
		},
		{
			"etask.entity": "sc014193",
			"id": "CF44A1B8-9565-C5C2-764C-2452FB3CFEA5"
		},
		{
			"etask.entity": "sc014198",
			"id": "D458A6DC-EF9E-EF21-0AF1-F88FECD6E1CF"
		},
		{
			"etask.entity": "sc014200",
			"id": "584215AA-2118-2161-41D1-D9A3C689CDDB"
		},
		{
			"etask.entity": "sc014205",
			"id": "C4178E7D-0AC5-463A-4A86-4FA18416DF07"
		},
		{
			"etask.entity": "sc014210",
			"id": "8C578CC6-85DD-9DA8-CD14-1B8BF970D1C4"
		},
		{
			"etask.entity": "sc014215",
			"id": "52845983-4DAF-E313-F7EB-553A208253DC"
		},
		{
			"etask.entity": "sc014220",
			"id": "E4C1FA6A-D983-B5B0-4F9E-C4FF05C7F9B4"
		},
		{
			"etask.entity": "sc014222",
			"id": "D3F7CA2C-56A0-8983-7E59-C70CD6E3B45C"
		},
		{
			"etask.entity": "sc023625",
			"id": "E469DB79-7B37-1602-F591-294A555322CA"
		},
		{
			"etask.entity": "sc017321",
			"id": "7E48305E-8453-140A-B4E6-96E05F6BDE7D"
		},
		{
			"etask.entity": "sc017322",
			"id": "FABE074C-A62B-0300-91E7-309393D46B25"
		},
		{
			"etask.entity": "sc017323",
			"id": "74EC35AA-A723-BD28-D9C5-53E5437E4E87"
		},
		{
			"etask.entity": "sc017324",
			"id": "0394F095-2307-5EE7-C9AB-611AB86E9385"
		},
		{
			"etask.entity": "sc017326",
			"id": "9D6F8B56-DDBC-E1F1-D724-A8C097CFFB33"
		},
		{
			"etask.entity": "sc017327",
			"id": "1DA48CB9-7BF0-37E0-8B0A-176966B47103"
		},
		{
			"etask.entity": "sc017328",
			"id": "6EE4F29E-0C58-245F-29AD-4FD049B2CC03"
		},
		{
			"etask.entity": "sc017329",
			"id": "28AAEA33-B921-1B1D-554F-4E0C4F32E43B"
		},
		{
			"etask.entity": "sc017331",
			"id": "4171E108-B732-69A9-7FD5-3AC4AE622A74"
		},
		{
			"etask.entity": "sc017332",
			"id": "EF70E2CB-6DE8-0DEF-5DBF-F50DF1467B1D"
		},
		{
			"etask.entity": "sc017333",
			"id": "78C91AC6-A87F-C589-00E2-1933EAB14836"
		},
		{
			"etask.entity": "sc017334",
			"id": "48DC3F96-732A-9A1A-336B-6F7F77323B1B"
		},
		{
			"etask.entity": "sc017336",
			"id": "2167D18D-7BB3-610C-C2C9-44DB17184EA6"
		},
		{
			"etask.entity": "sc017337",
			"id": "D200B021-25F7-CE1E-AFFD-F597027D17EF"
		},
		{
			"etask.entity": "sc017338",
			"id": "208BEFF2-A1F0-1963-EAC6-1D36F7E896C9"
		},
		{
			"etask.entity": "sc017339",
			"id": "AF30E0E1-6948-BF0A-8539-EF5E0787B260"
		},
		{
			"etask.entity": "sc017341",
			"id": "4A4585DF-AAFB-A8ED-2FBE-D537AE4FE0C4"
		},
		{
			"etask.entity": "sc023626",
			"id": "E08DC016-2289-D48B-273B-9616FA025527"
		},
		{
			"etask.entity": "sc017343",
			"id": "0BCA83EE-34B0-AB28-2682-1E484E3E3671"
		},
		{
			"etask.entity": "sc017344",
			"id": "85FA434F-9754-E1E2-784E-AF4E369ABEE3"
		},
		{
			"etask.entity": "sc017345",
			"id": "AAC1703D-6982-DFC9-A387-B2F2AFECE4E1"
		},
		{
			"etask.entity": "sc017346",
			"id": "A9666615-0101-9A46-FE16-78C4283C4370"
		},
		{
			"etask.entity": "sc017348",
			"id": "DACA5152-1121-E327-9D31-5BCD3F64B400"
		},
		{
			"etask.entity": "sc017349",
			"id": "C6D09B8D-9E98-60DA-7627-9170E034678B"
		},
		{
			"etask.entity": "sc017350",
			"id": "85EBC237-E230-EADD-A6E6-3D567FE558D3"
		},
		{
			"etask.entity": "sc017351",
			"id": "EF85F0A4-BA12-E8B0-8F66-5E286D30B3A5"
		},
		{
			"etask.entity": "sc017353",
			"id": "D63582B3-3CDD-C198-FCB7-FD2268D02FA9"
		},
		{
			"etask.entity": "sc017354",
			"id": "BE71AF2B-84B8-4F24-E9F4-3D26BA85DF8C"
		},
		{
			"etask.entity": "sc017355",
			"id": "02DECEE6-0A21-58B3-52FF-CD62A7277593"
		},
		{
			"etask.entity": "sc017356",
			"id": "1CC7863F-18EA-41C3-2F40-7B50CA7ABE69"
		},
		{
			"etask.entity": "sc017358",
			"id": "F956F5AC-7346-66B1-91AD-80115A82F8E1"
		},
		{
			"etask.entity": "sc017359",
			"id": "665FDC3B-F23B-BC23-E947-90BBFCC84E8D"
		},
		{
			"etask.entity": "sc017360",
			"id": "61073C4E-C48C-1AA8-8C63-859FF6C3A154"
		},
		{
			"etask.entity": "sc017361",
			"id": "CC257CBF-765C-D301-5AE6-8FDAD962A37E"
		},
		{
			"etask.entity": "sc017363",
			"id": "31744730-9FD3-AA1B-1698-0403DDB236CC"
		},
		{
			"etask.entity": "sc023627",
			"id": "AC085ED3-D571-C020-707A-208B5C6697EF"
		},
		{
			"etask.entity": "sc017365",
			"id": "D07F8565-128D-90CA-33A8-C7387E3E73CD"
		},
		{
			"etask.entity": "sc017366",
			"id": "14028463-5A38-0AB3-13F8-9C5B69539EEF"
		},
		{
			"etask.entity": "sc017367",
			"id": "9994594C-EFF8-5A61-49D5-7EE4D1ACB3EE"
		},
		{
			"etask.entity": "sc017368",
			"id": "DBB25AC2-CCBF-1CCC-3641-09AD81946C6D"
		},
		{
			"etask.entity": "sc017370",
			"id": "794DE74E-7E4E-4B64-80CE-0A8CE87B322B"
		},
		{
			"etask.entity": "sc017371",
			"id": "6E05A0E1-2BEE-30CC-F1CB-CB3EE0F7ADBA"
		},
		{
			"etask.entity": "sc017372",
			"id": "67AE6F9E-4BB0-023D-6A38-567C4A31AD5E"
		},
		{
			"etask.entity": "sc017373",
			"id": "BF7E2E08-0224-C52A-1F2A-A1EE34E4407F"
		},
		{
			"etask.entity": "sc017375",
			"id": "18D525BA-5F33-759E-6104-9EC88AAE966E"
		},
		{
			"etask.entity": "sc017376",
			"id": "F7C44403-141A-69F0-7218-CCA0EB927DCA"
		},
		{
			"etask.entity": "sc017377",
			"id": "8443819C-C535-6607-6E64-388AB1EEA5F5"
		},
		{
			"etask.entity": "sc017378",
			"id": "1AD2C97F-8CC2-C4C7-5C3A-D122643F51B0"
		},
		{
			"etask.entity": "sc017380",
			"id": "FB6C50AE-2A2D-72C9-6212-C3C9EDBAC724"
		},
		{
			"etask.entity": "sc017381",
			"id": "AFBC08A1-E4BF-BE16-85E6-84239683CFCB"
		},
		{
			"etask.entity": "sc017382",
			"id": "75FE6E15-4A4E-221C-BCE6-3C11302A2E57"
		},
		{
			"etask.entity": "sc017383",
			"id": "D5AF59E0-6A4A-4339-54A2-06E573715CE8"
		},
		{
			"etask.entity": "sc017385",
			"id": "B34C9B8C-CD2D-4A67-4B00-369454635842"
		},
		{
			"etask.entity": "sc014227",
			"id": "1E3B2619-B60B-8C1A-0E2E-CE4CEAB9E31A"
		},
		{
			"etask.entity": "sc014232",
			"id": "E48207D3-B681-A2A4-5BE0-08D8F449B900"
		},
		{
			"etask.entity": "sc014237",
			"id": "700BFD95-0713-CA46-25B2-37AD7A7B9919"
		},
		{
			"etask.entity": "sc014242",
			"id": "65FE8743-3622-EE13-A9B5-A140B7BCA66B"
		},
		{
			"etask.entity": "sc014244",
			"id": "122FB3D5-981F-5278-34E8-FF3E20954ABB"
		},
		{
			"etask.entity": "sc014249",
			"id": "4BC5CA7F-73E2-A262-BA44-BDB7A676A9A4"
		},
		{
			"etask.entity": "sc014254",
			"id": "3003483F-E5B7-DD4D-A0C8-6366ECA760B8"
		},
		{
			"etask.entity": "sc014259",
			"id": "C5522512-399D-140F-ABFF-7E5A57807DDC"
		},
		{
			"etask.entity": "sc014264",
			"id": "AA7738BE-B9CD-B4AC-6B64-4FAD8F55C2CD"
		},
		{
			"etask.entity": "sc014266",
			"id": "5B0ADF10-FA9D-26D0-9883-4BBB30D61F5E"
		},
		{
			"etask.entity": "sc014271",
			"id": "1CA392BE-EC1B-E8C1-54D0-BF808324DB26"
		},
		{
			"etask.entity": "sc014276",
			"id": "9FCB5BFE-0AB0-5EC8-7223-8CBF9C90150B"
		},
		{
			"etask.entity": "sc014281",
			"id": "A71AA361-70A2-D119-4BBE-2AD0E4733C0C"
		},
		{
			"etask.entity": "sc014286",
			"id": "2E649633-F181-93C0-CB4F-D4C90197E6EB"
		},
		{
			"etask.entity": "sc014288",
			"id": "3CA412C9-7482-E152-F3AC-64047FEA6BB7"
		},
		{
			"etask.entity": "sc014293",
			"id": "3E7BE6C6-CEF9-8771-1942-CF8B9317B4C6"
		},
		{
			"etask.entity": "sc014298",
			"id": "F06E3D04-38AA-33B2-5A2B-881C17C12209"
		},
		{
			"etask.entity": "sc014303",
			"id": "B7063A67-F39F-2353-0D89-2612151D702F"
		},
		{
			"etask.entity": "sc023628",
			"id": "4E75D26C-B1EE-16C2-EBA4-88798611798F"
		},
		{
			"etask.entity": "sc017387",
			"id": "F6D49414-A6AC-DCC2-FB3E-4172313B485C"
		},
		{
			"etask.entity": "sc017388",
			"id": "A8405C26-F818-69D9-0695-7443BE72B9CF"
		},
		{
			"etask.entity": "sc017389",
			"id": "E14323A0-161B-F4DA-D18D-8C4CD4CE3276"
		},
		{
			"etask.entity": "sc017390",
			"id": "974046F2-545F-152B-D956-A7C1C174510C"
		},
		{
			"etask.entity": "sc017392",
			"id": "4E31B732-F7DB-0ED2-8BB7-A3BC28D1E3FC"
		},
		{
			"etask.entity": "sc017393",
			"id": "2A2CC73B-B90F-589F-4375-F2CA3808F731"
		},
		{
			"etask.entity": "sc017394",
			"id": "23D0E19B-201A-F7ED-469B-D0D45730800A"
		},
		{
			"etask.entity": "sc017395",
			"id": "C7187777-FDDF-97DE-A04A-3AE33FFE2C7B"
		},
		{
			"etask.entity": "sc017397",
			"id": "B50995E6-8846-9A9E-E2BF-863B2D9E8565"
		},
		{
			"etask.entity": "sc017398",
			"id": "E4F87E51-FCBD-D767-AB86-DFC8798733E6"
		},
		{
			"etask.entity": "sc017399",
			"id": "FA0D23A5-880E-1043-B5FD-79135E652F33"
		},
		{
			"etask.entity": "sc017400",
			"id": "B85DDE72-2FC7-6295-0855-DF9BC977E2B8"
		},
		{
			"etask.entity": "sc017402",
			"id": "3907B5E1-0848-FB98-8955-B276AB122401"
		},
		{
			"etask.entity": "sc017403",
			"id": "DF449BA0-3001-E30D-234D-8D25BEBCC393"
		},
		{
			"etask.entity": "sc017404",
			"id": "E87F15D5-B409-6238-A834-F74377ECA646"
		},
		{
			"etask.entity": "sc017405",
			"id": "39E45D09-752A-FE7A-D067-C6B4CFB56586"
		},
		{
			"etask.entity": "sc017407",
			"id": "FFCC723D-C1CF-2CA2-953C-AF232264FDE5"
		},
		{
			"etask.entity": "sc023629",
			"id": "B8A3DF19-7B39-D944-7336-E580FD5AB8FF"
		},
		{
			"etask.entity": "sc017409",
			"id": "13D903B0-E3EE-DAE3-CCFB-869A1C5C5B6E"
		},
		{
			"etask.entity": "sc017410",
			"id": "C1F4794C-A02C-55E5-92A9-9295B2B8EA97"
		},
		{
			"etask.entity": "sc017411",
			"id": "D47B15B0-8ABB-74DD-CFBC-B9882C1EE75D"
		},
		{
			"etask.entity": "sc017412",
			"id": "A76C55EA-265C-F26A-7D66-785E4F2B5851"
		},
		{
			"etask.entity": "sc017414",
			"id": "8C6B5AD9-0B46-6ACF-8975-6731A98CF3E1"
		},
		{
			"etask.entity": "sc017415",
			"id": "DF7E2B53-5E8D-ABE2-12F1-F091446E052E"
		},
		{
			"etask.entity": "sc017416",
			"id": "F8B94BA9-750C-6E73-B8BD-DC5C84ACE3A4"
		},
		{
			"etask.entity": "sc017417",
			"id": "A1532B5A-4C6B-0366-485D-6EFA7DB495C6"
		},
		{
			"etask.entity": "sc017419",
			"id": "959AF1E0-2D70-E302-AF4C-5B0CCF316167"
		},
		{
			"etask.entity": "sc017420",
			"id": "A2AA9EA6-4EE3-360F-1D0F-324A63DF3BE6"
		},
		{
			"etask.entity": "sc017421",
			"id": "F4EDCF89-B998-E4A9-6364-082B8E76D703"
		},
		{
			"etask.entity": "sc017422",
			"id": "552708DD-CE2A-C5F3-1932-6C75080886EB"
		},
		{
			"etask.entity": "sc017424",
			"id": "EC3CD461-F7BF-C28C-C408-7B64BFA3042D"
		},
		{
			"etask.entity": "sc017425",
			"id": "E0A87013-9D0A-CEF3-52D7-F0753B627812"
		},
		{
			"etask.entity": "sc017426",
			"id": "E12A758A-2E22-A74D-E762-536D26D3F2CC"
		},
		{
			"etask.entity": "sc017427",
			"id": "7CD68976-8D0F-E2F2-30CD-0FDD0EDDAA1C"
		},
		{
			"etask.entity": "sc017429",
			"id": "32B18CA0-5648-2746-E9BC-C0E900A3571C"
		},
		{
			"etask.entity": "sc023630",
			"id": "775F3820-E3D1-5F29-5878-4B2F01EE2CF7"
		},
		{
			"etask.entity": "sc017431",
			"id": "27C555C1-C791-E979-4DD9-D881C6654DDC"
		},
		{
			"etask.entity": "sc017432",
			"id": "27BD9CCB-ABE4-1535-F45C-F25667B74C8F"
		},
		{
			"etask.entity": "sc017433",
			"id": "5A4EC42F-9486-E182-982F-01E5DDD023F4"
		},
		{
			"etask.entity": "sc017434",
			"id": "3B113EA2-261D-2A6A-CD27-8B66B848F035"
		},
		{
			"etask.entity": "sc017436",
			"id": "CC090EBC-AB25-4F43-8091-B69ED46BCCDE"
		},
		{
			"etask.entity": "sc017437",
			"id": "200B8762-450F-EC88-DC15-A9D3D4D0C281"
		},
		{
			"etask.entity": "sc017438",
			"id": "8C648C36-FFA6-1778-1D18-3C9DF2CA932A"
		},
		{
			"etask.entity": "sc017439",
			"id": "2AE87ACC-B09A-B610-E893-914EB9DF90E9"
		},
		{
			"etask.entity": "sc017441",
			"id": "C33B71FC-F6D1-33F4-A639-F2E0BDE9E450"
		},
		{
			"etask.entity": "sc017442",
			"id": "BA39E914-580B-CE61-3ED2-21F1BC0C149F"
		},
		{
			"etask.entity": "sc017443",
			"id": "36991E34-8340-D512-AD3B-54F371006C1F"
		},
		{
			"etask.entity": "sc017444",
			"id": "F1C99519-E519-977E-D8C2-45689EF0795D"
		},
		{
			"etask.entity": "sc017446",
			"id": "590BAA82-25D2-F960-7696-7DD2AEFEB20D"
		},
		{
			"etask.entity": "sc017447",
			"id": "441813B7-B863-2A5F-F22A-B015F5271926"
		},
		{
			"etask.entity": "sc017448",
			"id": "E4ABFF24-52BA-CE98-4EF0-632D90B63EC4"
		},
		{
			"etask.entity": "sc017449",
			"id": "5C889F4E-F208-F4CC-56A2-8B3A5892D6BB"
		},
		{
			"etask.entity": "sc017451",
			"id": "5B09BBC2-8D98-0FB1-4594-8008B364ED14"
		},
		{
			"etask.entity": "sc014308",
			"id": "62EBA991-1366-0EF7-AF23-2F1EF1A97FB7"
		},
		{
			"etask.entity": "sc014310",
			"id": "BEC3DE87-75AC-5878-9A93-C29314CD94FD"
		},
		{
			"etask.entity": "sc014315",
			"id": "2D3F457C-20F9-33BE-4740-991F494CE362"
		},
		{
			"etask.entity": "sc014320",
			"id": "25DBEE91-726A-08A0-7A75-94DE6FFE4F9C"
		},
		{
			"etask.entity": "sc014325",
			"id": "4B0A8D32-FDDD-D2C6-D1FC-23EE2D13844A"
		},
		{
			"etask.entity": "sc014330",
			"id": "549EC5D8-9539-90BB-B62E-BD5D56ED3326"
		},
		{
			"etask.entity": "sc014332",
			"id": "13F459F0-6ECB-2D1A-8E71-D68F01EF2E15"
		},
		{
			"etask.entity": "sc014337",
			"id": "C70C5366-3538-57AF-EA8A-A961B5AD5CDE"
		},
		{
			"etask.entity": "sc014342",
			"id": "2BA54D31-8377-0497-4B1A-CCECC40A92EC"
		},
		{
			"etask.entity": "sc014347",
			"id": "5F2A8942-A952-E91D-4394-9699EE74BAC5"
		},
		{
			"etask.entity": "sc014352",
			"id": "9CFB8153-B76A-FAE9-B098-43721433024E"
		},
		{
			"etask.entity": "sc014354",
			"id": "F8D0C2A0-8D9D-4FC8-0F6A-29617C00F6C7"
		},
		{
			"etask.entity": "sc014359",
			"id": "E66CB858-AD65-33C1-1DD0-F22D05C3726F"
		},
		{
			"etask.entity": "sc014364",
			"id": "9D972404-417F-1E3F-F67A-6A6FA34FD2CE"
		},
		{
			"etask.entity": "sc014369",
			"id": "B251118A-EE1A-FE71-4095-5A7F869379BD"
		},
		{
			"etask.entity": "sc014374",
			"id": "924855ED-73F3-E52E-BC62-C71704C167E3"
		},
		{
			"etask.entity": "sc014376",
			"id": "9F4B534C-5478-C83F-FD50-BD9B85464CBF"
		},
		{
			"etask.entity": "sc014381",
			"id": "6E931DC9-B25E-7809-80C5-4E83F31DAB74"
		},
		{
			"etask.entity": "sc023631",
			"id": "8AC53B4B-0BEE-CDB4-C205-37B549BB9CFD"
		},
		{
			"etask.entity": "sc017453",
			"id": "F47BEE9C-A63B-DFFB-945D-B54E6893BA39"
		},
		{
			"etask.entity": "sc017454",
			"id": "9A7F15D5-C436-B382-3BB8-B169A96354DA"
		},
		{
			"etask.entity": "sc017455",
			"id": "4DD5D4B5-248D-253A-019C-91B7C0BFEC00"
		},
		{
			"etask.entity": "sc017456",
			"id": "EDFF7427-9BB7-08AC-21FB-2E7B9EEDD326"
		},
		{
			"etask.entity": "sc017458",
			"id": "234DDB50-F799-1FCC-9318-226F1EBB2F80"
		},
		{
			"etask.entity": "sc017459",
			"id": "8E640F86-7D90-E171-786A-F7C3B84AE1E4"
		},
		{
			"etask.entity": "sc017460",
			"id": "5AC66491-278A-AC4D-631D-D2FC45B29891"
		},
		{
			"etask.entity": "sc017461",
			"id": "1666C79C-402B-0B53-EC4B-610AD6600F76"
		},
		{
			"etask.entity": "sc017463",
			"id": "03435D58-CA33-1922-D251-C3ACB9BBA52A"
		},
		{
			"etask.entity": "sc017464",
			"id": "C4EACAF9-BAB4-4D65-BEFD-B063A9192304"
		},
		{
			"etask.entity": "sc017465",
			"id": "DC701AFA-5A5C-AFAD-0218-4B91A21C994B"
		},
		{
			"etask.entity": "sc017466",
			"id": "7C3DA860-1911-8709-1DF2-847201D13A2E"
		},
		{
			"etask.entity": "sc017468",
			"id": "DF2B9E6C-80E1-6D2E-5024-E679D17DE5C6"
		},
		{
			"etask.entity": "sc017469",
			"id": "34393FEC-6B78-B60E-2B84-18DBA57EC588"
		},
		{
			"etask.entity": "sc017470",
			"id": "99EB8C66-F0F4-4BCF-6B82-79C1FBCCFDC9"
		},
		{
			"etask.entity": "sc017471",
			"id": "A6231B56-188B-FA2B-6AA4-96C26ED3FAB0"
		},
		{
			"etask.entity": "sc017473",
			"id": "20F867CB-5D68-4868-86C5-779D3B903B38"
		},
		{
			"etask.entity": "sc023632",
			"id": "F73C43E8-9543-8A26-FF6C-7389BEE7F1EC"
		},
		{
			"etask.entity": "sc017475",
			"id": "E88FF9EA-B623-2A95-524B-F66C69673888"
		},
		{
			"etask.entity": "sc017476",
			"id": "FFE714D1-8CE8-5632-510C-6C65966E2813"
		},
		{
			"etask.entity": "sc017477",
			"id": "4D5C9EEB-EB43-DE0F-60E2-D053344BCC74"
		},
		{
			"etask.entity": "sc017478",
			"id": "82B5A64A-5810-EC0F-3B38-1CE4DF94A8F1"
		},
		{
			"etask.entity": "sc017480",
			"id": "981C1EAC-6147-5605-760B-AE1AEBFC6C49"
		},
		{
			"etask.entity": "sc017481",
			"id": "86C730C1-8F98-54FF-A5FB-6F3E229C1F2E"
		},
		{
			"etask.entity": "sc017482",
			"id": "D0AFE9AF-F738-246D-19BB-65BB8B313274"
		},
		{
			"etask.entity": "sc017483",
			"id": "DEABB57C-1DFE-3955-657F-6FB0091EF652"
		},
		{
			"etask.entity": "sc017485",
			"id": "F31ECD12-05FD-64C3-3FFB-56D89202D096"
		},
		{
			"etask.entity": "sc017486",
			"id": "1756B821-A9D0-A47C-BD8E-67E188DE91DB"
		},
		{
			"etask.entity": "sc017487",
			"id": "C6421194-1B9C-1DA5-AD15-56D2C46F9462"
		},
		{
			"etask.entity": "sc017488",
			"id": "B76C7BC0-7E18-0CD0-3C27-1C15966284DD"
		},
		{
			"etask.entity": "sc017490",
			"id": "D5780AAB-DA42-47FA-5718-4A65EE22ACBD"
		},
		{
			"etask.entity": "sc017491",
			"id": "83D79C4A-C3CB-46E3-4512-A98910963986"
		},
		{
			"etask.entity": "sc017492",
			"id": "3259866B-B8D1-2D32-C5C2-FF1268772F87"
		},
		{
			"etask.entity": "sc017493",
			"id": "E1394294-3B61-E340-776E-E3E3068421EC"
		},
		{
			"etask.entity": "sc017495",
			"id": "72E4C57E-4842-1FCA-2C4A-3FF05C545654"
		},
		{
			"etask.entity": "sc023633",
			"id": "088DF9BC-6038-FD2E-0743-85EC9F9095F8"
		},
		{
			"etask.entity": "sc017497",
			"id": "9EF45E00-CB31-C428-DE44-504253F07D9D"
		},
		{
			"etask.entity": "sc017498",
			"id": "0EB8BDD1-7D27-48EE-3C49-D810564C0130"
		},
		{
			"etask.entity": "sc017499",
			"id": "6CCE60AA-26C2-215E-CBA4-F174EEB8F9D8"
		},
		{
			"etask.entity": "sc017500",
			"id": "B8A2BCF6-E46E-9534-7F31-FB22E322E794"
		},
		{
			"etask.entity": "sc017502",
			"id": "7C708BEF-130F-BD75-DDEB-111EB81FE8FD"
		},
		{
			"etask.entity": "sc017503",
			"id": "67A97023-B8F9-97F5-6368-C4C29CACDAEF"
		},
		{
			"etask.entity": "sc017504",
			"id": "F5334818-7C2C-FFA2-0F24-79F2DC27A0CB"
		},
		{
			"etask.entity": "sc017505",
			"id": "F552E27F-4A2D-2AEB-6FEC-25C4DBFE54E1"
		},
		{
			"etask.entity": "sc017507",
			"id": "7FAEA8BC-DF71-5E6E-C2BD-7670F97AC126"
		},
		{
			"etask.entity": "sc017508",
			"id": "082B51A1-8153-A697-C5A2-A6C3FCBEBD7D"
		},
		{
			"etask.entity": "sc017509",
			"id": "BF64DA5F-0A09-DA8A-FF14-8F0FFE282C0C"
		},
		{
			"etask.entity": "sc017510",
			"id": "8D7EE0A0-E0BC-EE3D-B120-FF3D9D5A4A4D"
		},
		{
			"etask.entity": "sc017512",
			"id": "39BFEDC1-3232-681B-D737-810D825430CC"
		},
		{
			"etask.entity": "sc017513",
			"id": "EC7DF10B-03C2-9D17-61B0-F8FC2705AD3F"
		},
		{
			"etask.entity": "sc017514",
			"id": "04F83596-C1EE-97C0-E5A5-FA1209FCEE71"
		},
		{
			"etask.entity": "sc017515",
			"id": "BE226AA5-3A21-2005-AF97-BCD1DCBFB071"
		},
		{
			"etask.entity": "sc017517",
			"id": "827546BB-C463-A7DE-3885-274483DB53C1"
		},
		{
			"etask.entity": "sc023634",
			"id": "AC3F43EA-F94E-19EB-DA19-70714E3B948F"
		},
		{
			"etask.entity": "sc017519",
			"id": "31A3E26D-564E-E448-3B50-52E495312C37"
		},
		{
			"etask.entity": "sc017520",
			"id": "B4A192E5-44C5-E364-38A7-39F7665B8E9A"
		},
		{
			"etask.entity": "sc017521",
			"id": "A321E192-DCC2-5FF5-C061-9358C5872E05"
		},
		{
			"etask.entity": "sc017522",
			"id": "BDC0C6C2-652C-1F11-D2AB-ADD785AB78D8"
		},
		{
			"etask.entity": "sc017524",
			"id": "382D425C-A18C-0657-2E79-72FB492C5005"
		},
		{
			"etask.entity": "sc017525",
			"id": "21F0A78E-EE06-7453-CA12-6AA0CD1CC006"
		},
		{
			"etask.entity": "sc017526",
			"id": "14072226-A391-C3BA-A49E-692D43642DAA"
		},
		{
			"etask.entity": "sc017527",
			"id": "7A3F54F1-B5BF-5860-6D8E-3F0D3CFE7983"
		},
		{
			"etask.entity": "sc017529",
			"id": "F15C3589-A3D4-B16A-70A1-28DD5991F346"
		},
		{
			"etask.entity": "sc017530",
			"id": "2989256D-5338-FBBE-44C1-A5F5176ACF21"
		},
		{
			"etask.entity": "sc017531",
			"id": "C778765B-F87C-C3EB-0768-D309A11FA270"
		},
		{
			"etask.entity": "sc017532",
			"id": "5131AC04-C256-5E8E-0DD6-B050A497DEC5"
		},
		{
			"etask.entity": "sc017534",
			"id": "C2F9DBE7-FCFB-BA7B-82AA-B8974050A951"
		},
		{
			"etask.entity": "sc017535",
			"id": "B80FBDA8-8C1B-11FA-C102-5F61CB87CD20"
		},
		{
			"etask.entity": "sc017536",
			"id": "00B6B4D5-B0FE-A53D-0206-0ED71FEA097E"
		},
		{
			"etask.entity": "sc017537",
			"id": "35A7AE16-8570-93DA-C980-63DA88557CC4"
		},
		{
			"etask.entity": "sc017539",
			"id": "C1D15035-128E-D04B-CCFA-8D8A7E449340"
		},
		{
			"etask.entity": "sc014386",
			"id": "FF669108-CD14-4006-633B-CD2DCE82CBD2"
		},
		{
			"etask.entity": "sc014391",
			"id": "B42C5B94-8D67-4A17-ACD4-E71675C8F33F"
		},
		{
			"etask.entity": "sc014396",
			"id": "F2BA04D8-C508-27B5-F29E-FFF4FA8B0E18"
		},
		{
			"etask.entity": "sc014398",
			"id": "8F1CB06A-992B-82E6-90CD-CBB810982B2C"
		},
		{
			"etask.entity": "sc014403",
			"id": "7E4A5B25-6FC8-F144-A4AF-3DB01BF6E589"
		},
		{
			"etask.entity": "sc014408",
			"id": "8E876561-9DAD-DE1F-9C53-0AEDEB4B1D38"
		},
		{
			"etask.entity": "sc014413",
			"id": "9F3A9125-2CE6-BAC8-3B84-658071ECABAB"
		},
		{
			"etask.entity": "sc014418",
			"id": "4338A353-96AB-FED9-C180-FF46345B27D9"
		},
		{
			"etask.entity": "sc014420",
			"id": "CD4686FD-510A-A7EA-96C5-8C136E149617"
		},
		{
			"etask.entity": "sc014425",
			"id": "EE3D4D0F-7C40-C935-0D07-D4C628C0577F"
		},
		{
			"etask.entity": "sc014430",
			"id": "24433C92-DA39-21F5-3F2D-8FB0A3303E2B"
		},
		{
			"etask.entity": "sc014435",
			"id": "FEFFC544-08AE-8B46-2FFC-AA550D4E2051"
		},
		{
			"etask.entity": "sc014440",
			"id": "C50E5F6F-50B8-BACF-53C6-669B5C8FCFAA"
		},
		{
			"etask.entity": "sc014442",
			"id": "CA7B4B41-0F28-92D9-36A5-FC74F568D7FE"
		},
		{
			"etask.entity": "sc014447",
			"id": "D0CA56D5-86A5-B19D-FE50-33C2C6AF8F6A"
		},
		{
			"etask.entity": "sc014452",
			"id": "C50DEE7E-82A8-3B4B-0898-1A5E4BD65AE8"
		},
		{
			"etask.entity": "sc014457",
			"id": "F9131561-CD78-B5C9-EEAE-7AE2A5C14D03"
		},
		{
			"etask.entity": "sc014462",
			"id": "62B61535-D794-328C-BDE6-959524B4409B"
		},
		{
			"etask.entity": "sc023635",
			"id": "3A4E9D24-C241-B4C8-9BBB-F4C36E26BD34"
		},
		{
			"etask.entity": "sc017541",
			"id": "CB7337FC-F345-0564-8C02-A92987B498E3"
		},
		{
			"etask.entity": "sc017542",
			"id": "A6BB06A2-DB7F-9478-98F1-165B62F3E3FC"
		},
		{
			"etask.entity": "sc017543",
			"id": "F80351EB-1618-4557-6EF9-4CEB5190F8D1"
		},
		{
			"etask.entity": "sc017544",
			"id": "110639E1-96CA-DBF9-AC33-2BA5E5ED0A1F"
		},
		{
			"etask.entity": "sc017546",
			"id": "3FDA0B4A-897C-ABB6-A691-092342F6780E"
		},
		{
			"etask.entity": "sc017547",
			"id": "17124355-CE66-E035-13F6-9CEA4278BFD4"
		},
		{
			"etask.entity": "sc017548",
			"id": "B1740EEA-BFAB-DF5E-4836-F69170055607"
		},
		{
			"etask.entity": "sc017549",
			"id": "2EC17E4D-7436-963B-35C4-34FC66687211"
		},
		{
			"etask.entity": "sc017551",
			"id": "13874EAF-EC3E-6361-5097-B94CE0DBBE33"
		},
		{
			"etask.entity": "sc017552",
			"id": "9632A89B-5367-AC62-5BE9-B3F490D49924"
		},
		{
			"etask.entity": "sc017553",
			"id": "7FDDE849-33F6-0F4A-FFD5-FCB681D4CEE1"
		},
		{
			"etask.entity": "sc017554",
			"id": "07574A75-5CFF-CCE2-EC01-CD9AB77A992F"
		},
		{
			"etask.entity": "sc017556",
			"id": "3276D1C9-8026-8EA9-72CC-7C07DB1E1401"
		},
		{
			"etask.entity": "sc017557",
			"id": "6AA486AB-3455-9B59-4E19-DF087A10AFC0"
		},
		{
			"etask.entity": "sc017558",
			"id": "0D4487B2-6C53-8CC8-2161-8BEDC11A743D"
		},
		{
			"etask.entity": "sc017559",
			"id": "A19C9C8B-3D38-49CC-31D4-F979277DEB39"
		},
		{
			"etask.entity": "sc017561",
			"id": "E03A3C91-A124-8FA4-815A-7E8E8696B8C1"
		},
		{
			"etask.entity": "sc023636",
			"id": "BBD739D7-8A1E-1665-D941-3D7011681AF8"
		},
		{
			"etask.entity": "sc017563",
			"id": "67F590DB-03BD-9137-A45D-8F9A10FAEDB6"
		},
		{
			"etask.entity": "sc017564",
			"id": "CF02D224-0724-DE63-AA5A-2FF5A53085CB"
		},
		{
			"etask.entity": "sc017565",
			"id": "868C90E7-B5C7-C221-06B1-E1E0E2868729"
		},
		{
			"etask.entity": "sc017566",
			"id": "50C9E8E6-57BA-CD46-B45A-C7EFC47BFE85"
		},
		{
			"etask.entity": "sc017568",
			"id": "6312A335-1025-C49F-4B2E-1DCF74229B22"
		},
		{
			"etask.entity": "sc017569",
			"id": "39C2CD96-C285-A377-8F70-6E07A54A1E90"
		},
		{
			"etask.entity": "sc017570",
			"id": "2CC9B703-6ADA-3CF8-D8DC-B279EEC77DD0"
		},
		{
			"etask.entity": "sc017571",
			"id": "63623B28-951C-DC94-5AC0-0D5DEF15768C"
		},
		{
			"etask.entity": "sc017573",
			"id": "B4C42FB1-1412-FB1C-A584-607DD40B4EF0"
		},
		{
			"etask.entity": "sc017574",
			"id": "7A728D2F-7B35-754B-75DB-89943746D2B6"
		},
		{
			"etask.entity": "sc017575",
			"id": "9083A490-CDBC-169B-0581-05A6E16B02DE"
		},
		{
			"etask.entity": "sc017576",
			"id": "8096760D-E3F4-6DB4-B096-5EFF5B63E69F"
		},
		{
			"etask.entity": "sc017578",
			"id": "B2A0EA1D-6DAD-1F00-B557-06D39FECC729"
		},
		{
			"etask.entity": "sc017579",
			"id": "D37D1899-3B23-AB01-394C-742FE5F5D1BF"
		},
		{
			"etask.entity": "sc017580",
			"id": "64AEF446-CBDA-A147-48D9-626372240147"
		},
		{
			"etask.entity": "sc017581",
			"id": "D6552F6E-8212-690B-0821-F3D7A01110CE"
		},
		{
			"etask.entity": "sc017583",
			"id": "22DF46D3-A5AA-021A-046F-F12AD07560A4"
		},
		{
			"etask.entity": "sc023637",
			"id": "2F772BBA-2C86-A5B4-AEFE-3812BAF61876"
		},
		{
			"etask.entity": "sc017585",
			"id": "F6979C4E-2D61-C38A-B4A8-6ED60BC41EA4"
		},
		{
			"etask.entity": "sc017586",
			"id": "B81E8656-217E-235F-73D3-784B6F4418AB"
		},
		{
			"etask.entity": "sc017587",
			"id": "7E7951FB-BE48-9E69-407E-5D109D132579"
		},
		{
			"etask.entity": "sc017588",
			"id": "110601DB-5F7D-33F5-B753-4FCCF818ACC8"
		},
		{
			"etask.entity": "sc017590",
			"id": "D8AEAC2F-A6B2-7E81-0F98-AC5D9311CB75"
		},
		{
			"etask.entity": "sc017591",
			"id": "72ADCD20-FA34-28C8-C70F-E9863D8BCE70"
		},
		{
			"etask.entity": "sc017592",
			"id": "AFD25367-1094-375E-6EA4-5D2BD44C80E0"
		},
		{
			"etask.entity": "sc017593",
			"id": "25D08075-2839-CB3C-F831-31F2A2C99942"
		},
		{
			"etask.entity": "sc017595",
			"id": "E6D6C3D8-AFBA-8963-8387-E3A621B27FC4"
		},
		{
			"etask.entity": "sc017596",
			"id": "13ADC464-C4D8-8FCB-8332-0FC9E367A197"
		},
		{
			"etask.entity": "sc017597",
			"id": "B6DD3E3C-B378-FA0E-61F7-52C791400093"
		},
		{
			"etask.entity": "sc017598",
			"id": "EFEE7AD1-851B-5A35-CC65-3FCD549980BA"
		},
		{
			"etask.entity": "sc017600",
			"id": "A4DAB912-CD8E-6258-C2C2-1459606B9818"
		},
		{
			"etask.entity": "sc017601",
			"id": "C6E25DCC-0E44-03D0-2355-2ADFE82DD881"
		},
		{
			"etask.entity": "sc017602",
			"id": "C9593ABD-668A-B755-EE2E-8C8315CF0657"
		},
		{
			"etask.entity": "sc017603",
			"id": "6917E330-18F4-253F-F028-6309BAB5F794"
		},
		{
			"etask.entity": "sc017605",
			"id": "2EC56D8D-EF0A-832C-3734-C47FEAD8B4E2"
		},
		{
			"etask.entity": "sc023638",
			"id": "75352AD8-75ED-8AC8-27EA-4AAE253F4FF2"
		},
		{
			"etask.entity": "sc017607",
			"id": "C82D29BA-9CE8-77DA-54CF-CC9C5098F328"
		},
		{
			"etask.entity": "sc017608",
			"id": "E95DA8BA-54E2-9CEE-B953-F9AAEE637528"
		},
		{
			"etask.entity": "sc017609",
			"id": "90A06AC4-E722-0A97-552A-C206584D67B2"
		},
		{
			"etask.entity": "sc017610",
			"id": "635C53D8-42FB-1046-E16D-2321D719FE7A"
		},
		{
			"etask.entity": "sc017612",
			"id": "1C5BBF75-E793-7E38-4F7A-E82E152F4230"
		},
		{
			"etask.entity": "sc017613",
			"id": "16DD6F18-DDD9-DD3E-3B35-332609F5147C"
		},
		{
			"etask.entity": "sc017614",
			"id": "1F90B95B-FE59-D943-435A-52E05EC0A5D9"
		},
		{
			"etask.entity": "sc017615",
			"id": "FCFA5957-33FF-FE4E-2F98-90A3C12313F3"
		},
		{
			"etask.entity": "sc017617",
			"id": "1A6AD6B5-1CBD-54D7-4D79-6461F68DFCE5"
		},
		{
			"etask.entity": "sc017618",
			"id": "6C228B90-EF1C-E82E-CD86-E6DC8509C04F"
		},
		{
			"etask.entity": "sc017619",
			"id": "BF844213-F093-494D-A8A7-B248274FC982"
		},
		{
			"etask.entity": "sc017620",
			"id": "DC53141F-DEC1-AEFD-43A8-0345D5C88021"
		},
		{
			"etask.entity": "sc017622",
			"id": "9A06989A-4E6D-4055-5109-EFB9A6BB4EE1"
		},
		{
			"etask.entity": "sc017623",
			"id": "1247967E-A27E-29FE-A64E-E5F2F59F8564"
		},
		{
			"etask.entity": "sc017624",
			"id": "37A809D3-5916-9247-B34C-A23D0DA217AA"
		},
		{
			"etask.entity": "sc017625",
			"id": "1F1724CC-F97E-5793-D306-9B858DC8B721"
		},
		{
			"etask.entity": "sc017627",
			"id": "B18DA4C5-CDBC-14E9-333E-8633D98D0CF7"
		},
		{
			"etask.entity": "sc014464",
			"id": "44F6FE55-093A-5F65-584B-3DD397F8B503"
		},
		{
			"etask.entity": "sc014469",
			"id": "D7D7E8A7-53F5-7BD6-6643-6C25647C071A"
		},
		{
			"etask.entity": "sc014474",
			"id": "5BC003A9-10F4-B3A2-8347-A9DB4C257CC2"
		},
		{
			"etask.entity": "sc014479",
			"id": "C2C82BB3-6B25-7544-FC44-479254974641"
		},
		{
			"etask.entity": "sc014484",
			"id": "645B65FF-FF31-52E0-13F9-E054C20F9069"
		},
		{
			"etask.entity": "sc014486",
			"id": "75CB9B80-C503-9D4F-F5D0-8505824A0FF3"
		},
		{
			"etask.entity": "sc014491",
			"id": "70D68A29-6D6C-A322-850E-8FDCFB09C312"
		},
		{
			"etask.entity": "sc014496",
			"id": "73C682AE-68E7-2009-F9B1-8AB030005CA1"
		},
		{
			"etask.entity": "sc014501",
			"id": "371311F5-2E61-C072-A687-9F6296D32BBB"
		},
		{
			"etask.entity": "sc014506",
			"id": "9CF78D23-6DE0-FEFD-1CC2-7EC856A589CD"
		},
		{
			"etask.entity": "sc014508",
			"id": "8FCC3BD7-5892-88AE-DA0A-3A3FB44DB8F5"
		},
		{
			"etask.entity": "sc014513",
			"id": "BB7435A4-666C-3215-FFF0-E8AC63C88873"
		},
		{
			"etask.entity": "sc014518",
			"id": "68938C69-C1AE-DAF6-4986-78EF9A9C8A70"
		},
		{
			"etask.entity": "sc014523",
			"id": "7705804B-1E9A-311C-AE54-F1D0EFD22E5A"
		},
		{
			"etask.entity": "sc014528",
			"id": "C787C38B-60A9-2A78-8939-BD98484A591D"
		},
		{
			"etask.entity": "sc014530",
			"id": "CF9FCC81-AD11-2B0F-FBEC-26FADDDF1B12"
		},
		{
			"etask.entity": "sc014535",
			"id": "D13A6C7E-C662-1CB8-4E49-E34851625F0D"
		},
		{
			"etask.entity": "sc014540",
			"id": "44B38D46-D6E0-19C9-EB51-6A44C3209394"
		},
		{
			"etask.entity": "sc023639",
			"id": "10DB29F4-D6DD-5353-1E4C-579E0F59E1F0"
		},
		{
			"etask.entity": "sc017629",
			"id": "F8BC6D50-560E-A787-7412-67049CAD38B1"
		},
		{
			"etask.entity": "sc017630",
			"id": "F17505F2-7EDE-0F10-AD3B-07616282B30B"
		},
		{
			"etask.entity": "sc017631",
			"id": "45B2602E-E9BB-7A87-7B71-88D7ABA89238"
		},
		{
			"etask.entity": "sc017632",
			"id": "60CDC38D-A36C-97C4-4CF3-DBDFFCAA4FC2"
		},
		{
			"etask.entity": "sc017634",
			"id": "89E195D9-E366-931D-574B-F22CC932B434"
		},
		{
			"etask.entity": "sc017635",
			"id": "1B48CE83-A98E-FFB8-6817-A8078EC9BEC6"
		},
		{
			"etask.entity": "sc017636",
			"id": "F9279E56-B125-6279-4001-EF95ABCCC450"
		},
		{
			"etask.entity": "sc017637",
			"id": "8AEC3A82-73B7-7BDF-AE01-89EF982D9DFB"
		},
		{
			"etask.entity": "sc017639",
			"id": "F6F66C44-37AC-2BF8-09AF-FA6B5E85EE58"
		},
		{
			"etask.entity": "sc017640",
			"id": "81AD7782-1E34-1853-829D-1F7EDD47D0B3"
		},
		{
			"etask.entity": "sc017641",
			"id": "890EC6C8-DCFB-E0B9-5B30-410EA9851096"
		},
		{
			"etask.entity": "sc017642",
			"id": "DFF7BE77-391F-76CF-6FDD-6D1F7DBD316D"
		},
		{
			"etask.entity": "sc017644",
			"id": "55A612A6-5F9B-37E3-D91C-C1535E915862"
		},
		{
			"etask.entity": "sc017645",
			"id": "ED511521-708E-7111-AB5E-2CA52400269E"
		},
		{
			"etask.entity": "sc017646",
			"id": "6606BC2E-7C06-D236-A8A0-73D42D347D2D"
		},
		{
			"etask.entity": "sc017647",
			"id": "F454641A-B9F1-5C5F-B13C-8A5707E066C0"
		},
		{
			"etask.entity": "sc017649",
			"id": "894C21C7-9116-FC74-93F3-16C0F7C474E9"
		},
		{
			"etask.entity": "sc023640",
			"id": "30D55284-9405-F6C4-75FF-D363A05A85C6"
		},
		{
			"etask.entity": "sc017651",
			"id": "99561905-EF75-B7EF-F975-587133D71183"
		},
		{
			"etask.entity": "sc017652",
			"id": "30C5E9AB-1F86-2ECC-3C06-E7C61A4E3427"
		},
		{
			"etask.entity": "sc017653",
			"id": "2863BE25-380B-9A08-C537-C2DAF3ED3C4C"
		},
		{
			"etask.entity": "sc017654",
			"id": "522E8179-0B79-A621-DCE9-A5F76C55C977"
		},
		{
			"etask.entity": "sc017656",
			"id": "184CC15E-1421-F5EE-872E-6B89FCDB45CB"
		},
		{
			"etask.entity": "sc017657",
			"id": "AEBD579F-6221-AB15-7EFB-3602013732CE"
		},
		{
			"etask.entity": "sc017658",
			"id": "6B67305D-6E54-5672-1873-D6F4E9B8E7E8"
		},
		{
			"etask.entity": "sc017659",
			"id": "8D1333FB-89E6-93A3-B55D-D803E83E1CE3"
		},
		{
			"etask.entity": "sc017661",
			"id": "ECF02AF6-60CF-D4BA-565B-6C6E16022352"
		},
		{
			"etask.entity": "sc017662",
			"id": "F55B7E7E-11EF-8DFE-5927-C870EA6299E3"
		},
		{
			"etask.entity": "sc017663",
			"id": "70464FD3-6038-2B70-A066-43258C292334"
		},
		{
			"etask.entity": "sc017664",
			"id": "A14A0147-A5FF-4E16-8C54-51DE572ACA61"
		},
		{
			"etask.entity": "sc017666",
			"id": "A4C73B52-6F11-2251-527F-A3F6FD65DC68"
		},
		{
			"etask.entity": "sc017667",
			"id": "C14B315E-D51F-E4B9-A169-6356B8715920"
		},
		{
			"etask.entity": "sc017668",
			"id": "3CF90D5D-131F-1B29-7FC6-B38DA27DB3BB"
		},
		{
			"etask.entity": "sc017669",
			"id": "FE4B5074-F0E8-707A-1969-7CB7FB598097"
		},
		{
			"etask.entity": "sc017671",
			"id": "46643BC2-2DA5-C647-6A94-7C1103AF45DF"
		},
		{
			"etask.entity": "sc023641",
			"id": "CFB6638B-35D8-E7B6-7F82-96C0B96E5DFE"
		},
		{
			"etask.entity": "sc017673",
			"id": "FAB530A7-2E2B-06AA-CA35-CAB35757E530"
		},
		{
			"etask.entity": "sc017674",
			"id": "25382A48-2C97-78C4-FC8F-EE96759F6E5C"
		},
		{
			"etask.entity": "sc017675",
			"id": "FDD4053C-3409-FF7F-134F-C4A58F492230"
		},
		{
			"etask.entity": "sc017676",
			"id": "098CAEB1-57F8-1BE0-C127-A32DE57DEF79"
		},
		{
			"etask.entity": "sc017678",
			"id": "1D3DCC54-F61F-6AF4-E6F0-84F71A1AC577"
		},
		{
			"etask.entity": "sc017679",
			"id": "2D11B33D-F72C-6F9B-AB75-1FF7CB75B9A3"
		},
		{
			"etask.entity": "sc017680",
			"id": "55D440FD-32A1-14BE-22AE-3C40EE6EFE38"
		},
		{
			"etask.entity": "sc017681",
			"id": "9ABA0DE0-57C9-53A3-CA9B-700D17CFD468"
		},
		{
			"etask.entity": "sc017683",
			"id": "A265A184-2CDF-6898-039C-DC0E130736A0"
		},
		{
			"etask.entity": "sc017684",
			"id": "940C4441-5A72-F94E-C3C2-87FC121783C6"
		},
		{
			"etask.entity": "sc017685",
			"id": "D132A975-68B2-C09B-2650-A17F94DB841F"
		},
		{
			"etask.entity": "sc017686",
			"id": "E69CD79F-5A9B-1765-F3B7-C50E414B94BC"
		},
		{
			"etask.entity": "sc017688",
			"id": "3F910FDC-5242-E949-4C0C-3AB3BF485648"
		},
		{
			"etask.entity": "sc017689",
			"id": "3B8DC320-05A9-6181-6D39-5EB1667AC431"
		},
		{
			"etask.entity": "sc017690",
			"id": "83C004B4-6D4D-5862-A9B8-ACC9A02C0C0D"
		},
		{
			"etask.entity": "sc017691",
			"id": "9BEC0775-E0F1-566E-A3D6-966430F3E121"
		},
		{
			"etask.entity": "sc017693",
			"id": "152231BA-737A-0856-EB95-B66E030C704A"
		},
		{
			"etask.entity": "sc014545",
			"id": "C3A60956-6D23-5B20-786E-68683E4B2E3A"
		},
		{
			"etask.entity": "sc014550",
			"id": "AD820CFB-F235-D157-105C-B1ECCCAA5889"
		},
		{
			"etask.entity": "sc014552",
			"id": "984E10CF-A3C7-6F4D-B9DE-AD29D595AC01"
		},
		{
			"etask.entity": "sc014557",
			"id": "A4785F2D-8E7E-EBE3-4E21-FC8A1D435F28"
		},
		{
			"etask.entity": "sc014562",
			"id": "91F51C7C-17D6-9CA3-D094-46851D244D05"
		},
		{
			"etask.entity": "sc014567",
			"id": "8626B6BA-652C-C2C3-AF44-A374AFFBA0EA"
		},
		{
			"etask.entity": "sc014572",
			"id": "36B42A63-79E1-DB1F-2259-F63522787A0F"
		},
		{
			"etask.entity": "sc014574",
			"id": "FAA5C496-BF0A-C1EB-8EF6-1E22F71AF988"
		},
		{
			"etask.entity": "sc014579",
			"id": "9F73C7E2-A705-6F18-6414-111F27D9B599"
		},
		{
			"etask.entity": "sc014584",
			"id": "CB9B5E66-1D06-112A-BD60-BC16A7440042"
		},
		{
			"etask.entity": "sc014589",
			"id": "E0628B91-717B-5B0E-6BA6-1B2C5BB13AF9"
		},
		{
			"etask.entity": "sc014594",
			"id": "CF4E4649-F419-5BCE-4DB4-CD608BE7F283"
		},
		{
			"etask.entity": "sc014596",
			"id": "74EF667D-B0D0-E3A7-62B3-4E1324622136"
		},
		{
			"etask.entity": "sc014601",
			"id": "A36A2A9C-C6EB-DDBA-DAD8-35A5C10C0D4A"
		},
		{
			"etask.entity": "sc014606",
			"id": "C97C2887-409C-CD5B-E57A-C88856C0AE40"
		},
		{
			"etask.entity": "sc014611",
			"id": "FFC95B25-0033-D828-E85B-6E8DDCE90336"
		},
		{
			"etask.entity": "sc014616",
			"id": "D3433130-49B2-D89C-2977-5A9483E5F981"
		},
		{
			"etask.entity": "sc014618",
			"id": "C8B4E649-BECF-AD9B-5BE7-D95FF6E7B784"
		},
		{
			"etask.entity": "sc023642",
			"id": "70F042D9-FCA7-A3DE-012D-5E6F5E505173"
		},
		{
			"etask.entity": "sc017695",
			"id": "B7E32BE4-2EDE-7ADA-1050-58DA5D88FF9D"
		},
		{
			"etask.entity": "sc017696",
			"id": "06A20294-8397-FEBA-759E-B6B1DFAF929A"
		},
		{
			"etask.entity": "sc017697",
			"id": "096AC613-BB2D-9278-349A-6F9A5D3C2A52"
		},
		{
			"etask.entity": "sc017698",
			"id": "1EF181FF-3888-8047-BE82-AF3B4E370AA6"
		},
		{
			"etask.entity": "sc017700",
			"id": "FDE376D7-E49B-7D78-4807-2B75D25C0A25"
		},
		{
			"etask.entity": "sc017701",
			"id": "C7C04F2E-FE87-2576-A15F-461F1E6AB1AB"
		},
		{
			"etask.entity": "sc017702",
			"id": "AFCC19A7-A089-7EDA-616C-52200395100A"
		},
		{
			"etask.entity": "sc017703",
			"id": "15ED91C7-8F3D-9DBA-6B3C-9AF41F72981F"
		},
		{
			"etask.entity": "sc017705",
			"id": "DCCB9C40-B217-6A42-B4BC-EC7B196943EB"
		},
		{
			"etask.entity": "sc017706",
			"id": "574F74BD-7521-5DF0-5F17-BADB0955EC1B"
		},
		{
			"etask.entity": "sc017707",
			"id": "486C4049-40A2-3354-F422-3E1B866ADD5C"
		},
		{
			"etask.entity": "sc017708",
			"id": "50F06EC6-BC90-DF69-3068-89D4C3C58E09"
		},
		{
			"etask.entity": "sc017710",
			"id": "8C5011E9-35AE-2963-00DD-27A916552375"
		},
		{
			"etask.entity": "sc017711",
			"id": "02740842-BEE7-78F3-A950-BB8DB7465DB8"
		},
		{
			"etask.entity": "sc017712",
			"id": "780A241A-4F3E-CC2E-FEE2-4F549C5E152A"
		},
		{
			"etask.entity": "sc017713",
			"id": "1499F822-4E61-F589-4FD5-744AF731DF9B"
		},
		{
			"etask.entity": "sc017715",
			"id": "E8A44C53-F36F-F6B8-88C8-4FD0250A448F"
		},
		{
			"etask.entity": "sc023643",
			"id": "16FF0F50-877F-B6B2-11D6-4131ADB8DD7B"
		},
		{
			"etask.entity": "sc017717",
			"id": "9C9BF0D1-3089-98A8-4FF2-8550ED0379B8"
		},
		{
			"etask.entity": "sc017718",
			"id": "B5545030-C8B6-EA47-D2E5-B2E4C2534306"
		},
		{
			"etask.entity": "sc017719",
			"id": "AD9D5F1A-393C-E063-F4D3-57FFAFD35BBF"
		},
		{
			"etask.entity": "sc017720",
			"id": "0DDB3850-2D65-C989-F5BF-70E54F19D63A"
		},
		{
			"etask.entity": "sc017722",
			"id": "110BD8B7-F4B3-64A0-FFEF-B69E98E73FBE"
		},
		{
			"etask.entity": "sc017723",
			"id": "EABD81F8-44F7-6C29-C694-2F032EB041BC"
		},
		{
			"etask.entity": "sc017724",
			"id": "68CB38A2-831C-3AF5-417D-044443B41766"
		},
		{
			"etask.entity": "sc017725",
			"id": "5C324ECA-9A67-A115-E7E9-E68168C76659"
		},
		{
			"etask.entity": "sc017727",
			"id": "710587C6-00F6-7DFF-60C1-26ABD35F540E"
		},
		{
			"etask.entity": "sc017728",
			"id": "2FDCA7E1-6F7F-C70B-C213-0250F2FA6358"
		},
		{
			"etask.entity": "sc017729",
			"id": "EB79DBBE-FD20-51A3-AAA7-C5D544100798"
		},
		{
			"etask.entity": "sc017730",
			"id": "76CF0790-48E2-5907-B721-9CFE4508D075"
		},
		{
			"etask.entity": "sc017732",
			"id": "365B7146-FE41-BF9E-2136-E4C32EFD16C1"
		},
		{
			"etask.entity": "sc017733",
			"id": "DC47AA71-2847-F3F6-6F39-C0F2D2ECC3B6"
		},
		{
			"etask.entity": "sc017734",
			"id": "A87D8F6F-4173-F3FC-431B-70D9114A36C9"
		},
		{
			"etask.entity": "sc017735",
			"id": "BCD3AB7A-EE08-AAEC-1FF1-7853E631660A"
		},
		{
			"etask.entity": "sc017737",
			"id": "4A89AE81-C69D-6211-2823-142EB55B29E9"
		},
		{
			"etask.entity": "sc023644",
			"id": "FD79446D-51A3-B603-779E-46E5683007B8"
		},
		{
			"etask.entity": "sc017739",
			"id": "BB15D0E1-5649-24B0-6429-93E62EB0624B"
		},
		{
			"etask.entity": "sc017740",
			"id": "33BFC416-18D2-67AE-8B59-082664363555"
		},
		{
			"etask.entity": "sc017741",
			"id": "16329285-F0EC-730C-C132-6694E065E177"
		},
		{
			"etask.entity": "sc017742",
			"id": "94745FCC-9937-FB51-889E-B11936532FC7"
		},
		{
			"etask.entity": "sc017744",
			"id": "808DB3FE-5A9F-F113-9D57-5AC6A46A35B4"
		},
		{
			"etask.entity": "sc017745",
			"id": "85D21BA6-67DD-E7C3-938E-49F447C6E37E"
		},
		{
			"etask.entity": "sc017746",
			"id": "B29ED897-3DA3-F52B-6579-8A45DD454FAA"
		},
		{
			"etask.entity": "sc017747",
			"id": "1CF6985D-3C22-CD65-D883-215DCACBEE4F"
		},
		{
			"etask.entity": "sc017749",
			"id": "146187F4-C709-642B-05CC-E0A0500AF973"
		},
		{
			"etask.entity": "sc017750",
			"id": "54C62A10-34B6-488F-C3FB-81E5766433E1"
		},
		{
			"etask.entity": "sc017751",
			"id": "A1B02E72-3E86-6FDA-CCE8-8F27BB3D9442"
		},
		{
			"etask.entity": "sc017752",
			"id": "412BF0BC-B20B-90D4-B080-E555808AE262"
		},
		{
			"etask.entity": "sc017754",
			"id": "9FD2AE50-6D93-D12B-6F8F-D753F1B0587A"
		},
		{
			"etask.entity": "sc017755",
			"id": "0A73AFA5-F21C-A91C-35DC-1CF2796A8221"
		},
		{
			"etask.entity": "sc017756",
			"id": "AA357CD0-55E1-C0B0-61DC-D1ECDE8B6E0C"
		},
		{
			"etask.entity": "sc017757",
			"id": "132691BF-B81B-EA67-CA81-A21B113F9598"
		},
		{
			"etask.entity": "sc017759",
			"id": "80FEF865-1EA5-09B1-6FA6-AA99A69F45BC"
		},
		{
			"etask.entity": "sc023645",
			"id": "15745DDC-BD14-115E-71EA-BE201CD2E539"
		},
		{
			"etask.entity": "sc017761",
			"id": "4EF5F5FB-5BC3-7E7C-74DF-6EDCAEEFAD97"
		},
		{
			"etask.entity": "sc017762",
			"id": "180A8B8B-1AFC-002B-8B1B-EB6DC6609E9B"
		},
		{
			"etask.entity": "sc017763",
			"id": "A4D88216-0511-B625-C0F7-953952120D07"
		},
		{
			"etask.entity": "sc017764",
			"id": "A5EE5BBC-BDD3-A504-6139-2707B498677D"
		},
		{
			"etask.entity": "sc017766",
			"id": "E2E0E149-E4E9-8032-41BD-935D702F5E1F"
		},
		{
			"etask.entity": "sc017767",
			"id": "0CB4015E-9073-50CE-FE2F-8FBBDBD441BB"
		},
		{
			"etask.entity": "sc017768",
			"id": "36192162-CD22-D4C2-F930-48C96FD3C26E"
		},
		{
			"etask.entity": "sc017769",
			"id": "A1525687-3A07-0838-9FFA-AB7F1076C9C2"
		},
		{
			"etask.entity": "sc017771",
			"id": "C0E81603-862C-4E32-5143-94519F80D369"
		},
		{
			"etask.entity": "sc017772",
			"id": "CDC260C8-7156-A568-E100-E4294090CB7B"
		},
		{
			"etask.entity": "sc017773",
			"id": "2C813661-D618-BC6E-828A-8B11892417AE"
		},
		{
			"etask.entity": "sc017774",
			"id": "80278686-FE0D-E3E5-6977-72244444BCA8"
		},
		{
			"etask.entity": "sc017776",
			"id": "FE31AB22-E53E-51EA-49F1-5D95DC6B4192"
		},
		{
			"etask.entity": "sc017777",
			"id": "1198058A-64B9-8DA4-B605-EDF50E3B6006"
		},
		{
			"etask.entity": "sc017778",
			"id": "3E12FA05-8795-0B7D-96F9-34591EF191B6"
		},
		{
			"etask.entity": "sc017779",
			"id": "7DB49002-590B-1FAC-9F8F-67D61133D073"
		},
		{
			"etask.entity": "sc017781",
			"id": "525096A3-2330-D70E-C525-D808C9820B2F"
		},
		{
			"etask.entity": "sc014623",
			"id": "1BCC6870-BB9F-CC95-81BD-05D2A9472F8E"
		},
		{
			"etask.entity": "sc014628",
			"id": "CDDFCC98-06BF-D1B6-CA9E-0A0EB767D0DA"
		},
		{
			"etask.entity": "sc014633",
			"id": "B797CD9F-2754-EBE3-1F40-C2727F91A797"
		},
		{
			"etask.entity": "sc014638",
			"id": "4B7664DD-BA15-B011-C870-9FAE2EDC18E6"
		},
		{
			"etask.entity": "sc014640",
			"id": "4E99E62A-691F-8757-059B-B9554ECE117D"
		},
		{
			"etask.entity": "sc014645",
			"id": "004ACE78-A29B-BE88-1019-674C747C6A4D"
		},
		{
			"etask.entity": "sc014650",
			"id": "6C6C656F-D7AB-CE30-E9DA-8AC9E31472FA"
		},
		{
			"etask.entity": "sc014655",
			"id": "CBFF0F6D-19BE-1030-303B-179E222185A6"
		},
		{
			"etask.entity": "sc014660",
			"id": "0E7FBBA7-B687-FF1A-DE67-ECEAA7991120"
		},
		{
			"etask.entity": "sc014662",
			"id": "D7B90529-6925-9613-F1C5-1D324DEF31B1"
		},
		{
			"etask.entity": "sc014667",
			"id": "F4AC0AE8-1722-02B0-C4DA-C4D4552A4DFB"
		},
		{
			"etask.entity": "sc014672",
			"id": "7C098765-3433-F68F-408D-29FE49A84901"
		},
		{
			"etask.entity": "sc014677",
			"id": "A21BEA8C-3502-67E3-A420-89D684A32991"
		},
		{
			"etask.entity": "sc014682",
			"id": "49A9E54B-7405-E993-6ABB-D70591D08029"
		},
		{
			"etask.entity": "sc014684",
			"id": "97290CEF-FC30-1351-1596-5F95EE21C03D"
		},
		{
			"etask.entity": "sc014689",
			"id": "75C71096-FACE-C2F5-6413-3CC699DF58AC"
		},
		{
			"etask.entity": "sc014694",
			"id": "C825FA34-109A-CF09-22AE-52EE0B48D7AA"
		},
		{
			"etask.entity": "sc014699",
			"id": "A7EA2C9E-FCB9-3303-3AFE-14E07F463DE5"
		},
		{
			"etask.entity": "sc023646",
			"id": "E32B1A6C-1AA8-5048-B359-3B5696EB0F99"
		},
		{
			"etask.entity": "sc017783",
			"id": "DEC4A005-3CA8-87F5-7BC3-FECF29930D06"
		},
		{
			"etask.entity": "sc017784",
			"id": "5E785503-3699-56AB-CFC3-5DCCAFE32AAF"
		},
		{
			"etask.entity": "sc017785",
			"id": "9E583C39-C887-8ED6-938A-EF793AC6E0E9"
		},
		{
			"etask.entity": "sc017786",
			"id": "EC02256A-77AE-415A-CCA3-ED721F0312E0"
		},
		{
			"etask.entity": "sc017788",
			"id": "B25CF452-1CC2-A385-61E1-094BDEF8CAC2"
		},
		{
			"etask.entity": "sc017789",
			"id": "0F533347-F292-E567-82AB-B1A6D47C2C4C"
		},
		{
			"etask.entity": "sc017790",
			"id": "51A0DF79-D180-BDA5-BAFD-F75285457336"
		},
		{
			"etask.entity": "sc017791",
			"id": "D717BB2B-2499-A925-FEBF-856DC41E218D"
		},
		{
			"etask.entity": "sc017793",
			"id": "CE6FC79D-6912-A08B-CC78-5E2A7C67EA21"
		},
		{
			"etask.entity": "sc017794",
			"id": "C204B033-8FB7-4760-3526-3325BD2F4387"
		},
		{
			"etask.entity": "sc017795",
			"id": "48E15EBE-3F5E-8969-85E4-A2F112389401"
		},
		{
			"etask.entity": "sc017796",
			"id": "009D506D-95E5-FFA1-F752-11601622CCE4"
		},
		{
			"etask.entity": "sc017798",
			"id": "BA2BC134-BFF9-6541-70BC-2D0F07B44E2F"
		},
		{
			"etask.entity": "sc017799",
			"id": "E6729FD5-A2C9-AC25-D0AF-4C59C7B9009F"
		},
		{
			"etask.entity": "sc017800",
			"id": "DD03A9AE-7E4B-AD53-6DF6-23841659B017"
		},
		{
			"etask.entity": "sc017801",
			"id": "BEBC18E5-5614-EE2B-81D3-5CF0ED1EE87F"
		},
		{
			"etask.entity": "sc017803",
			"id": "60CEE344-D912-8AE8-3868-3DECE7C74CB6"
		},
		{
			"etask.entity": "sc023647",
			"id": "F1834104-BF27-DC7B-A037-BBBBFA17C518"
		},
		{
			"etask.entity": "sc023648",
			"id": "7D69B438-D4E6-F743-EA11-1596AB897572"
		},
		{
			"etask.entity": "sc023649",
			"id": "D073570C-BF55-E537-0CB0-A6595ADC4F5C"
		},
		{
			"etask.entity": "sc017805",
			"id": "30B2B896-26FC-2932-78C0-9BA6429AD565"
		},
		{
			"etask.entity": "sc017806",
			"id": "7FACD472-E140-87F9-E9EB-9465B26FA8A6"
		},
		{
			"etask.entity": "sc017807",
			"id": "AEF4DBF5-EAE3-6D12-C446-6CAFFA23BA69"
		},
		{
			"etask.entity": "sc017808",
			"id": "FD8CD865-065D-D0B2-4451-D6CCEF05A4AC"
		},
		{
			"etask.entity": "sc017810",
			"id": "EBA7C84E-AADA-459D-BF27-35288A9768C0"
		},
		{
			"etask.entity": "sc017811",
			"id": "C94B2962-634E-BE26-88F6-E47C6C4439D0"
		},
		{
			"etask.entity": "sc017812",
			"id": "4C895126-8DAD-2A25-E615-197A1DB7BC75"
		},
		{
			"etask.entity": "sc017813",
			"id": "920542C3-3D5E-7989-9E24-7BF3002F4ED1"
		},
		{
			"etask.entity": "sc017815",
			"id": "994C427A-C539-DD6F-29F3-63A4D83FF6D9"
		},
		{
			"etask.entity": "sc017816",
			"id": "68B31697-AB5C-823C-EAD0-32E48CEA53A5"
		},
		{
			"etask.entity": "sc017817",
			"id": "50DAE3FA-3DD9-139D-59DA-FE308349CA48"
		},
		{
			"etask.entity": "sc017818",
			"id": "D5E14D77-AEF5-F4EF-7209-DFBF2A2E9618"
		},
		{
			"etask.entity": "sc017820",
			"id": "CF918E2E-D30F-843C-0830-6344DF3F097E"
		},
		{
			"etask.entity": "sc017821",
			"id": "FF06AEC0-39AC-4EC8-74E1-49A4445676F5"
		},
		{
			"etask.entity": "sc017822",
			"id": "E7098AC0-9012-2553-E3FF-301E1C29F5FD"
		},
		{
			"etask.entity": "sc017823",
			"id": "B1A06F1A-CBC3-E5DA-63A9-150DBC85F20D"
		},
		{
			"etask.entity": "sc023650",
			"id": "9E8D9A9B-4CED-65E5-43E7-E41498A7C1DF"
		},
		{
			"etask.entity": "sc017827",
			"id": "3519E7EB-27C0-D050-4365-9BED66299EB4"
		},
		{
			"etask.entity": "sc017828",
			"id": "370864FB-CC09-DE8A-B47C-139BCEFB1FEA"
		},
		{
			"etask.entity": "sc017829",
			"id": "24ECC132-FE32-8F8D-090A-D20E2F82DCDB"
		},
		{
			"etask.entity": "sc017830",
			"id": "984E1DFE-D223-E3BE-5905-4880CB130F43"
		},
		{
			"etask.entity": "sc017832",
			"id": "04BC22DF-CFCE-4974-FE73-803A71675B67"
		},
		{
			"etask.entity": "sc017833",
			"id": "B1823332-278E-36A7-E485-5EF840887346"
		},
		{
			"etask.entity": "sc017834",
			"id": "633CADF4-D024-D3D7-11CC-572BA15B36BC"
		},
		{
			"etask.entity": "sc017835",
			"id": "8877D49A-D6E8-88E1-8D38-ABB9D9C2BEDD"
		},
		{
			"etask.entity": "sc017837",
			"id": "6D6152A2-B0FE-0840-4DDE-6C9A311D1021"
		},
		{
			"etask.entity": "sc017838",
			"id": "217B518D-A862-E81A-0ED6-B2103823B558"
		},
		{
			"etask.entity": "sc017839",
			"id": "6D762F9F-943E-4F14-9499-E1696AA8BB73"
		},
		{
			"etask.entity": "sc017840",
			"id": "CAE11980-AB45-7A39-4AA2-7F6D62153000"
		},
		{
			"etask.entity": "sc017842",
			"id": "845F17AE-8ED0-AE9D-79C2-B649D433E24B"
		},
		{
			"etask.entity": "sc017843",
			"id": "662BFEDB-8C53-2BE8-0879-E11C31732E1C"
		},
		{
			"etask.entity": "sc017844",
			"id": "D037231D-BA3B-935A-AD19-32805D302AEC"
		},
		{
			"etask.entity": "sc017845",
			"id": "2688E03A-9E5A-580D-8952-62B561C26841"
		},
		{
			"etask.entity": "sc017847",
			"id": "0E18E8FF-4978-52FC-76C6-2D0537DE13C6"
		},
		{
			"etask.entity": "sc014704",
			"id": "6683BC85-7457-58A0-4F29-F13315861FD2"
		},
		{
			"etask.entity": "sc014706",
			"id": "8A0D7C60-37EC-9086-2B63-50DF8EC39A34"
		},
		{
			"etask.entity": "sc014711",
			"id": "311FC695-D8AC-077A-214A-0596D9181433"
		},
		{
			"etask.entity": "sc014716",
			"id": "CC846028-7D67-FC84-A6BC-D41E8159544D"
		},
		{
			"etask.entity": "sc014721",
			"id": "3C36BD1B-A638-2C7C-CD6D-0C0F673660F7"
		},
		{
			"etask.entity": "sc014726",
			"id": "C8ECB085-817E-4D40-B229-6CFAB6AB7E9B"
		},
		{
			"etask.entity": "sc014728",
			"id": "700FE0E0-68FE-DA78-9E08-A694AE3FFAA9"
		},
		{
			"etask.entity": "sc014733",
			"id": "10E0CBB2-3C6D-9842-F582-05AD084D5CD0"
		},
		{
			"etask.entity": "sc014738",
			"id": "0BEF5D27-1DC5-1B9D-E056-9D4571CF892C"
		},
		{
			"etask.entity": "sc014743",
			"id": "0755968A-901C-EE9C-49A8-386B0ACE6676"
		},
		{
			"etask.entity": "sc014748",
			"id": "5223EBFE-FD97-73CA-9EA4-9EA222D96F55"
		},
		{
			"etask.entity": "sc014750",
			"id": "6EC7FF26-D462-BA71-ED00-FCC49134B919"
		},
		{
			"etask.entity": "sc014755",
			"id": "A097828D-B940-211A-389E-D478D62FD2B5"
		},
		{
			"etask.entity": "sc014760",
			"id": "F357DC88-BB63-3109-0C47-87CD18D4B047"
		},
		{
			"etask.entity": "sc014765",
			"id": "03E5869A-79E5-6DF6-87FF-7456CC59209B"
		},
		{
			"etask.entity": "sc014770",
			"id": "4BD5D834-5B5F-B00D-1A6F-397E70AB89F1"
		},
		{
			"etask.entity": "sc014772",
			"id": "59F58C77-5C1F-94F1-9EBE-D49EF3077BED"
		},
		{
			"etask.entity": "sc014777",
			"id": "DCF81CE5-D00E-AF72-0BCD-1C90BAF6C201"
		},
		{
			"etask.entity": "sc023651",
			"id": "0C5524FA-2362-C4D2-FE47-B037E93DE97D"
		},
		{
			"etask.entity": "sc017849",
			"id": "4BC78203-01F7-D71E-4448-6FCC8A4E9D1C"
		},
		{
			"etask.entity": "sc017850",
			"id": "456FFAE6-6EAE-AC60-BBAB-834A1873C599"
		},
		{
			"etask.entity": "sc017851",
			"id": "1FA2BB57-0244-DC01-7063-C296A4BCC438"
		},
		{
			"etask.entity": "sc017852",
			"id": "A0BD761D-085F-AD86-0EAF-B1CF43BA9554"
		},
		{
			"etask.entity": "sc017854",
			"id": "F6D41487-AF48-4133-8963-BC4C3CC4D77C"
		},
		{
			"etask.entity": "sc017856",
			"id": "20F8B279-97E5-18A7-7DFE-0855F66DDD8F"
		},
		{
			"etask.entity": "sc017857",
			"id": "D35A36CF-9DFE-7230-AEA8-25B6CE6ADFE6"
		},
		{
			"etask.entity": "sc017858",
			"id": "01190D99-FB79-25C0-49D6-664F7064F695"
		},
		{
			"etask.entity": "sc017859",
			"id": "F7A52EC2-B022-EDD3-9BB7-B453F0F64B40"
		},
		{
			"etask.entity": "sc017860",
			"id": "894B3051-72F4-E8C3-8574-E8143224B911"
		},
		{
			"etask.entity": "sc017861",
			"id": "E2FC351D-DFAB-61B9-DA84-0AF12BAC6495"
		},
		{
			"etask.entity": "sc017862",
			"id": "4D3C7AB6-CCF9-0034-C79B-F78C38EB0175"
		},
		{
			"etask.entity": "sc017865",
			"id": "2358C89B-459E-3747-5D09-85650D18D87E"
		},
		{
			"etask.entity": "sc017866",
			"id": "1692C285-93C6-F8B4-1086-CADE8FBC2CAE"
		},
		{
			"etask.entity": "sc017867",
			"id": "E8AE3FE8-5602-8A5B-A00B-529BD084304A"
		},
		{
			"etask.entity": "sc017868",
			"id": "E327DAE0-9572-7F19-A306-0EE3CEEEB096"
		},
		{
			"etask.entity": "sc017869",
			"id": "5E36397B-A24F-9373-B4C6-E63C23182967"
		},
		{
			"etask.entity": "sc023652",
			"id": "DBC35501-1774-1D5A-2A5F-F62DF9861C96"
		},
		{
			"etask.entity": "sc023653",
			"id": "711F1CFC-387F-1E03-034B-D5D0357BE883"
		},
		{
			"etask.entity": "sc023654",
			"id": "01843AC2-1C3B-26B9-926F-7F65DEEA7D17"
		},
		{
			"etask.entity": "sc017871",
			"id": "948861E6-6F15-78C1-C4DC-12C535868EB4"
		},
		{
			"etask.entity": "sc017872",
			"id": "8034BA54-288A-2221-558D-A91F7E9D5690"
		},
		{
			"etask.entity": "sc017873",
			"id": "EA48AD95-4462-79CC-9B07-9B3A25C820EE"
		},
		{
			"etask.entity": "sc017874",
			"id": "593390CB-B780-7C2C-0FAB-DAB1C20A3F8E"
		},
		{
			"etask.entity": "sc017878",
			"id": "BA214EC3-5FFC-782A-F1DF-65D7553AA331"
		},
		{
			"etask.entity": "sc017879",
			"id": "D789B7EA-D30C-16B3-DEE9-93048F075D33"
		},
		{
			"etask.entity": "sc017880",
			"id": "2CE3D1BF-FC5E-D26A-6F0D-E82FBD1BB7A7"
		},
		{
			"etask.entity": "sc017881",
			"id": "23AF6C61-1F25-E64C-B489-8DE956B34031"
		},
		{
			"etask.entity": "sc017882",
			"id": "B724DADA-3233-5051-3183-47DD9E8F225C"
		},
		{
			"etask.entity": "sc017883",
			"id": "49B41E2A-39F1-D39F-52FB-804BE9342DEF"
		},
		{
			"etask.entity": "sc017884",
			"id": "68441CFE-88A8-C3BA-82D4-003039B8A8F1"
		},
		{
			"etask.entity": "sc017885",
			"id": "A975ED8F-001A-A3D1-C441-B9787154CBC3"
		},
		{
			"etask.entity": "sc017886",
			"id": "7E558D46-A4E8-A7F3-86A6-D6D2E5F5FD25"
		},
		{
			"etask.entity": "sc017887",
			"id": "94B00E6D-4A1F-9BEB-60FC-59CA9B79A3B7"
		},
		{
			"etask.entity": "sc017890",
			"id": "0293C466-6F38-14DC-46D8-7B0522466F06"
		},
		{
			"etask.entity": "sc017891",
			"id": "E0D590F7-1760-AE33-BD33-FEC9DE27B8A2"
		},
		{
			"etask.entity": "sc023655",
			"id": "D3BD777F-DE46-2A48-DC08-A2EDF87F5ACD"
		},
		{
			"etask.entity": "sc017893",
			"id": "95E8A957-CC44-2846-63D7-1C02BB057A84"
		},
		{
			"etask.entity": "sc017894",
			"id": "E544023B-F100-B1E8-BF3D-7B4A2BBE2CE8"
		},
		{
			"etask.entity": "sc017895",
			"id": "8ABA726B-FD33-10F9-A26E-A141D5B50437"
		},
		{
			"etask.entity": "sc017896",
			"id": "A44FBD6A-BC59-49E7-3B05-310BC4D60AE7"
		},
		{
			"etask.entity": "sc017898",
			"id": "506934A1-0841-45F7-458A-68D85A2F7F2F"
		},
		{
			"etask.entity": "sc017899",
			"id": "1C9298F9-E5A2-9E62-6100-D3F63B1F4AA9"
		},
		{
			"etask.entity": "sc017900",
			"id": "D8549F59-964E-7160-EB30-1D6B2C1F24C4"
		},
		{
			"etask.entity": "sc017901",
			"id": "E7A374B7-E19E-986D-CBCB-35C2A4A93322"
		},
		{
			"etask.entity": "sc017903",
			"id": "A79477D8-ED75-D752-6759-F5EBBD45D5FB"
		},
		{
			"etask.entity": "sc017904",
			"id": "AB5329B6-CA28-D954-3EB9-535E305B1802"
		},
		{
			"etask.entity": "sc017905",
			"id": "6564D82C-B397-8987-6C8E-0619E5092EBC"
		},
		{
			"etask.entity": "sc017906",
			"id": "C2995A00-00B1-27CC-5393-2C0D349B7888"
		},
		{
			"etask.entity": "sc017908",
			"id": "8A5874E3-122C-0839-F4B5-335ADD3941B0"
		},
		{
			"etask.entity": "sc017909",
			"id": "18604929-62AB-83B6-E23B-48EC2C9AB675"
		},
		{
			"etask.entity": "sc017910",
			"id": "BAE4DE40-C5D4-01A7-F8E5-E6152AEE2FA0"
		},
		{
			"etask.entity": "sc017911",
			"id": "DEB9BC14-ED41-F4FB-23AD-BD8DFB3BB147"
		},
		{
			"etask.entity": "sc017913",
			"id": "73E6D6C0-1B83-D7FA-600E-C1764077F095"
		},
		{
			"etask.entity": "sc023656",
			"id": "DC20231D-09C3-FA6C-FF3C-05DC698CDC53"
		},
		{
			"etask.entity": "sc017915",
			"id": "732FA5F0-2CCB-1A24-9AA1-D0DD7D8ADA9B"
		},
		{
			"etask.entity": "sc017916",
			"id": "3679241F-0E84-9FF3-4AF5-AC2EFD0B1718"
		},
		{
			"etask.entity": "sc017917",
			"id": "A4A037DC-79E7-2DD0-886D-4AC0C4E4B34C"
		},
		{
			"etask.entity": "sc017918",
			"id": "CB4AA9F5-E55B-69CE-B841-8E91A374340B"
		},
		{
			"etask.entity": "sc017922",
			"id": "2C981A73-73DA-8776-F3AC-6CFDF4F3D863"
		},
		{
			"etask.entity": "sc017923",
			"id": "E6EB03CA-1FE8-EB71-D441-8955C0342244"
		},
		{
			"etask.entity": "sc017924",
			"id": "E19BE12F-A503-FA4B-5E68-5F7D5043D363"
		},
		{
			"etask.entity": "sc017925",
			"id": "EAACEBFB-3467-7F15-5CA9-04B2DD6A261F"
		},
		{
			"etask.entity": "sc017926",
			"id": "529E4A36-2FEF-03A4-39F6-ECF8578A7BE2"
		},
		{
			"etask.entity": "sc017927",
			"id": "2A360F29-71DF-43AF-E3DE-62B3039D968F"
		},
		{
			"etask.entity": "sc017928",
			"id": "F5C5CCCC-CFA1-E3EB-7F84-82B026E47459"
		},
		{
			"etask.entity": "sc017929",
			"id": "522FC17D-7613-F433-DAE7-1ED9D2EDD3B8"
		},
		{
			"etask.entity": "sc017930",
			"id": "58F72A0C-FD03-1DC5-8ED7-2BACB59195E0"
		},
		{
			"etask.entity": "sc017931",
			"id": "3FEC5FE3-B7C1-B585-CE12-A57DB774EC1F"
		},
		{
			"etask.entity": "sc017932",
			"id": "F4BB1983-28F8-3663-E82C-FB8A413DED20"
		},
		{
			"etask.entity": "sc017933",
			"id": "841E7EE9-FAB1-1768-28FB-CC6FA8A3F679"
		},
		{
			"etask.entity": "sc017935",
			"id": "BFD82AFB-56D6-4C06-4E81-8BA09A68EE81"
		},
		{
			"etask.entity": "sc014782",
			"id": "991D0E7E-68A5-A09F-EAE9-B6C0B59218EF"
		},
		{
			"etask.entity": "sc014787",
			"id": "B2628679-F17E-F0A6-E2E8-0E056059AE23"
		},
		{
			"etask.entity": "sc014792",
			"id": "95FE58C9-D1CB-C3BB-C409-56285EBC460D"
		},
		{
			"etask.entity": "sc014794",
			"id": "B8E6CA91-FC8F-A98E-8D4E-0DC0BAAC8019"
		},
		{
			"etask.entity": "sc014799",
			"id": "DD718156-36DE-8CDC-E8E5-61A7312E8152"
		},
		{
			"etask.entity": "sc014804",
			"id": "EACFBB8C-9E7B-81E7-75E9-0DDB080BE932"
		},
		{
			"etask.entity": "sc014809",
			"id": "C98DEDE4-51CA-D9A5-F2A7-AA64176C9600"
		},
		{
			"etask.entity": "sc014814",
			"id": "E37DD9E0-B91E-D0B0-373E-8E53B093A18B"
		},
		{
			"etask.entity": "sc014816",
			"id": "0251C198-FEF1-D2CE-24B6-6DD2B7AC3E15"
		},
		{
			"etask.entity": "sc014821",
			"id": "0FD75193-C725-7823-CB9D-707FC20DBF6D"
		},
		{
			"etask.entity": "sc014826",
			"id": "A3C7F52C-0BC4-EE6D-1F98-BBC8B3E25A7C"
		},
		{
			"etask.entity": "sc014831",
			"id": "260D02F7-FD5D-450A-1891-8B7E4C3F0D89"
		},
		{
			"etask.entity": "sc014836",
			"id": "88D32166-119D-25B7-EB91-69639A20D203"
		},
		{
			"etask.entity": "sc014838",
			"id": "577CAE9E-1C76-C495-ABBB-7769CB52617B"
		},
		{
			"etask.entity": "sc014843",
			"id": "4106D724-BDF8-46EA-50A2-07036126867B"
		},
		{
			"etask.entity": "sc014848",
			"id": "CE0CCC7F-16E9-07AC-FE18-AD46791BFE5A"
		},
		{
			"etask.entity": "sc014853",
			"id": "6649E56C-D04F-C1F3-488D-39884EC79326"
		},
		{
			"etask.entity": "sc014858",
			"id": "310FB203-9703-4267-9398-146938B43388"
		},
		{
			"etask.entity": "sc023657",
			"id": "AD3DA687-EF2D-1439-B40C-E689EDC20A49"
		},
		{
			"etask.entity": "sc017937",
			"id": "EC1A0A22-25AD-0184-4E54-989A434D8895"
		},
		{
			"etask.entity": "sc017938",
			"id": "00B70F5E-19F4-C152-6693-50516B32C404"
		},
		{
			"etask.entity": "sc017939",
			"id": "7FE42DD6-94AB-76F7-0662-127EA5914E64"
		},
		{
			"etask.entity": "sc017940",
			"id": "D7834696-8D26-A741-3CFF-D564CF975B66"
		},
		{
			"etask.entity": "sc017942",
			"id": "CEB8507E-9FA7-F346-5F55-AA7E70AA6EFC"
		},
		{
			"etask.entity": "sc017943",
			"id": "E39AD118-14F3-2F5F-4414-3579E96C8D4E"
		},
		{
			"etask.entity": "sc017944",
			"id": "C27B3790-3750-74C3-7BDC-BDF974459C64"
		},
		{
			"etask.entity": "sc017945",
			"id": "A6747E50-1A8E-A3A4-3130-1F993D7E5E1B"
		},
		{
			"etask.entity": "sc017947",
			"id": "75BAF262-1B06-D9FB-EECD-D2EF49EA37DF"
		},
		{
			"etask.entity": "sc017948",
			"id": "DB909DF1-ED88-227D-0F50-4127DF210405"
		},
		{
			"etask.entity": "sc017949",
			"id": "0211063F-DFF5-27E2-1511-8404D7882130"
		},
		{
			"etask.entity": "sc017950",
			"id": "765BFEC9-4EEF-B92D-42C6-C3B1F777E020"
		},
		{
			"etask.entity": "sc017952",
			"id": "AEA44C3A-E060-8F58-0A5B-374757C47A06"
		},
		{
			"etask.entity": "sc017953",
			"id": "72C5D3D7-67EF-1701-CF78-3624C3D4B061"
		},
		{
			"etask.entity": "sc017954",
			"id": "8B6C29C8-CE1F-6954-096B-8DDFCB231364"
		},
		{
			"etask.entity": "sc017955",
			"id": "011FC2BB-6056-154E-11C9-AE0C2F80D831"
		},
		{
			"etask.entity": "sc017957",
			"id": "D44982C9-32F1-9469-1A48-DDD2EA1D80DD"
		},
		{
			"etask.entity": "sc023658",
			"id": "FC422ACD-094A-7AA9-5537-08CD92C27201"
		},
		{
			"etask.entity": "sc017959",
			"id": "0BAD01C1-1CE6-B686-EE80-44B6FBA81EEF"
		},
		{
			"etask.entity": "sc017960",
			"id": "ACF15426-A4A3-C16B-422D-4701136159B9"
		},
		{
			"etask.entity": "sc017961",
			"id": "D6EC6361-872D-94B1-DB40-65D473BCF0EF"
		},
		{
			"etask.entity": "sc017962",
			"id": "30A74AD0-ABB0-CD3A-E37C-D436A97C32F9"
		},
		{
			"etask.entity": "sc017964",
			"id": "59028DAC-662C-97C1-603A-ADA8AB334709"
		},
		{
			"etask.entity": "sc017965",
			"id": "1AFF39D6-EF29-7005-00BB-C6ACCFC508E8"
		},
		{
			"etask.entity": "sc017966",
			"id": "083B110C-F7EA-3EF5-2E1E-76DE1B8DAC7A"
		},
		{
			"etask.entity": "sc017967",
			"id": "37569B1A-D0A7-CACE-4460-3AAC7CADA524"
		},
		{
			"etask.entity": "sc017969",
			"id": "448C806B-D69B-4EF4-F72A-DC1C6945C78C"
		},
		{
			"etask.entity": "sc017970",
			"id": "9C1F616D-E23F-F1E4-198D-4AA5B6EF2B70"
		},
		{
			"etask.entity": "sc017971",
			"id": "79FD408E-4245-C930-6119-A4E224949A91"
		},
		{
			"etask.entity": "sc017972",
			"id": "C12D5E4F-60AE-F6B8-E690-2E4BFC15D111"
		},
		{
			"etask.entity": "sc017974",
			"id": "F04BD795-B908-4348-E4A4-721B6E8674E2"
		},
		{
			"etask.entity": "sc017975",
			"id": "0A991D2D-AEC7-3FB0-846C-BB09B87F17AA"
		},
		{
			"etask.entity": "sc017976",
			"id": "83576C16-97E3-4FA9-1D18-68F3C1642911"
		},
		{
			"etask.entity": "sc017977",
			"id": "672FF9C7-F75D-1C5C-0824-18ECBB9BECE7"
		},
		{
			"etask.entity": "sc017979",
			"id": "EB2F24F1-CEF5-2AFC-B8E9-0A19269C1439"
		},
		{
			"etask.entity": "sc023659",
			"id": "ED362ECE-C7D7-A58D-83AB-04A2A4E59D92"
		},
		{
			"etask.entity": "sc017981",
			"id": "076431CB-1841-2041-9B5B-2650D9AE38D5"
		},
		{
			"etask.entity": "sc017982",
			"id": "49C14E66-D939-DD4E-5200-790320605227"
		},
		{
			"etask.entity": "sc017983",
			"id": "61B51274-4E23-4CE8-D46C-46C51FB529BE"
		},
		{
			"etask.entity": "sc017984",
			"id": "7A05766B-9745-F384-C430-6790E0F33057"
		},
		{
			"etask.entity": "sc017986",
			"id": "A6BD1209-259D-0322-6868-CA5DA30622A5"
		},
		{
			"etask.entity": "sc017987",
			"id": "DEAD54C5-68CE-28F0-7C9E-CC6D393FF5C2"
		},
		{
			"etask.entity": "sc017988",
			"id": "1A3255DB-2415-2707-F9B8-87B6C6A5A398"
		},
		{
			"etask.entity": "sc017989",
			"id": "5BA12BA0-577B-B93C-55D6-A151AE30ECB4"
		},
		{
			"etask.entity": "sc017991",
			"id": "ACA6259C-051C-4878-934F-B0F81889408C"
		},
		{
			"etask.entity": "sc017992",
			"id": "99611ED4-8535-0385-A213-83C71A7D3ACD"
		},
		{
			"etask.entity": "sc017993",
			"id": "D3BF9EB6-A285-4793-F689-E8AA9231466A"
		},
		{
			"etask.entity": "sc017994",
			"id": "DA3F7B0E-BA52-A15D-D41D-53B51C281D1C"
		},
		{
			"etask.entity": "sc017996",
			"id": "89B92393-E1B7-3DA5-A809-D5678CF383EC"
		},
		{
			"etask.entity": "sc017997",
			"id": "2A5410E8-73BE-8A55-4045-35E1D35C6481"
		},
		{
			"etask.entity": "sc017998",
			"id": "87E777C8-48F4-148A-A988-1F7DA8C4145F"
		},
		{
			"etask.entity": "sc017999",
			"id": "27F640D0-988B-91DF-9C9D-169D379AD890"
		},
		{
			"etask.entity": "sc018001",
			"id": "BD7FDDAA-B086-60A1-AE2D-A86C98D39326"
		},
		{
			"etask.entity": "sc014860",
			"id": "387B50AB-B7BD-B3E0-AA5B-5305FA298B65"
		},
		{
			"etask.entity": "sc014865",
			"id": "368B610F-94C8-F6E5-8A59-1EAF57430730"
		},
		{
			"etask.entity": "sc014870",
			"id": "A22DF7D1-21F2-3F1C-7695-03F19ACEF4B4"
		},
		{
			"etask.entity": "sc014875",
			"id": "A7E458AE-8B93-4EA2-037C-A57C99D1836C"
		},
		{
			"etask.entity": "sc014880",
			"id": "1A6DFCC9-BC42-79E8-BC46-9C5F1B77D151"
		},
		{
			"etask.entity": "sc014882",
			"id": "860230BB-D5C4-F62D-61D0-8BB884D87CD0"
		},
		{
			"etask.entity": "sc014887",
			"id": "77CA15A1-D579-A62F-7870-6A5AFB90059D"
		},
		{
			"etask.entity": "sc014892",
			"id": "64A9C122-247E-E97A-F8AC-8F14186731A8"
		},
		{
			"etask.entity": "sc014897",
			"id": "AD944D04-B912-2B0D-0566-F994157BAB82"
		},
		{
			"etask.entity": "sc014902",
			"id": "4F6E62A4-2FA1-A63A-17FB-40D9ECA011DB"
		},
		{
			"etask.entity": "sc014904",
			"id": "88AA9696-728F-A359-EDA1-5165818F38CF"
		},
		{
			"etask.entity": "sc014909",
			"id": "4229D7C7-FD77-0336-0DA7-0B50B3CB9A4E"
		},
		{
			"etask.entity": "sc014914",
			"id": "2180783D-2B21-C874-C26B-402CDF937B46"
		},
		{
			"etask.entity": "sc014919",
			"id": "F94575E4-D513-D64D-8578-6702B09A1536"
		},
		{
			"etask.entity": "sc014924",
			"id": "C7084D59-D443-0EC2-5EBF-B60BC0EA3400"
		},
		{
			"etask.entity": "sc014926",
			"id": "18A8492F-5DC8-6294-3BB8-D0FD9226FF08"
		},
		{
			"etask.entity": "sc014931",
			"id": "C8D8DEFE-2B68-4CFA-AABC-B29C7DB43F5F"
		},
		{
			"etask.entity": "sc014936",
			"id": "E3FD4079-FCBF-5A89-BDAD-386659B1CF53"
		},
		{
			"etask.entity": "sc023660",
			"id": "B1083181-1C8D-5183-1CEB-69CF52FA3660"
		},
		{
			"etask.entity": "sc018003",
			"id": "E0999687-920F-387E-6165-2F75B0FC5074"
		},
		{
			"etask.entity": "sc018004",
			"id": "C19096CD-6979-9383-454F-9D33EBB5AF9B"
		},
		{
			"etask.entity": "sc018005",
			"id": "9497C504-98AB-F2A2-2AEF-64EF536C92AC"
		},
		{
			"etask.entity": "sc018006",
			"id": "ECFE865B-DFFE-4A06-00A4-6FFAAC030EDA"
		},
		{
			"etask.entity": "sc018008",
			"id": "436261CF-D3A9-4700-826B-DB4712D7B897"
		},
		{
			"etask.entity": "sc018009",
			"id": "FF0DD7AB-3183-1E8A-6903-8489815B224B"
		},
		{
			"etask.entity": "sc018010",
			"id": "9929DDAA-8361-68F3-B643-20A732DA1CA9"
		},
		{
			"etask.entity": "sc018011",
			"id": "F498171B-4C96-6C7E-953A-8B88575A94EF"
		},
		{
			"etask.entity": "sc018013",
			"id": "78554AA8-AFEA-BE30-DCD3-C89C292C5A07"
		},
		{
			"etask.entity": "sc018014",
			"id": "35FA2F63-8A39-3100-E0B6-15DC1D690982"
		},
		{
			"etask.entity": "sc018015",
			"id": "1C09F10E-C7CC-5C80-4BC8-55D706EB860A"
		},
		{
			"etask.entity": "sc018016",
			"id": "315F55E2-4F9B-DE65-F71B-92118DB5246A"
		},
		{
			"etask.entity": "sc018018",
			"id": "879348E5-F542-13BE-C077-16FAF423C625"
		},
		{
			"etask.entity": "sc018019",
			"id": "68283449-430B-3082-693C-FA1EA82B6CE0"
		},
		{
			"etask.entity": "sc018020",
			"id": "4FE0FEE8-1F37-2F8E-2926-0F5A46B86251"
		},
		{
			"etask.entity": "sc018021",
			"id": "978DE6CB-E264-E41E-E552-341105947BD4"
		},
		{
			"etask.entity": "sc018023",
			"id": "EF6CD108-761D-686E-FD7A-63F655FD173E"
		},
		{
			"etask.entity": "sc023661",
			"id": "91EA94AC-E024-871A-246B-373AC1C463BF"
		},
		{
			"etask.entity": "sc018025",
			"id": "860DED61-876B-40C8-B3E1-AF2A91BA0620"
		},
		{
			"etask.entity": "sc018026",
			"id": "812B041A-3912-4A4A-855A-06D3E2A37CD7"
		},
		{
			"etask.entity": "sc018027",
			"id": "71F9CCF4-2FCD-41ED-988C-64265B83AA7C"
		},
		{
			"etask.entity": "sc018028",
			"id": "234AD6FF-F83C-A29E-D9A2-2D77005166AD"
		},
		{
			"etask.entity": "sc018030",
			"id": "13DDCD6D-C85F-02D5-B8F8-E12EF9E03B56"
		},
		{
			"etask.entity": "sc018031",
			"id": "E6211BAB-7F46-0E25-8B9C-5F9422D9E400"
		},
		{
			"etask.entity": "sc018032",
			"id": "360BBB9C-BEB7-1788-B206-5E119BE1C726"
		},
		{
			"etask.entity": "sc018033",
			"id": "B23BCB61-2320-A2BB-34F3-FBB18231698C"
		},
		{
			"etask.entity": "sc018035",
			"id": "A2EFB0E0-C437-7BA2-B1F7-6BB3F8D10235"
		},
		{
			"etask.entity": "sc018036",
			"id": "7DF6A2A9-5AE7-A411-5F98-383280B5946F"
		},
		{
			"etask.entity": "sc018037",
			"id": "234E4248-5945-E882-4D79-F456A7FE4000"
		},
		{
			"etask.entity": "sc018038",
			"id": "C37C7A32-5BA2-7D74-3F45-4120C1767F7C"
		},
		{
			"etask.entity": "sc018040",
			"id": "4D480CFC-5294-0C08-B554-7131ADB13336"
		},
		{
			"etask.entity": "sc018041",
			"id": "371ADA10-1879-AC20-4965-90550B413614"
		},
		{
			"etask.entity": "sc018042",
			"id": "440CFDEB-D32E-2517-40D0-3B5FE4D1F827"
		},
		{
			"etask.entity": "sc018043",
			"id": "EB607C81-3753-BC34-76A8-5EF4B3BA04D7"
		},
		{
			"etask.entity": "sc018045",
			"id": "1E711097-A205-61F4-5CA4-4894BB0E5DA6"
		},
		{
			"etask.entity": "sc023662",
			"id": "7849FF33-4F94-D389-AC6F-66EC05E1A304"
		},
		{
			"etask.entity": "sc018047",
			"id": "F84BD717-FFCA-5769-CABE-837E3B84436B"
		},
		{
			"etask.entity": "sc018048",
			"id": "B0631E1F-F269-1BBC-C5AB-98854D0D39FA"
		},
		{
			"etask.entity": "sc018049",
			"id": "584FDB15-FDD6-0D06-2682-C107DCBDE6AB"
		},
		{
			"etask.entity": "sc018050",
			"id": "CF40BEA5-1D94-DF17-2F94-D0F0A72574CD"
		},
		{
			"etask.entity": "sc018052",
			"id": "1024720A-F7B7-3B35-4EAC-470B46F3E40A"
		},
		{
			"etask.entity": "sc018053",
			"id": "6336168D-83FF-6555-F5FE-CC8BEFF806E2"
		},
		{
			"etask.entity": "sc018054",
			"id": "16889C0C-3D08-6F30-BFC1-772A412F329A"
		},
		{
			"etask.entity": "sc018055",
			"id": "0E38F271-28BB-30AC-E8CE-BAA303038A4B"
		},
		{
			"etask.entity": "sc018057",
			"id": "6DC1333F-DDE3-BE20-A1FF-15EE1E7C602A"
		},
		{
			"etask.entity": "sc018058",
			"id": "A483DDB3-A43F-D954-98CD-F6CB374C9742"
		},
		{
			"etask.entity": "sc018059",
			"id": "6A083814-4C9F-5260-FD89-9B1D2A2BF0CD"
		},
		{
			"etask.entity": "sc018060",
			"id": "71F4FDB0-04BA-E26A-6C78-57047B9719D0"
		},
		{
			"etask.entity": "sc018062",
			"id": "87AAA78E-B3C7-79D6-47BA-6ACDF37BE79C"
		},
		{
			"etask.entity": "sc018063",
			"id": "6290875D-33EE-08C1-766A-3B05922B960A"
		},
		{
			"etask.entity": "sc018064",
			"id": "3907A615-747A-862D-012A-E1AD5E6EFAAD"
		},
		{
			"etask.entity": "sc018065",
			"id": "03FEB932-AB8F-6323-0032-FCE9444B2578"
		},
		{
			"etask.entity": "sc018067",
			"id": "C0CF111F-D176-B67B-9734-83CC5D047E5F"
		},
		{
			"etask.entity": "sc014941",
			"id": "4773730B-87AC-DC43-270E-3FEF975CA524"
		},
		{
			"etask.entity": "sc014946",
			"id": "DD6B3FC5-95A6-E556-F709-05527478C118"
		},
		{
			"etask.entity": "sc014948",
			"id": "0E268237-7CC4-0C52-F6FD-BA037FF9B8D9"
		},
		{
			"etask.entity": "sc014953",
			"id": "E63685A8-456F-0971-AFE7-4C49F9C55F2B"
		},
		{
			"etask.entity": "sc014958",
			"id": "07B8DC1B-D8B8-4962-DB4E-1D4188A1B402"
		},
		{
			"etask.entity": "sc014963",
			"id": "4E433010-55F6-FCEB-FCE3-B86DDA133F44"
		},
		{
			"etask.entity": "sc014968",
			"id": "80D75272-67C6-27B2-D6F8-594C440E3830"
		},
		{
			"etask.entity": "sc014970",
			"id": "B82E06BE-5D03-0314-851A-D32EFDEABBAA"
		},
		{
			"etask.entity": "sc014975",
			"id": "7C4FE578-5186-E519-7454-81CB32764A73"
		},
		{
			"etask.entity": "sc014980",
			"id": "3F22C24C-3B3E-EF98-3B70-138F77181EA3"
		},
		{
			"etask.entity": "sc014985",
			"id": "A66FA692-9183-1BF8-500F-992888F611BA"
		},
		{
			"etask.entity": "sc014990",
			"id": "E87749B3-5BCD-C2AA-D3D6-55EB84F49893"
		},
		{
			"etask.entity": "sc014992",
			"id": "8C48B1DB-1904-5F9E-B4AE-6E835F7EF11E"
		},
		{
			"etask.entity": "sc014997",
			"id": "26A0FDAE-3385-531A-5A34-2A20F52CBF0E"
		},
		{
			"etask.entity": "sc015002",
			"id": "40743BE4-EED5-1538-607C-3E2F754585F5"
		},
		{
			"etask.entity": "sc015007",
			"id": "BF4B3825-E22E-98CC-EEC7-159D2BA361AD"
		},
		{
			"etask.entity": "sc015012",
			"id": "0B1AA0E8-C731-206C-B1EB-D48947B8DA9D"
		},
		{
			"etask.entity": "sc015014",
			"id": "2DF420E2-135A-5A85-39C1-4EC7115CD6FB"
		},
		{
			"etask.entity": "sc023663",
			"id": "024AA6FB-D010-42C4-1F2F-759A422ABE42"
		},
		{
			"etask.entity": "sc018069",
			"id": "A9A34B66-FD99-4465-DE10-83800E6E62AE"
		},
		{
			"etask.entity": "sc018070",
			"id": "F776B3E9-4FCA-B8D0-8122-5C8E46691C69"
		},
		{
			"etask.entity": "sc018071",
			"id": "696CDF2B-B8B4-1F4F-1D59-6ADAD197D090"
		},
		{
			"etask.entity": "sc018072",
			"id": "F45AE08B-8B1C-33D1-A75B-4BE0540E7AAE"
		},
		{
			"etask.entity": "sc018074",
			"id": "A991CAC4-00B1-A245-23D2-BFB4D4AA9B61"
		},
		{
			"etask.entity": "sc018075",
			"id": "D9A13DA5-064A-7411-2BD9-AAF6E7AD8238"
		},
		{
			"etask.entity": "sc018076",
			"id": "2548EBC9-8294-BD0E-D512-89AD7D59114D"
		},
		{
			"etask.entity": "sc018077",
			"id": "2EAE3963-710B-7C49-176D-AF35AA19493F"
		},
		{
			"etask.entity": "sc018079",
			"id": "DD500FA6-5DF1-BF85-C306-2F0BAFFC10D4"
		},
		{
			"etask.entity": "sc018080",
			"id": "9D32E3CE-797D-E395-8DAB-D8336079F4DC"
		},
		{
			"etask.entity": "sc018081",
			"id": "DEBBE67A-DDED-0C7A-6B12-23B69EA912A0"
		},
		{
			"etask.entity": "sc018082",
			"id": "A9886D10-6F76-4BC7-0800-DABC4C86DCD7"
		},
		{
			"etask.entity": "sc018084",
			"id": "11385A8C-61E9-0A88-3BD8-1CCC9A1D9706"
		},
		{
			"etask.entity": "sc018085",
			"id": "C45C7C75-B9EC-59DB-09AA-80A1FEEF79B8"
		},
		{
			"etask.entity": "sc018086",
			"id": "337E7769-176F-7185-2BF4-3FB793A6CD5E"
		},
		{
			"etask.entity": "sc018087",
			"id": "CD0EC544-5A97-2872-83CC-5BE331744809"
		},
		{
			"etask.entity": "sc018089",
			"id": "DED074D3-728C-E79F-C223-454A000D27D7"
		},
		{
			"etask.entity": "sc023664",
			"id": "2E1A3E7B-630D-9AFD-0F09-F46F9EF8CB9D"
		},
		{
			"etask.entity": "sc018091",
			"id": "87B6229C-A94F-17B6-6F06-B0B3E1E156EF"
		},
		{
			"etask.entity": "sc018092",
			"id": "BC8D9F26-AECB-2676-F850-AA95A2AAB8C5"
		},
		{
			"etask.entity": "sc018093",
			"id": "D9ADC853-4E2D-E10C-FD4A-B41EB89DC74D"
		},
		{
			"etask.entity": "sc018094",
			"id": "E3C32FCE-6EFB-AD93-8F61-DE3DE40E7DB5"
		},
		{
			"etask.entity": "sc018096",
			"id": "F27232DC-A12A-2F23-1E6D-61B135B2ABCC"
		},
		{
			"etask.entity": "sc018097",
			"id": "DEADE0D1-2BCA-170C-F0A6-0210D7181ABD"
		},
		{
			"etask.entity": "sc018098",
			"id": "CEEA1C54-352D-0367-493E-486EDA1A7004"
		},
		{
			"etask.entity": "sc018099",
			"id": "EB91379E-218B-6A12-BD57-EEF06A793C38"
		},
		{
			"etask.entity": "sc018101",
			"id": "6412BBBA-7C74-E479-E578-3F1C015FF117"
		},
		{
			"etask.entity": "sc018102",
			"id": "E31B2918-955D-C397-99CD-168013CC44AC"
		},
		{
			"etask.entity": "sc018103",
			"id": "26EC6C1B-6484-57C5-72B3-A033449C5D6E"
		},
		{
			"etask.entity": "sc018104",
			"id": "4586B6E0-C909-59EA-D0A6-318F615E2C36"
		},
		{
			"etask.entity": "sc018106",
			"id": "8FC25BF7-9815-85A9-83EF-897D987F385B"
		},
		{
			"etask.entity": "sc018107",
			"id": "7EB02FF6-7C45-8D90-03AA-8034908968EA"
		},
		{
			"etask.entity": "sc018108",
			"id": "4AA8C5C8-8DA9-FD73-38BB-A35EA078374C"
		},
		{
			"etask.entity": "sc018109",
			"id": "90E5191B-A295-5326-C957-0B39BAFFEDD7"
		},
		{
			"etask.entity": "sc018111",
			"id": "BB0CF9A3-414E-408A-3280-1268B2B524C1"
		},
		{
			"etask.entity": "sc023665",
			"id": "C6C0F962-E29C-F27B-6064-79FAF3276237"
		},
		{
			"etask.entity": "sc018113",
			"id": "15A6BE07-49AB-D37D-B85B-65A4ACF55EFB"
		},
		{
			"etask.entity": "sc018114",
			"id": "AE1DC2BD-3C0E-0B57-684C-FC9F61E63B40"
		},
		{
			"etask.entity": "sc018115",
			"id": "C6B97473-6C7C-026B-F9FD-0B04B4EA088D"
		},
		{
			"etask.entity": "sc018116",
			"id": "8F28729F-90B9-01C3-D2BB-032716C0D64A"
		},
		{
			"etask.entity": "sc018118",
			"id": "7B665987-2D3C-68C9-2161-A5673A9B9EEC"
		},
		{
			"etask.entity": "sc018119",
			"id": "DAF3C3A1-98DD-8A63-0719-218C5D818931"
		},
		{
			"etask.entity": "sc018120",
			"id": "72D49370-B6C0-0EEF-82F4-645C78283D35"
		},
		{
			"etask.entity": "sc018121",
			"id": "7F219FE3-B25E-7F38-D173-C826E8E5DA07"
		},
		{
			"etask.entity": "sc018123",
			"id": "2009DD2F-52E0-4D67-27FE-B0714ECE5319"
		},
		{
			"etask.entity": "sc018124",
			"id": "80396B3F-5D0A-D08B-7D9E-48AD1AB0E0FE"
		},
		{
			"etask.entity": "sc018125",
			"id": "6B0497EC-42B6-E900-DACB-220D9140B30A"
		},
		{
			"etask.entity": "sc018126",
			"id": "AE50CE42-CE23-31D7-A688-132BF018340D"
		},
		{
			"etask.entity": "sc018128",
			"id": "CDAA1FC9-E284-22E9-111F-43EA91D242C1"
		},
		{
			"etask.entity": "sc018129",
			"id": "DDB0733A-AB92-AECA-7021-B05C6297B171"
		},
		{
			"etask.entity": "sc018130",
			"id": "E2C9F2F4-6DCF-D1DB-D8E9-17F6D305A6D8"
		},
		{
			"etask.entity": "sc018131",
			"id": "21ECC7C8-C2EB-18BD-0FD5-394AE8671B5A"
		},
		{
			"etask.entity": "sc018133",
			"id": "B60624CE-93F2-9F8A-1B27-39F9E5AD6414"
		},
		{
			"etask.entity": "sc023666",
			"id": "3E9415EB-6260-D0B7-A84E-9CAAB822E11C"
		},
		{
			"etask.entity": "sc018135",
			"id": "FECBCCED-BBB5-BC61-3FB7-577E91C4664B"
		},
		{
			"etask.entity": "sc018136",
			"id": "4F10569A-84F5-D459-64BE-79F8E153F036"
		},
		{
			"etask.entity": "sc018137",
			"id": "7C86C3C0-3BEF-0D6A-1F5E-7489382DD7AE"
		},
		{
			"etask.entity": "sc018138",
			"id": "410D2D00-937B-B252-84C0-5B00B57DAD2D"
		},
		{
			"etask.entity": "sc018140",
			"id": "90E09B4A-CE7E-6FD9-281C-BBD269B9BF31"
		},
		{
			"etask.entity": "sc018141",
			"id": "C600F50C-5863-D413-8C7E-B64E02FA2935"
		},
		{
			"etask.entity": "sc018142",
			"id": "FA2B32CD-4D6E-BB95-7E4F-90F9D4CD6679"
		},
		{
			"etask.entity": "sc018143",
			"id": "EF27A9BD-7C2D-1643-9482-43BA7A587F12"
		},
		{
			"etask.entity": "sc018145",
			"id": "F5B99BDA-B897-9C9C-FB08-CC90B30E2191"
		},
		{
			"etask.entity": "sc018146",
			"id": "BF31A87B-9552-F167-851E-BAF0CBB6A0C3"
		},
		{
			"etask.entity": "sc018147",
			"id": "9E821177-A8CE-562C-7CB9-98CA208AAB77"
		},
		{
			"etask.entity": "sc018148",
			"id": "3E321C38-3B97-D175-6A75-E149648B63A3"
		},
		{
			"etask.entity": "sc018150",
			"id": "CBB2C0A3-C462-A508-B8E1-26C2B5475EC8"
		},
		{
			"etask.entity": "sc018151",
			"id": "49B36424-0ACA-8E80-022A-E5E6F0C449B6"
		},
		{
			"etask.entity": "sc018152",
			"id": "DC0AF446-35C1-523E-7988-5997584876C9"
		},
		{
			"etask.entity": "sc018153",
			"id": "E2888543-8D30-AE87-D185-304FA63DA965"
		},
		{
			"etask.entity": "sc018155",
			"id": "7E50BF2E-1EB1-8470-1CF6-4934EBC89746"
		},
		{
			"etask.entity": "sc015019",
			"id": "52FF8E61-AA8B-485B-0A84-61C18F8D3523"
		},
		{
			"etask.entity": "sc015024",
			"id": "8D7446DC-3A83-5053-971A-B166A4A13F87"
		},
		{
			"etask.entity": "sc015029",
			"id": "344BA16D-C5C6-D472-550E-D264B94AE7C4"
		},
		{
			"etask.entity": "sc015034",
			"id": "0475A335-F777-8FB4-1D5F-836E25C1FAA6"
		},
		{
			"etask.entity": "sc015036",
			"id": "3DC9D533-2C8A-DD50-522E-E2EB8802E439"
		},
		{
			"etask.entity": "sc015041",
			"id": "98F0D655-D16F-1C01-9D37-22C82E7521C4"
		},
		{
			"etask.entity": "sc015046",
			"id": "A7254546-2DC6-7D02-8C3E-AB86449B9233"
		},
		{
			"etask.entity": "sc015051",
			"id": "1F66FC17-D58A-BFF0-3811-DD63AA2FCB44"
		},
		{
			"etask.entity": "sc015056",
			"id": "D97AD2A5-E983-2EA3-489E-846F4DF25175"
		},
		{
			"etask.entity": "sc015058",
			"id": "59FBB0C4-C9CC-A1C3-EC7E-5FE548909F26"
		},
		{
			"etask.entity": "sc015063",
			"id": "97AB5CB6-1A76-7446-54D1-92F3FD7C1935"
		},
		{
			"etask.entity": "sc015068",
			"id": "1482267D-AA4B-B71B-348D-9DE5E17FD617"
		},
		{
			"etask.entity": "sc015073",
			"id": "A8669AE4-C9E3-D7E7-65E7-96F8EE7BA21C"
		},
		{
			"etask.entity": "sc015078",
			"id": "9AE8BF31-DBE4-C234-6EC7-3FE4C1356B10"
		},
		{
			"etask.entity": "sc015080",
			"id": "61B17343-7134-6F48-C4EF-3181AB6083FB"
		},
		{
			"etask.entity": "sc015085",
			"id": "484CCCE3-8450-BCAC-D180-7ABB9A071718"
		},
		{
			"etask.entity": "sc015090",
			"id": "8E170782-889F-918E-F52B-0BF62510FE4C"
		},
		{
			"etask.entity": "sc015095",
			"id": "6908F4BE-A23E-5453-1529-F0E4CBA2FB97"
		},
		{
			"etask.entity": "sc023667",
			"id": "8BACCBF1-885A-7304-1B04-1F750BF1B114"
		},
		{
			"etask.entity": "sc018157",
			"id": "1F05362A-9B14-7244-710B-FB0C352A09C5"
		},
		{
			"etask.entity": "sc018158",
			"id": "FED08327-F087-83AB-1E20-0C5D415D728D"
		},
		{
			"etask.entity": "sc018159",
			"id": "2FF040C4-07D0-F1A4-2CA1-5C30D750FFE3"
		},
		{
			"etask.entity": "sc018160",
			"id": "931B01F8-E604-9662-5632-E794DF8DC14B"
		},
		{
			"etask.entity": "sc018162",
			"id": "28EE2AA5-9A17-CA78-1CED-FE4346C9D4BE"
		},
		{
			"etask.entity": "sc018163",
			"id": "22461473-AD89-022C-B52B-7F3B9A76CB4B"
		},
		{
			"etask.entity": "sc018164",
			"id": "8F5D7EA1-611A-9BDF-EEE2-093733DC5CF0"
		},
		{
			"etask.entity": "sc018165",
			"id": "37869F43-2B61-53C0-1BEF-4F7DCC6434EE"
		},
		{
			"etask.entity": "sc018167",
			"id": "7FB72DD4-78CB-74C0-FC39-D483BA9036F5"
		},
		{
			"etask.entity": "sc018168",
			"id": "7A80D0C9-C0A4-30EE-0170-7989AA436B53"
		},
		{
			"etask.entity": "sc018169",
			"id": "C0FDF6CE-D9D5-0D0C-75DC-FC895085586B"
		},
		{
			"etask.entity": "sc018170",
			"id": "2C301046-B91C-7EB2-6338-F43CE03D6819"
		},
		{
			"etask.entity": "sc018172",
			"id": "3AA21E6E-6BB1-5F92-655E-C9A11027953F"
		},
		{
			"etask.entity": "sc018173",
			"id": "2DF2B7D9-8CF3-110B-A928-7B79D03B14E0"
		},
		{
			"etask.entity": "sc018174",
			"id": "C7792D38-969C-4E41-E305-DF9ABFCB12EC"
		},
		{
			"etask.entity": "sc018175",
			"id": "B463F855-F6EF-CDFB-2309-72189AB6EE9D"
		},
		{
			"etask.entity": "sc018177",
			"id": "98442267-105D-CB98-8DB7-36D08E480D76"
		},
		{
			"etask.entity": "sc023668",
			"id": "E252BC5F-3206-469B-1217-210A725812FE"
		},
		{
			"etask.entity": "sc018179",
			"id": "12020769-15F4-C171-8AFD-014A25302268"
		},
		{
			"etask.entity": "sc018180",
			"id": "165D2739-29E7-DA43-6676-81A214428BCC"
		},
		{
			"etask.entity": "sc018181",
			"id": "BF8F68FA-A19A-0D08-2A12-4C54411D539A"
		},
		{
			"etask.entity": "sc018182",
			"id": "8F0DCCB8-B873-8DAA-2439-2DA39875D5BC"
		},
		{
			"etask.entity": "sc018184",
			"id": "5A22377A-A18E-B7FF-6101-CAA24052C75E"
		},
		{
			"etask.entity": "sc018185",
			"id": "E80D19A0-A221-134C-3B88-9A34A947CAF7"
		},
		{
			"etask.entity": "sc018186",
			"id": "39BDE125-7B47-D2F3-7EDD-E5B0E05CCB06"
		},
		{
			"etask.entity": "sc018187",
			"id": "139D96B4-823A-6AEF-ACF5-2EB91F25386D"
		},
		{
			"etask.entity": "sc018189",
			"id": "A0D326F5-2D44-01F3-9BBC-8077CF15F3C6"
		},
		{
			"etask.entity": "sc018190",
			"id": "70BE444D-D283-F646-862A-FEE42D91080D"
		},
		{
			"etask.entity": "sc018191",
			"id": "1A54C9F2-B123-92FD-07CD-7CB1DDA4B705"
		},
		{
			"etask.entity": "sc018192",
			"id": "8005DB25-87BB-A2D1-6622-6FB90186319E"
		},
		{
			"etask.entity": "sc018194",
			"id": "E5DBCD4D-F41B-639D-B021-1ABBC9FAF39E"
		},
		{
			"etask.entity": "sc018195",
			"id": "538E7A32-D5BD-FF42-39B2-448503FEEE5E"
		},
		{
			"etask.entity": "sc018196",
			"id": "A19C0EEA-5B28-2F42-03EC-44E7CDE9893E"
		},
		{
			"etask.entity": "sc018197",
			"id": "D4B590CD-24EA-2EA3-5B9B-B65D3A056E46"
		},
		{
			"etask.entity": "sc018199",
			"id": "A918A84A-3731-D08F-F56F-F66E8256B071"
		},
		{
			"etask.entity": "sc023669",
			"id": "134B3CB8-A9BE-385E-B1BF-40CCAC58C54A"
		},
		{
			"etask.entity": "sc018201",
			"id": "EA68E2EC-00CC-D09E-F8D8-EA4D21FE7D0B"
		},
		{
			"etask.entity": "sc018202",
			"id": "D7F01E44-B7B5-8DEB-7FAD-BDCD24A0E120"
		},
		{
			"etask.entity": "sc018203",
			"id": "81E7F75C-EFD6-14F9-443C-75B9A68DE2CC"
		},
		{
			"etask.entity": "sc018204",
			"id": "E4A21136-295F-F2A6-370D-73BE62F9D84E"
		},
		{
			"etask.entity": "sc018206",
			"id": "F75C0BA8-D42D-A875-8444-64FBB7E69EBF"
		},
		{
			"etask.entity": "sc018207",
			"id": "9FDA333E-C3E2-A849-D910-41A5C1454A89"
		},
		{
			"etask.entity": "sc018208",
			"id": "3C13758F-649F-6146-B21D-41E829D7D362"
		},
		{
			"etask.entity": "sc018209",
			"id": "7BE9A1B9-A717-22A7-E5CF-67315E408844"
		},
		{
			"etask.entity": "sc018211",
			"id": "E589C6BA-9970-E28E-3142-B8F8C7EAFB30"
		},
		{
			"etask.entity": "sc018212",
			"id": "EB642CA1-F786-CF83-2849-DDBBB8D33F68"
		},
		{
			"etask.entity": "sc018213",
			"id": "C3CB9B9D-4AD0-BD2B-2CA2-BE6832469D67"
		},
		{
			"etask.entity": "sc018214",
			"id": "0B232645-1AB0-062B-9AD5-724C942BA114"
		},
		{
			"etask.entity": "sc018216",
			"id": "07519934-339B-B7B8-8B9A-EBE467A0162C"
		},
		{
			"etask.entity": "sc018217",
			"id": "E6A94620-6D6F-FEB1-E373-23A3A0612559"
		},
		{
			"etask.entity": "sc018218",
			"id": "DC800941-E767-C220-3881-D754A5F70380"
		},
		{
			"etask.entity": "sc018219",
			"id": "AAEE33F1-FB55-FB7C-034B-DADC4FE45A77"
		},
		{
			"etask.entity": "sc018221",
			"id": "EF7A83B3-F376-AF52-E120-4EF2C23D9869"
		},
		{
			"etask.entity": "sc023670",
			"id": "6C283E15-9C4A-F64B-1080-DE5A81EAC76D"
		},
		{
			"etask.entity": "sc023671",
			"id": "AA3A552B-7290-A445-CBE6-AFA17D9491BF"
		},
		{
			"etask.entity": "sc023672",
			"id": "78ED610B-A5E0-B177-A903-757575D3DD19"
		},
		{
			"etask.entity": "sc023673",
			"id": "56D36C41-30BD-2946-5EB4-A88E6930C56C"
		},
		{
			"etask.entity": "sc018223",
			"id": "516C9184-BC2E-160E-44B4-11E80D82B9C7"
		},
		{
			"etask.entity": "sc018224",
			"id": "9C186710-A1A7-3804-895A-014229B31B28"
		},
		{
			"etask.entity": "sc018225",
			"id": "D6731D5D-1AD7-D53D-09EA-DECF7DD11F1E"
		},
		{
			"etask.entity": "sc018226",
			"id": "E8B19B3B-3894-4284-36EE-55F1DDAF715E"
		},
		{
			"etask.entity": "sc018228",
			"id": "D8216A57-9F5E-C60A-B606-5CED007D24D5"
		},
		{
			"etask.entity": "sc018229",
			"id": "B6C67C95-8323-20B8-DFA7-1D3076F0FFD6"
		},
		{
			"etask.entity": "sc018230",
			"id": "7852647F-9A70-9027-2346-119EBAA9460B"
		},
		{
			"etask.entity": "sc018231",
			"id": "359A7E9E-2BA9-BB51-689F-1B5DE792813B"
		},
		{
			"etask.entity": "sc018233",
			"id": "5BD74465-DE3E-96D9-DF61-53B3553BF2FE"
		},
		{
			"etask.entity": "sc018234",
			"id": "3CCD521B-B55E-13BB-1104-C93313DE3368"
		},
		{
			"etask.entity": "sc018235",
			"id": "FE98DFA4-EE44-B721-34AC-50FD5DB5D7CA"
		},
		{
			"etask.entity": "sc018236",
			"id": "4885A1CA-5A5F-AB1A-C86E-526A52FE2CD6"
		},
		{
			"etask.entity": "sc018238",
			"id": "71C27E83-73E4-DDB4-A3D7-8A9743F2373D"
		},
		{
			"etask.entity": "sc018242",
			"id": "8B809853-7A94-462B-722E-F910F1DF39B7"
		},
		{
			"etask.entity": "sc018243",
			"id": "57ACC599-2D80-074E-F0DA-78BC5E0E7555"
		},
		{
			"etask.entity": "sc015100",
			"id": "D6C909AC-E5D2-D1F1-F138-2882F3E02E5D"
		},
		{
			"etask.entity": "sc015102",
			"id": "56949B9E-5350-6D00-1819-10D8AACA9178"
		},
		{
			"etask.entity": "sc015107",
			"id": "2A8A49D1-7585-491A-6722-B997B4A56FF8"
		},
		{
			"etask.entity": "sc015112",
			"id": "9D0CFFA1-7829-CF1C-73EC-EE8DDC8ACB0E"
		},
		{
			"etask.entity": "sc015117",
			"id": "6EED65B9-2588-3119-BF30-61754DC649AF"
		},
		{
			"etask.entity": "sc015122",
			"id": "3237001E-8683-C47C-D164-CA4444679BBD"
		},
		{
			"etask.entity": "sc015124",
			"id": "4FA32426-145E-CE26-37E4-8CD47464E168"
		},
		{
			"etask.entity": "sc015129",
			"id": "10440D95-CB8B-BE0C-38C3-1196801AAA2F"
		},
		{
			"etask.entity": "sc015134",
			"id": "22D9FABB-F3F1-C661-63C8-E4C5E0C0F26D"
		},
		{
			"etask.entity": "sc015139",
			"id": "01795600-4BF7-1D7E-04C4-5FF3DE97C0EB"
		},
		{
			"etask.entity": "sc015144",
			"id": "7D0F3C11-D6BC-2A03-0144-1ACC540906CE"
		},
		{
			"etask.entity": "sc015146",
			"id": "79C7EABA-3573-CBF7-4CE8-6642BA7385C6"
		},
		{
			"etask.entity": "sc015151",
			"id": "6A2CBAF9-4942-1A89-4004-94F74E6A3DCB"
		},
		{
			"etask.entity": "sc015156",
			"id": "120D127F-9975-A35C-1A87-BBA4D5720585"
		},
		{
			"etask.entity": "sc015161",
			"id": "EB65DEF8-AF88-4B35-C268-BC2BB75A76E3"
		},
		{
			"etask.entity": "sc015166",
			"id": "1506E0A5-32E2-6011-2B48-84D27A9382A5"
		},
		{
			"etask.entity": "sc015168",
			"id": "1D8E42F5-F591-8862-2E3B-F3E7DB5EA68A"
		},
		{
			"etask.entity": "sc015173",
			"id": "73C63C1B-1973-4BDC-CAF0-27D8AD6E87BB"
		},
		{
			"etask.entity": "sc023674",
			"id": "09316913-0225-85C3-4E67-0B65851E943E"
		},
		{
			"etask.entity": "sc023675",
			"id": "F53BE625-0530-D156-9B16-9A642B1BCE8F"
		},
		{
			"etask.entity": "sc023676",
			"id": "55CC6EAC-9F7F-6F76-0BC1-48534CD96FA7"
		},
		{
			"etask.entity": "sc018245",
			"id": "3A649697-2B96-03BB-000C-9B7026157F21"
		},
		{
			"etask.entity": "sc018246",
			"id": "190A99BA-4B0A-C2E0-B22E-1A97B6D0BA17"
		},
		{
			"etask.entity": "sc018247",
			"id": "C01033ED-BA4D-9D4F-CCE2-04D59D7B95FA"
		},
		{
			"etask.entity": "sc018248",
			"id": "99BA1A7A-4636-86F4-5FE9-4730B0D7370A"
		},
		{
			"etask.entity": "sc018250",
			"id": "FD8B7B52-CF95-1542-E988-CBE0C57D6215"
		},
		{
			"etask.entity": "sc018251",
			"id": "0BFE6359-B87C-C375-F68D-C51A08C771FD"
		},
		{
			"etask.entity": "sc018252",
			"id": "4385642C-8221-671D-F702-F56962E3A961"
		},
		{
			"etask.entity": "sc018253",
			"id": "B5BD210A-1A96-0518-BDCE-050E4C150B3C"
		},
		{
			"etask.entity": "sc018255",
			"id": "337AEDC3-A0BA-0D4A-3E56-B1F24204C8DF"
		},
		{
			"etask.entity": "sc018256",
			"id": "71CE3BED-45A3-BC8A-71C9-B7887AF24CA9"
		},
		{
			"etask.entity": "sc018257",
			"id": "EB3832B0-B802-495A-379D-9013E293EA04"
		},
		{
			"etask.entity": "sc018258",
			"id": "92272C2F-DA37-A12B-0D38-070537C8D162"
		},
		{
			"etask.entity": "sc018260",
			"id": "340A3EDB-B6BD-D33F-0EBB-A59633B8E878"
		},
		{
			"etask.entity": "sc018261",
			"id": "8FAC23C7-B704-90AB-E212-8C6836C936D7"
		},
		{
			"etask.entity": "sc018262",
			"id": "488A89CC-3A95-2108-25CC-00C2310AB1DF"
		},
		{
			"etask.entity": "sc018263",
			"id": "157042AB-F0B8-3968-AEBF-5218DE550E06"
		},
		{
			"etask.entity": "sc023677",
			"id": "39DAD6B1-6ECC-6027-8D62-B6D10ECACF55"
		},
		{
			"etask.entity": "sc018269",
			"id": "7ED4B5E6-64DE-DA90-7AE1-82960355BB02"
		},
		{
			"etask.entity": "sc018270",
			"id": "2E1AEF97-1895-1E79-EAE3-7BE7947E23A8"
		},
		{
			"etask.entity": "sc018271",
			"id": "48AFC914-8E27-0483-10FC-456CDE630FF1"
		},
		{
			"etask.entity": "sc018272",
			"id": "983E0DD3-D3F6-90B9-1E04-6A712A69DC34"
		},
		{
			"etask.entity": "sc018273",
			"id": "3A0B3ADE-72FC-D711-7AEA-43537B13B817"
		},
		{
			"etask.entity": "sc018274",
			"id": "FB6C6971-C4C3-1A4F-3DBB-7775FC4D4C30"
		},
		{
			"etask.entity": "sc018275",
			"id": "A337DFED-C331-A0DD-D9E1-EADA32343048"
		},
		{
			"etask.entity": "sc018276",
			"id": "B26649C3-257C-31D8-68D1-0BA1F5D41809"
		},
		{
			"etask.entity": "sc018277",
			"id": "B4546327-DA4E-4DA2-89B5-5D1015DD04E6"
		},
		{
			"etask.entity": "sc018278",
			"id": "39592B1A-C8D0-B5D2-D2AE-D4D7F2664608"
		},
		{
			"etask.entity": "sc018279",
			"id": "AFC3F8D6-644C-70C4-A59E-1C2F3D524532"
		},
		{
			"etask.entity": "sc018280",
			"id": "822E719D-DC7E-F668-DE1E-A95B1A116570"
		},
		{
			"etask.entity": "sc018282",
			"id": "12E50ACF-1348-9BF2-3920-04EDB8A9BD3A"
		},
		{
			"etask.entity": "sc018283",
			"id": "5CF82A61-2543-910A-4683-C313D5715944"
		},
		{
			"etask.entity": "sc018284",
			"id": "1F0D85C0-6D95-8521-455A-2B6CCCDCCABC"
		},
		{
			"etask.entity": "sc018285",
			"id": "ECBC08D2-F4C5-D5C9-F6F3-204BB14F2B9B"
		},
		{
			"etask.entity": "sc018287",
			"id": "8686DFFB-0C72-41B8-29A6-8CDC0CF90DA5"
		},
		{
			"etask.entity": "sc023678",
			"id": "CB7ABD1F-9E89-BBED-5115-8CAD4472B5C0"
		},
		{
			"etask.entity": "sc023679",
			"id": "2F5D54F6-1C55-AAA1-5661-F1C75ED91D3A"
		},
		{
			"etask.entity": "sc023680",
			"id": "B828DF79-5947-BF13-F509-852BC35DB7C6"
		},
		{
			"etask.entity": "sc023681",
			"id": "BA108B6B-C159-864E-3940-C5D5398B259F"
		},
		{
			"etask.entity": "sc023682",
			"id": "EACB2B92-F4B2-CAA6-B0A1-307A75770B7B"
		},
		{
			"etask.entity": "sc023683",
			"id": "3A28DFDA-4A7A-DC39-7D62-7AF973661407"
		},
		{
			"etask.entity": "sc023684",
			"id": "EE641255-ED51-EB8F-E18A-7D14F8CB4337"
		},
		{
			"etask.entity": "sc023685",
			"id": "A2CC9F6B-D38E-BFE7-A7E7-FE9F5B079423"
		},
		{
			"etask.entity": "sc023686",
			"id": "88077083-D43E-322C-ADB6-06AB3FB140BC"
		},
		{
			"etask.entity": "sc023687",
			"id": "3CFC3B9C-4965-07AF-6FBB-E27A11490504"
		},
		{
			"etask.entity": "sc023688",
			"id": "360CCD5C-02ED-7D9F-4DF0-E7650ADC497E"
		},
		{
			"etask.entity": "sc023689",
			"id": "DE2B9057-E246-8071-E11A-6A4CDB795888"
		},
		{
			"etask.entity": "sc023690",
			"id": "28FF8D46-1EEF-9334-7D4D-B95F16C826D3"
		},
		{
			"etask.entity": "sc018289",
			"id": "F57C43ED-EC21-0635-6E04-4840645A1468"
		},
		{
			"etask.entity": "sc018290",
			"id": "82D4E469-BB5F-3EE6-4F96-3304741E367A"
		},
		{
			"etask.entity": "sc018291",
			"id": "F4665F50-4AE9-336C-27E1-CC1772498DC5"
		},
		{
			"etask.entity": "sc018292",
			"id": "854BF6CF-38BC-7796-DD42-09D766A62991"
		},
		{
			"etask.entity": "sc018294",
			"id": "35C2CFFB-007D-25D4-7A36-A0F0252444F9"
		},
		{
			"etask.entity": "sc018299",
			"id": "75713FB2-0222-AFFA-C5F8-30747EE1E917"
		},
		{
			"etask.entity": "sc018300",
			"id": "F6B29850-7804-6393-23FE-97E9FB5A153A"
		},
		{
			"etask.entity": "sc018301",
			"id": "965BE51F-6346-DF72-9546-32AE6301FE94"
		},
		{
			"etask.entity": "sc015178",
			"id": "A77CCC87-B3F7-A0D0-B797-B4973D8F2F94"
		},
		{
			"etask.entity": "sc015183",
			"id": "0EA1BC21-5768-56E7-9172-E5405600ECB4"
		},
		{
			"etask.entity": "sc015188",
			"id": "BDB3308F-3BD5-94E2-385C-AEF1F778F3F9"
		},
		{
			"etask.entity": "sc015190",
			"id": "344B3481-3EE5-1843-50EC-FE140D09CBB1"
		},
		{
			"etask.entity": "sc015195",
			"id": "47F21374-9F56-5ED7-7DB0-E219FC7093AB"
		},
		{
			"etask.entity": "sc015200",
			"id": "4D43B606-76A4-5B11-0300-AFF6BDE1A82B"
		},
		{
			"etask.entity": "sc015205",
			"id": "D414478F-9E69-B9E7-F470-E16B73BA04C5"
		},
		{
			"etask.entity": "sc015210",
			"id": "28ACE4A7-19C6-96E3-18BF-D57AD0E92EC7"
		},
		{
			"etask.entity": "sc015212",
			"id": "92E2ED84-8174-ED85-A743-1673986033A7"
		},
		{
			"etask.entity": "sc015217",
			"id": "C208A898-981F-4284-5E8C-0D375D4CA1D0"
		},
		{
			"etask.entity": "sc015222",
			"id": "05E3CA07-410B-41BD-496B-5E4BC4058AC1"
		},
		{
			"etask.entity": "sc015227",
			"id": "7AC885A0-54FE-FAA0-E2F3-4F26CC3F5FDF"
		},
		{
			"etask.entity": "sc015232",
			"id": "C6B31986-B557-D0DF-6973-18FAB8A7B935"
		},
		{
			"etask.entity": "sc015234",
			"id": "E51E8753-865D-4C2D-A90B-35F12BF320BD"
		},
		{
			"etask.entity": "sc015239",
			"id": "1ADD04CA-9FF3-080E-DBEE-7027A8B00057"
		},
		{
			"etask.entity": "sc015244",
			"id": "8CE138B8-1D43-D9C2-986C-5EDED624FD19"
		},
		{
			"etask.entity": "sc015249",
			"id": "0D5098E9-FDE2-B0BD-EF11-F31332C68EE7"
		},
		{
			"etask.entity": "sc015254",
			"id": "B5B951BB-18DC-C0E5-35B9-87F340F1FD28"
		},
		{
			"etask.entity": "sc023691",
			"id": "B64F8F81-474E-619D-6382-922C81C280E9"
		},
		{
			"etask.entity": "sc023692",
			"id": "C4C31A04-E66A-6789-8420-314B060B8C94"
		},
		{
			"etask.entity": "sc023693",
			"id": "61EBED10-62C9-F188-9BC4-B446BE418FDB"
		},
		{
			"etask.entity": "sc018313",
			"id": "C67708EB-1BAD-E879-E682-0833CBB870A6"
		},
		{
			"etask.entity": "sc018314",
			"id": "91758B44-9AAF-927A-E398-353BFC08391E"
		},
		{
			"etask.entity": "sc018315",
			"id": "7AA81EEE-F6E5-411F-2057-7502AE1C2A9D"
		},
		{
			"etask.entity": "sc018316",
			"id": "985CBB62-8E74-0F11-45AE-3884A0709D38"
		},
		{
			"etask.entity": "sc018317",
			"id": "EA893DF3-07EB-C94E-BEF8-D5F86A7D9247"
		},
		{
			"etask.entity": "sc018318",
			"id": "8A1C0D42-906F-ABB6-D37F-09AFB2F6E4B4"
		},
		{
			"etask.entity": "sc018319",
			"id": "EEAAE06F-12E9-3F86-0967-A72D084771F5"
		},
		{
			"etask.entity": "sc018320",
			"id": "E24E8D4B-2D43-1392-A21C-01BD34FDFF86"
		},
		{
			"etask.entity": "sc018324",
			"id": "5B23F717-46A3-C1F7-E041-6B03B88704D1"
		},
		{
			"etask.entity": "sc018325",
			"id": "D5487A7D-4AEE-2763-72E2-30678821C15E"
		},
		{
			"etask.entity": "sc018326",
			"id": "185A6B27-F857-7B4C-85E2-2F7BF7F614D9"
		},
		{
			"etask.entity": "sc018327",
			"id": "692C84C5-15F5-77B7-B6BE-8846F32AF618"
		},
		{
			"etask.entity": "sc018328",
			"id": "B35C3519-0445-8233-067E-2839CB3BD33C"
		},
		{
			"etask.entity": "sc018329",
			"id": "869792C9-F41E-9F03-176A-F0DC9B6FE168"
		},
		{
			"etask.entity": "sc018330",
			"id": "B017AC74-D836-E669-B208-6647957A9187"
		},
		{
			"etask.entity": "sc018331",
			"id": "AF40F39C-CAE5-9FEF-CC0E-F2CCA7C2B5AF"
		},
		{
			"etask.entity": "sc023694",
			"id": "A293F26E-FFB4-0311-FB18-E170E84AC6E7"
		},
		{
			"etask.entity": "sc023695",
			"id": "BB804FD7-282A-451F-46F9-73CA2DA59A61"
		},
		{
			"etask.entity": "sc023696",
			"id": "86D92591-0FFA-85A0-69A1-775A6C0EA346"
		},
		{
			"etask.entity": "sc023697",
			"id": "7C5B2EAF-AFF1-3885-43E0-378E64C7F464"
		},
		{
			"etask.entity": "sc018333",
			"id": "0311D3F2-7527-58BA-DE0F-BC04B01EEEB8"
		},
		{
			"etask.entity": "sc018334",
			"id": "7047106B-0AD5-222B-8FC0-543A74D698C4"
		},
		{
			"etask.entity": "sc018335",
			"id": "65391D11-9579-D921-405D-FA2997EC71C8"
		},
		{
			"etask.entity": "sc018336",
			"id": "BC310A47-99CF-7971-643F-B7C01455745C"
		},
		{
			"etask.entity": "sc018338",
			"id": "11E6DD1B-E42B-53D3-59BC-CE89228AE3EE"
		},
		{
			"etask.entity": "sc018339",
			"id": "99449AC7-4395-DF3E-5736-BF20A0FFAA1C"
		},
		{
			"etask.entity": "sc018340",
			"id": "10DC7027-A81B-FF34-B9B9-B6A22AEAB791"
		},
		{
			"etask.entity": "sc018341",
			"id": "24418786-2AC9-FF8E-DBC2-927E8AE21340"
		},
		{
			"etask.entity": "sc018343",
			"id": "9209F7D9-FBD8-8D44-5E7D-8C7B42721DB0"
		},
		{
			"etask.entity": "sc018344",
			"id": "06E337A6-0A32-C173-CF53-94FAEFB5DA54"
		},
		{
			"etask.entity": "sc018345",
			"id": "8A22BF2E-805D-974D-DABE-4C9D557E1651"
		},
		{
			"etask.entity": "sc018346",
			"id": "BCFE37D1-F16E-FF5E-5D46-4C911B80A09B"
		},
		{
			"etask.entity": "sc018351",
			"id": "A9CD4E0B-7A32-3376-CAD6-2EC636420D1B"
		},
		{
			"etask.entity": "sc018352",
			"id": "85FF9B61-A158-063F-AE24-10C57117948E"
		},
		{
			"etask.entity": "sc018353",
			"id": "D4FE85B5-9A02-D479-AA2A-3786CE35AED3"
		},
		{
			"etask.entity": "sc023698",
			"id": "B9C72E23-C770-9303-2B0B-170840C699EB"
		},
		{
			"etask.entity": "sc023699",
			"id": "62FD0BF4-B91D-BC45-926C-9A0C4D55A460"
		},
		{
			"etask.entity": "sc023700",
			"id": "2EF7DA7C-64DA-42C3-7215-E231D8DB57AD"
		},
		{
			"etask.entity": "sc018355",
			"id": "B484051F-4AB6-60F1-B413-4AA827F9BA1D"
		},
		{
			"etask.entity": "sc018356",
			"id": "294B53A4-0FB3-C5C7-830C-F87E018F4502"
		},
		{
			"etask.entity": "sc018357",
			"id": "42A38283-6A41-5B92-A1D8-E6417BA8750F"
		},
		{
			"etask.entity": "sc018358",
			"id": "39DD56CA-0BB0-AD5E-4849-CF695BA8FAF5"
		},
		{
			"etask.entity": "sc018360",
			"id": "94A3B4DB-DC95-353F-8BC0-2C59090222DE"
		},
		{
			"etask.entity": "sc018361",
			"id": "E344D383-C1EA-1C2C-5A0E-6264427A18A3"
		},
		{
			"etask.entity": "sc018362",
			"id": "00934DEB-EC7B-B80D-5F33-0B8634371DA4"
		},
		{
			"etask.entity": "sc018363",
			"id": "EAEF8014-B3F9-30E3-7120-DB690283A9AF"
		},
		{
			"etask.entity": "sc018365",
			"id": "DD6DA81A-C1BE-D7AE-8827-6F5060A1603F"
		},
		{
			"etask.entity": "sc018366",
			"id": "2997EDE9-62A0-B1E9-37BC-5958485928FB"
		},
		{
			"etask.entity": "sc018367",
			"id": "58C89160-FC66-5A8B-133C-B54FF7158919"
		},
		{
			"etask.entity": "sc018368",
			"id": "80F5A431-14E1-3C6D-BA3F-4565AFB4B47D"
		},
		{
			"etask.entity": "sc018370",
			"id": "FEC1637D-ECEF-56FF-B854-1DC5C76B4760"
		},
		{
			"etask.entity": "sc018371",
			"id": "4C3716A9-50CB-13CA-7201-81DC7D195E8E"
		},
		{
			"etask.entity": "sc018372",
			"id": "5C525C77-6323-3C86-D5D7-26BA051C0E0B"
		},
		{
			"etask.entity": "sc018373",
			"id": "F68B9B0B-AE7C-F436-51EE-3337C2002848"
		},
		{
			"etask.entity": "sc023701",
			"id": "ED130EE7-A2D5-DB7B-12ED-E2C3266B792D"
		},
		{
			"etask.entity": "sc018378",
			"id": "AEBEECCE-8026-E68F-246F-2B1C5F5CF5B2"
		},
		{
			"etask.entity": "sc018379",
			"id": "3463F73D-618A-BB91-FC08-272929B46739"
		},
		{
			"etask.entity": "sc018380",
			"id": "DC39CA75-6BB3-24B6-2781-3192B926AFF6"
		},
		{
			"etask.entity": "sc018381",
			"id": "5C8A62F3-B346-51F1-774D-375737FB0961"
		},
		{
			"etask.entity": "sc018382",
			"id": "D5B2B86E-8C94-4680-4178-08E49CC0716E"
		},
		{
			"etask.entity": "sc018383",
			"id": "023B00C7-F97F-2F57-3AAC-3CB2377F95D2"
		},
		{
			"etask.entity": "sc018384",
			"id": "AD99C7C4-E3C9-27A6-58B7-3248951180AB"
		},
		{
			"etask.entity": "sc018385",
			"id": "4E27451A-4856-55A7-FF8B-E73F0BB57202"
		},
		{
			"etask.entity": "sc018387",
			"id": "81C5C6B9-71E5-E9A7-47E0-78A37A171C8F"
		},
		{
			"etask.entity": "sc018388",
			"id": "8D9BFA46-69BD-220F-DB47-101FCA3F9853"
		},
		{
			"etask.entity": "sc018389",
			"id": "7939F2BC-42E3-C994-6A91-84C5912F87C0"
		},
		{
			"etask.entity": "sc018390",
			"id": "D62B4771-2B97-44CF-FDD6-27AE31266E6B"
		},
		{
			"etask.entity": "sc018392",
			"id": "0006B21D-3B05-31E8-78D3-C283EA7FCC63"
		},
		{
			"etask.entity": "sc018393",
			"id": "B182D450-513E-9E44-FD93-D947AB49C5E1"
		},
		{
			"etask.entity": "sc018394",
			"id": "F4B0CD03-3CE7-C75F-21B7-AD44463385E2"
		},
		{
			"etask.entity": "sc018395",
			"id": "28BF3772-8B36-660A-F2D9-D0B29A22766D"
		},
		{
			"etask.entity": "sc018397",
			"id": "A6FC8DB7-7A30-D161-4232-CB940FCF10E1"
		},
		{
			"etask.entity": "sc015256",
			"id": "69277040-1DB8-5269-AC0A-F5955803F313"
		},
		{
			"etask.entity": "sc015261",
			"id": "3B031878-3677-E25A-0584-14CDC8684772"
		},
		{
			"etask.entity": "sc015266",
			"id": "0158CCC4-22B8-4CA5-FEFA-763F1DDDA5CA"
		},
		{
			"etask.entity": "sc015271",
			"id": "5436AE65-79AD-E38C-ED69-8003F38896CB"
		},
		{
			"etask.entity": "sc015276",
			"id": "DDEECBCD-5F7C-97FE-D508-D9D8265D484E"
		},
		{
			"etask.entity": "sc015278",
			"id": "D5217B48-DA2D-DF93-DC1C-92738AA2E989"
		},
		{
			"etask.entity": "sc015283",
			"id": "E1C0B78D-40A4-1D69-4413-35A25027FE72"
		},
		{
			"etask.entity": "sc015288",
			"id": "2951B511-72EB-AECD-45A7-ED3AD4F364BA"
		},
		{
			"etask.entity": "sc015293",
			"id": "860D486D-404E-9825-0F27-3EF44137C336"
		},
		{
			"etask.entity": "sc015298",
			"id": "1EBEED0A-DF75-8493-3EC9-298D9A3BDFFA"
		},
		{
			"etask.entity": "sc015300",
			"id": "D897063F-0F0C-4194-813A-852C7D15E645"
		},
		{
			"etask.entity": "sc015305",
			"id": "82B27FA9-067F-EC8B-FA0E-820513DFF172"
		},
		{
			"etask.entity": "sc015310",
			"id": "F2D319C1-F926-D49A-EB3C-83BE48B95B56"
		},
		{
			"etask.entity": "sc015315",
			"id": "9F284CFF-1AE7-49BD-F96F-53C386583D22"
		},
		{
			"etask.entity": "sc015320",
			"id": "3A0FCEB4-41C1-1CE8-C6C7-49C3801711C7"
		},
		{
			"etask.entity": "sc015322",
			"id": "BFB8A217-3FC9-6A40-FB3D-EA364E100108"
		},
		{
			"etask.entity": "sc015327",
			"id": "339BC9E2-CCB7-824C-DDF2-A0858F18CACF"
		},
		{
			"etask.entity": "sc015332",
			"id": "EA9F49A6-9527-4860-DA85-0EDA53A0F548"
		},
		{
			"etask.entity": "sc023702",
			"id": "DCA52B53-C621-8B7C-1C49-AFD17C061442"
		},
		{
			"etask.entity": "sc018399",
			"id": "5A249F80-109C-DFA3-2C97-1F9BD9C364D4"
		},
		{
			"etask.entity": "sc018400",
			"id": "B9215C2B-BD89-5EAF-C67F-0624794A0B53"
		},
		{
			"etask.entity": "sc018401",
			"id": "D56BEA3B-862F-FDE6-EA92-2D2A2985C17F"
		},
		{
			"etask.entity": "sc018402",
			"id": "6F8B860B-14E7-7659-6061-D2F71DEBF324"
		},
		{
			"etask.entity": "sc018404",
			"id": "B91A990C-DB0B-C724-AD85-C54D2C87FD3E"
		},
		{
			"etask.entity": "sc018405",
			"id": "AAA616E0-AF7E-023C-475E-0196B0489701"
		},
		{
			"etask.entity": "sc018406",
			"id": "E910E912-2153-05C5-D60E-7D3C5D6EBA27"
		},
		{
			"etask.entity": "sc018407",
			"id": "1CAD25FB-9F25-BC62-2126-FDA46422B6E0"
		},
		{
			"etask.entity": "sc018409",
			"id": "B56668CC-0AB4-8840-016A-6A8874A80BA4"
		},
		{
			"etask.entity": "sc018410",
			"id": "825600A1-CE54-F4B2-369E-F1FA47D1FBCD"
		},
		{
			"etask.entity": "sc018411",
			"id": "0BB0F0F3-A5F5-F43D-2924-5CE0D718CAD7"
		},
		{
			"etask.entity": "sc018412",
			"id": "80D95A2E-D9A4-0A5E-3DC0-2B0095132616"
		},
		{
			"etask.entity": "sc018414",
			"id": "8B1A5D63-55E4-676B-3B52-335A16E34F88"
		},
		{
			"etask.entity": "sc018415",
			"id": "D07C8960-4D5F-FFA6-4101-F89D2C0901E5"
		},
		{
			"etask.entity": "sc018416",
			"id": "25AE32EC-35AE-684B-AA96-20AC7B7E8B89"
		},
		{
			"etask.entity": "sc018417",
			"id": "DA48524F-862F-AF5F-61BA-6CA94B50C4A2"
		},
		{
			"etask.entity": "sc018419",
			"id": "DD497BB5-5BCA-B62C-78F0-637791B93EA9"
		},
		{
			"etask.entity": "sc023703",
			"id": "1CCFB4F1-0CE5-7541-9594-74D3836E2D5B"
		},
		{
			"etask.entity": "sc018421",
			"id": "66457B64-8104-F3EB-5B55-236BE783FF0B"
		},
		{
			"etask.entity": "sc018422",
			"id": "BABACF5A-0C22-276C-910C-F1C7267E5880"
		},
		{
			"etask.entity": "sc018423",
			"id": "B0F26FB7-D78E-F94A-CC41-E0C37A2565C4"
		},
		{
			"etask.entity": "sc018424",
			"id": "6BF671BA-74DA-DF14-8CAC-E3C466D8B737"
		},
		{
			"etask.entity": "sc018426",
			"id": "3B80D5FD-1A0E-7249-E57E-A7C00D5D0391"
		},
		{
			"etask.entity": "sc018427",
			"id": "3BFE6685-5EFA-BDDC-1B27-7E7F816DCC83"
		},
		{
			"etask.entity": "sc018428",
			"id": "FE9E9DA1-0246-D739-E95D-FD3F31FCF35A"
		},
		{
			"etask.entity": "sc018429",
			"id": "8DF81ADE-54E4-67A7-A1C0-1665927AFDDF"
		},
		{
			"etask.entity": "sc018431",
			"id": "40B25BFE-A125-AC13-1724-ABEDE343524E"
		},
		{
			"etask.entity": "sc018432",
			"id": "7C0A48B9-C29F-3557-EF2F-E06720CC21E3"
		},
		{
			"etask.entity": "sc018433",
			"id": "8397C60E-BE7F-E812-6F51-5E71859FA544"
		},
		{
			"etask.entity": "sc018434",
			"id": "87B4684F-742F-4C0D-0FCD-F886FABED868"
		},
		{
			"etask.entity": "sc018436",
			"id": "1BECF4D8-60CD-5416-C63A-A0067D46FAC1"
		},
		{
			"etask.entity": "sc018437",
			"id": "9B93EFEF-FA1C-B427-4C74-3BC3E3F81507"
		},
		{
			"etask.entity": "sc018438",
			"id": "051A3A04-EB0B-2A84-8139-EAAB39DD5ADB"
		},
		{
			"etask.entity": "sc018439",
			"id": "34B4E861-9828-E231-8D17-715ABED86A95"
		},
		{
			"etask.entity": "sc018441",
			"id": "CDCDCE6A-1A56-B344-352D-541457A4CE87"
		},
		{
			"etask.entity": "sc023704",
			"id": "EA0C3B15-0171-06F5-C25C-54DE352FE907"
		},
		{
			"etask.entity": "sc018443",
			"id": "1E90E220-9CC6-ADCE-3683-1DC9AE625597"
		},
		{
			"etask.entity": "sc018444",
			"id": "BE75626E-ED73-9B5F-946C-21C2A0FA4A84"
		},
		{
			"etask.entity": "sc018445",
			"id": "6A5870FD-8CA6-E98F-60D8-02689B80033F"
		},
		{
			"etask.entity": "sc018446",
			"id": "2BF88978-3432-C5EE-4D9C-3F601FB34AA1"
		},
		{
			"etask.entity": "sc018448",
			"id": "38BD2EA5-595F-9C90-0E97-97C42CDEA750"
		},
		{
			"etask.entity": "sc018449",
			"id": "FAA2F9FC-A2D1-265B-46B5-B1A6B8B222C8"
		},
		{
			"etask.entity": "sc018450",
			"id": "163B8CA2-AD3F-C3D7-27A4-9A960576BC6F"
		},
		{
			"etask.entity": "sc018451",
			"id": "2825646D-69ED-9C3B-5915-2C7FF3B0EEE5"
		},
		{
			"etask.entity": "sc018453",
			"id": "D7EA3B37-A11D-CB44-E1E0-06223659D99E"
		},
		{
			"etask.entity": "sc018454",
			"id": "D5C827F4-14E1-084F-10E0-518D28BFA865"
		},
		{
			"etask.entity": "sc018455",
			"id": "F7B200BB-D33C-B81A-B2BF-1C9A6E8E9B92"
		},
		{
			"etask.entity": "sc018456",
			"id": "17B87CE3-1B11-5322-903B-1EB2AC4D0AC8"
		},
		{
			"etask.entity": "sc018458",
			"id": "99492DF1-C718-FDE6-365C-C6A7C0C89820"
		},
		{
			"etask.entity": "sc018459",
			"id": "9CBC99B5-7F96-52FC-5929-2825348F1BA9"
		},
		{
			"etask.entity": "sc018460",
			"id": "8191EEEB-E500-D7B6-178B-6B0A4B478CBE"
		},
		{
			"etask.entity": "sc018461",
			"id": "BE15790C-4BA7-9299-3925-4B5233AE3FD0"
		},
		{
			"etask.entity": "sc018463",
			"id": "44C79FF0-8A15-D4FE-69FC-81ACE18FD45D"
		},
		{
			"etask.entity": "sc015337",
			"id": "6E2ADE8C-D93D-75F0-8030-D98E8234FE52"
		},
		{
			"etask.entity": "sc015342",
			"id": "2FFD09F8-C127-DB09-56E4-4283F476EBE2"
		},
		{
			"etask.entity": "sc015344",
			"id": "520C02F0-AEB6-2DDF-E06A-684F1703DCB0"
		},
		{
			"etask.entity": "sc015349",
			"id": "C5980C84-9CAC-48F5-9E06-F65232D2C41A"
		},
		{
			"etask.entity": "sc015354",
			"id": "0A54E4D4-C51F-A04F-5658-BD44EBA024C2"
		},
		{
			"etask.entity": "sc015359",
			"id": "EAD57418-17B6-7777-C317-D4147E0D355B"
		},
		{
			"etask.entity": "sc015364",
			"id": "D4A5F761-C4FA-B725-3D86-41ABBD0CA999"
		},
		{
			"etask.entity": "sc015366",
			"id": "0EDD2604-AB19-6BAD-FE1A-C7D42F257B2A"
		},
		{
			"etask.entity": "sc015371",
			"id": "797675AD-6F4D-65D0-BB74-CD9679D9BEA9"
		},
		{
			"etask.entity": "sc015376",
			"id": "2CFFA9B2-E821-C4D1-C79D-B42D23048A33"
		},
		{
			"etask.entity": "sc015381",
			"id": "8C3F90AC-7487-6163-4B2F-676ACDF547B2"
		},
		{
			"etask.entity": "sc015386",
			"id": "D2C87A55-A909-B428-E7A7-614EED0FC8B0"
		},
		{
			"etask.entity": "sc015388",
			"id": "224F58BA-2EE2-3306-2AA0-091C23D3216F"
		},
		{
			"etask.entity": "sc015393",
			"id": "79000CBA-E18F-929E-7E55-B4CC450BBF3A"
		},
		{
			"etask.entity": "sc015398",
			"id": "5322CE8B-F378-51A1-4312-817F3540E01A"
		},
		{
			"etask.entity": "sc015403",
			"id": "DFC74F11-E7BE-BA8B-46CC-7A4838484ECB"
		},
		{
			"etask.entity": "sc015408",
			"id": "B7C3F6A2-49A2-B017-B7C2-938292042B36"
		},
		{
			"etask.entity": "sc015410",
			"id": "5794933E-63F0-D1D1-A11B-D605CE642A5C"
		},
		{
			"etask.entity": "sc023705",
			"id": "ED87D610-AB9F-68C4-824F-3B48DB52CDF1"
		},
		{
			"etask.entity": "sc018465",
			"id": "0B23C386-FD7B-383B-A713-EE867C8B7CDD"
		},
		{
			"etask.entity": "sc018466",
			"id": "6A46015D-666B-CB77-9D1E-6A458B29D499"
		},
		{
			"etask.entity": "sc018467",
			"id": "B0F66693-6E06-D69F-6B68-4BEAAA91A479"
		},
		{
			"etask.entity": "sc018468",
			"id": "70E13FB0-C2A0-CF2F-34E3-7DB2EEE69B4B"
		},
		{
			"etask.entity": "sc018470",
			"id": "D1D6FF86-3098-340F-72FC-8B8DF0BFC62D"
		},
		{
			"etask.entity": "sc018471",
			"id": "45EFF7E4-D14C-02E7-628E-623319CCCBDD"
		},
		{
			"etask.entity": "sc018472",
			"id": "D273E02A-88E8-C8AB-8385-1A4192451D9E"
		},
		{
			"etask.entity": "sc018473",
			"id": "21B6F757-A14A-D56F-8DEC-510A3A5182B5"
		},
		{
			"etask.entity": "sc018475",
			"id": "749C8622-BD91-8FCF-7625-3F9DFE6F323B"
		},
		{
			"etask.entity": "sc018476",
			"id": "C06E3B31-BE10-37E3-3073-8EAFD8757BEA"
		},
		{
			"etask.entity": "sc018477",
			"id": "10BA1065-055B-0E3B-7A6A-457AE823B79F"
		},
		{
			"etask.entity": "sc018478",
			"id": "726DA3CE-4EAC-2938-3D6F-9496F8D7A219"
		},
		{
			"etask.entity": "sc018480",
			"id": "F1DD5098-233C-139A-BC55-B989651A1D5A"
		},
		{
			"etask.entity": "sc018481",
			"id": "789D2E5A-A4AA-6C27-E16B-017D0693DC87"
		},
		{
			"etask.entity": "sc018482",
			"id": "469DD804-4B51-A4DB-A8AF-15A1DDC2E931"
		},
		{
			"etask.entity": "sc018483",
			"id": "A9324356-F8C0-C2AA-A1F0-2001EE9AEAF6"
		},
		{
			"etask.entity": "sc018485",
			"id": "70395A33-3BFC-054E-7128-200F54A1CAB6"
		},
		{
			"etask.entity": "sc023706",
			"id": "E2B7CB4D-68E2-3001-0699-D937D618B04A"
		},
		{
			"etask.entity": "sc018487",
			"id": "D7C3BD4D-9995-2A39-D4BA-C1DB19FEF3C2"
		},
		{
			"etask.entity": "sc018488",
			"id": "094CAE4C-AB77-C5A1-8FAA-AB08C8508E94"
		},
		{
			"etask.entity": "sc018489",
			"id": "F225D519-1A4C-4084-438F-34DA36C6BF44"
		},
		{
			"etask.entity": "sc018490",
			"id": "3D196856-BDBB-3318-E8C3-3EF0340EE094"
		},
		{
			"etask.entity": "sc018492",
			"id": "53035C35-DB12-D22D-EA2F-654C04DF6B67"
		},
		{
			"etask.entity": "sc018493",
			"id": "89C6585D-9424-8DE8-AE35-07DFB64B6376"
		},
		{
			"etask.entity": "sc018494",
			"id": "CD045252-3653-1214-C26D-0AF7F14F0923"
		},
		{
			"etask.entity": "sc018495",
			"id": "4DDA0EBD-4277-A55E-14AF-DD88954A2C37"
		},
		{
			"etask.entity": "sc018497",
			"id": "FF947595-2287-A901-5647-46245FF5F69B"
		},
		{
			"etask.entity": "sc018498",
			"id": "BFA04F46-3B63-321A-8D1F-3228AEF9960A"
		},
		{
			"etask.entity": "sc018499",
			"id": "FE21BBD6-DCBE-5351-F67A-E2764408073C"
		},
		{
			"etask.entity": "sc018500",
			"id": "E8167021-0CE4-DB1A-E33C-A76C6C7B9A89"
		},
		{
			"etask.entity": "sc018502",
			"id": "DDE4A6E5-8F9A-F384-EFEB-B0BFFD3337DE"
		},
		{
			"etask.entity": "sc018503",
			"id": "D8F25DDC-43AF-033E-C5B7-46FC5FED4EC2"
		},
		{
			"etask.entity": "sc018504",
			"id": "4F4AD878-AAE9-FCF6-4E71-430EEB4A0641"
		},
		{
			"etask.entity": "sc018505",
			"id": "99B68118-BE0C-601C-5C12-38A29D127591"
		},
		{
			"etask.entity": "sc018507",
			"id": "FE189562-8A9A-81D3-7CBA-9970C853F46A"
		},
		{
			"etask.entity": "sc023707",
			"id": "4E7AD208-A75F-E68C-E551-6E7647216227"
		},
		{
			"etask.entity": "sc018509",
			"id": "1C9167CD-2A31-8684-7725-14544475DABB"
		},
		{
			"etask.entity": "sc018510",
			"id": "A4EA4830-44EE-61A5-BA1C-273EB5918AA1"
		},
		{
			"etask.entity": "sc018511",
			"id": "7014C2FF-B657-03E2-E0BE-09C7246F011E"
		},
		{
			"etask.entity": "sc018512",
			"id": "C028A35B-1E6A-6F37-2621-AE26C437D61F"
		},
		{
			"etask.entity": "sc018514",
			"id": "77E54AC6-FF19-938A-FAAB-2994B226E2B2"
		},
		{
			"etask.entity": "sc018515",
			"id": "0DE7F2B2-E8C3-A41A-8295-C81EBE634462"
		},
		{
			"etask.entity": "sc018516",
			"id": "879CB211-A2FD-C140-88AF-1C4DDF939F9E"
		},
		{
			"etask.entity": "sc018517",
			"id": "63CF6223-FF00-57F6-EE0E-317E9FC4EFD9"
		},
		{
			"etask.entity": "sc018519",
			"id": "C1B72A2D-7F79-8254-A9D3-A9E0EE00AFF1"
		},
		{
			"etask.entity": "sc018520",
			"id": "0803C448-843C-F643-768D-4514FC1B3DCB"
		},
		{
			"etask.entity": "sc018521",
			"id": "6109DE4E-4F36-5BDD-63BC-E9A810FFD0EA"
		},
		{
			"etask.entity": "sc018522",
			"id": "2A6DD402-A086-11C4-C042-40698527E1A4"
		},
		{
			"etask.entity": "sc018524",
			"id": "C91E4425-AC42-CC60-F6B0-55199EE7A090"
		},
		{
			"etask.entity": "sc018525",
			"id": "94A786AE-6DBB-E046-CFEC-AE149C556B87"
		},
		{
			"etask.entity": "sc018526",
			"id": "EB7788A8-2DDA-22EB-973A-0AF01D01994A"
		},
		{
			"etask.entity": "sc018527",
			"id": "6671712B-A9E6-C6BE-8179-6A4EEE1DA11B"
		},
		{
			"etask.entity": "sc018529",
			"id": "7A2D0B91-4707-5862-457E-BF306BF8309A"
		},
		{
			"etask.entity": "sc015415",
			"id": "C9676BC8-BFBB-B606-51A2-76EDF51B9584"
		},
		{
			"etask.entity": "sc015420",
			"id": "ABA460FB-6209-5935-B3B2-0B02416E4D9C"
		},
		{
			"etask.entity": "sc015425",
			"id": "D87B3919-1954-A2C7-5686-F5D9489F6D2F"
		},
		{
			"etask.entity": "sc015430",
			"id": "7B4AA1F8-1C5E-FB4F-13D5-91E898998357"
		},
		{
			"etask.entity": "sc015432",
			"id": "8E59B45F-05D2-98E2-17AC-D28B0EBD0032"
		},
		{
			"etask.entity": "sc015437",
			"id": "89846504-446D-AE89-31D4-80FFB6833786"
		},
		{
			"etask.entity": "sc015442",
			"id": "3E6E93F7-2E49-6BEA-055B-D91766A71862"
		},
		{
			"etask.entity": "sc015447",
			"id": "B0FBAEA1-1174-FC6F-9A79-F00E73AF9BFA"
		},
		{
			"etask.entity": "sc015452",
			"id": "179BBF00-AA16-3F1B-43B9-723C8AAF414F"
		},
		{
			"etask.entity": "sc015454",
			"id": "BA791C55-148A-44D5-B853-A254F5882364"
		},
		{
			"etask.entity": "sc015459",
			"id": "84B8B321-065F-5207-EF7C-8BD3C2321130"
		},
		{
			"etask.entity": "sc015464",
			"id": "CEF10CBE-123A-790A-B162-7EEA20708502"
		},
		{
			"etask.entity": "sc015469",
			"id": "CA289F79-65D7-0775-C8F0-EB26388686FE"
		},
		{
			"etask.entity": "sc015474",
			"id": "1371F118-6F2C-5EF2-556E-2B85171D116F"
		},
		{
			"etask.entity": "sc015476",
			"id": "E31B06A1-BC65-92DD-CCF2-84B937C612FB"
		},
		{
			"etask.entity": "sc015481",
			"id": "3572DA7C-6568-5A0E-311A-0E2FA8255A33"
		},
		{
			"etask.entity": "sc015486",
			"id": "BE1C6071-4E30-F00E-C700-FCF0C317B55C"
		},
		{
			"etask.entity": "sc015491",
			"id": "A55630B7-0FF2-5119-1484-4344075F0E08"
		},
		{
			"etask.entity": "sc023708",
			"id": "D01FC035-A80D-E326-86CD-96E84CB943B9"
		},
		{
			"etask.entity": "sc018531",
			"id": "D59A3FDA-66DD-EEFA-199B-83318DCD7E17"
		},
		{
			"etask.entity": "sc018532",
			"id": "44A7B73B-3F82-6055-A267-DAE3541E0355"
		},
		{
			"etask.entity": "sc018533",
			"id": "F068699F-3E2D-DF35-88B6-04555BAA4954"
		},
		{
			"etask.entity": "sc018534",
			"id": "F4110421-9568-CD95-C336-7EF7D7B4BDE2"
		},
		{
			"etask.entity": "sc018536",
			"id": "4DABF7AB-76BC-CED7-4113-8DB354C09C15"
		},
		{
			"etask.entity": "sc018537",
			"id": "D197C79C-7D6B-F4A4-FEDB-E0D3AA3AB892"
		},
		{
			"etask.entity": "sc018538",
			"id": "5ED03278-2A74-A77A-4784-9FA2A9764C66"
		},
		{
			"etask.entity": "sc018539",
			"id": "8B2CFC1F-D0DB-2EE5-02C0-AB47DBD10775"
		},
		{
			"etask.entity": "sc018541",
			"id": "54B403D4-DE5F-77D1-AB09-C22A3610F557"
		},
		{
			"etask.entity": "sc018542",
			"id": "88F9D23A-8B4A-F196-5F5C-986B97ED9D83"
		},
		{
			"etask.entity": "sc018543",
			"id": "3E78C68F-17C5-6E87-B9DC-E66D4961BB7A"
		},
		{
			"etask.entity": "sc018544",
			"id": "2174C735-5EC2-76EE-3784-55B44DBBC385"
		},
		{
			"etask.entity": "sc018546",
			"id": "C47B157E-EED6-3476-8C33-249F12E5BAFE"
		},
		{
			"etask.entity": "sc018547",
			"id": "D4658E78-377C-B7E1-8F2A-467158365571"
		},
		{
			"etask.entity": "sc018548",
			"id": "A2401276-D6CC-294F-440C-1903E5EE0B70"
		},
		{
			"etask.entity": "sc018549",
			"id": "9B08841F-9973-46DB-61E1-D16837F1BB12"
		},
		{
			"etask.entity": "sc018551",
			"id": "A5DC00EA-675E-3366-45F3-E18F8F211455"
		},
		{
			"etask.entity": "sc023709",
			"id": "C0196624-9EE9-0536-5DC3-F4723A9D1B98"
		},
		{
			"etask.entity": "sc018553",
			"id": "75AF1928-3257-FEF2-64F8-A3C27F333959"
		},
		{
			"etask.entity": "sc018554",
			"id": "200ECEC2-C5AA-A4B8-2CEE-6080CBB96B75"
		},
		{
			"etask.entity": "sc018555",
			"id": "E184A3F5-A463-821A-19DD-96E42AD81FE8"
		},
		{
			"etask.entity": "sc018556",
			"id": "88543B6A-242D-8B36-C2A9-86AD5646481A"
		},
		{
			"etask.entity": "sc018558",
			"id": "770A9E02-6112-5C41-D7CF-A9C9CB1D350C"
		},
		{
			"etask.entity": "sc018559",
			"id": "75B49F8F-BF80-3DFB-61B0-B546FDBA9B1A"
		},
		{
			"etask.entity": "sc018560",
			"id": "D1387C35-6806-E0E8-7D3B-00740E623374"
		},
		{
			"etask.entity": "sc018561",
			"id": "AD5D2BAF-EB12-9439-B9D1-33309B50FA45"
		},
		{
			"etask.entity": "sc018563",
			"id": "1EBA71EF-4B33-4A46-6012-EC122D7A9AD7"
		},
		{
			"etask.entity": "sc018564",
			"id": "D91EC34E-959A-980F-5CAB-D959E0B6EE25"
		},
		{
			"etask.entity": "sc018565",
			"id": "D74AB92B-7B63-8EFA-C531-BB2205E9C7D7"
		},
		{
			"etask.entity": "sc018566",
			"id": "A6124983-5B73-C7F7-5D3D-58611C1FA88D"
		},
		{
			"etask.entity": "sc018568",
			"id": "BBBB342F-78FB-E001-D180-428A7E934F34"
		},
		{
			"etask.entity": "sc018569",
			"id": "4DA9090B-3941-03B3-028D-7D23714286EA"
		},
		{
			"etask.entity": "sc018570",
			"id": "CA38FECF-260E-970A-B769-B9DB55CE8434"
		},
		{
			"etask.entity": "sc018571",
			"id": "147AA59F-D68A-D3C9-776B-CB20FCF336D4"
		},
		{
			"etask.entity": "sc018573",
			"id": "9F83B0CA-DD7E-D8CC-6E1F-1777E808018E"
		},
		{
			"etask.entity": "sc023710",
			"id": "3ED953EB-6622-D133-18EA-B59EDA964C41"
		},
		{
			"etask.entity": "sc018575",
			"id": "1C880EED-A9C1-381F-CCBF-07AE7A383855"
		},
		{
			"etask.entity": "sc018576",
			"id": "40249B25-A4C1-EC86-5E6B-0A59EFAFBDF2"
		},
		{
			"etask.entity": "sc018577",
			"id": "3C7A73A0-8454-82BE-ECF3-2993FF73A6B5"
		},
		{
			"etask.entity": "sc018578",
			"id": "2C70036F-A1E0-E783-1D0A-BE7AF6E99ADA"
		},
		{
			"etask.entity": "sc018580",
			"id": "D56FC851-9401-0939-0444-6FF03557B72C"
		},
		{
			"etask.entity": "sc018581",
			"id": "313246D7-B099-3AB7-EE0D-8D12548E70AD"
		},
		{
			"etask.entity": "sc018582",
			"id": "4F1BDBC2-207F-84EF-A845-E09A24945ECD"
		},
		{
			"etask.entity": "sc018583",
			"id": "DA9F26DA-3292-DF8C-1E0E-91C6632B1CA8"
		},
		{
			"etask.entity": "sc018585",
			"id": "598B7050-46AB-7862-0BF1-E43CA1B0E93B"
		},
		{
			"etask.entity": "sc018586",
			"id": "473BB41B-758D-E64A-291C-F2B2B3F50F23"
		},
		{
			"etask.entity": "sc018587",
			"id": "F97BD083-6F81-F6F2-FC30-2AFED02ADE7B"
		},
		{
			"etask.entity": "sc018588",
			"id": "505D9271-7DB7-D17D-9C7E-AA1C6F899B78"
		},
		{
			"etask.entity": "sc018590",
			"id": "1549E1A7-1809-5566-3423-014A637B8F5C"
		},
		{
			"etask.entity": "sc018591",
			"id": "CAAFD256-3508-F481-A412-255DEE3A2877"
		},
		{
			"etask.entity": "sc018592",
			"id": "501B333A-85B5-BECF-BE19-5935897F084F"
		},
		{
			"etask.entity": "sc018593",
			"id": "0DF49084-6E2C-A418-F6F8-EA895CEB9FA1"
		},
		{
			"etask.entity": "sc018595",
			"id": "3A12F03D-F527-A31A-83E1-E6164125C3BD"
		},
		{
			"etask.entity": "sc023711",
			"id": "5CD3FBCC-0D2E-2C95-C7C3-B295DC9D8FF6"
		},
		{
			"etask.entity": "sc018597",
			"id": "DA0E5983-A3AD-A38B-1EC7-EE2FCCA52B8F"
		},
		{
			"etask.entity": "sc018598",
			"id": "DCB2B9B1-BD37-25F0-0E5B-841DFD899CBE"
		},
		{
			"etask.entity": "sc018599",
			"id": "BC189937-D7DA-0AE9-937A-BE247DEE2BD6"
		},
		{
			"etask.entity": "sc018600",
			"id": "355E5F25-DF75-149B-EDA4-252BC81C9EA0"
		},
		{
			"etask.entity": "sc018602",
			"id": "3BEDF6A3-83AF-2669-F3D8-BE62A79CA896"
		},
		{
			"etask.entity": "sc018603",
			"id": "B65736F1-4F7E-372C-1D8D-40BEC428B795"
		},
		{
			"etask.entity": "sc018604",
			"id": "E18A5019-F92C-B55C-474E-F7C66A82041E"
		},
		{
			"etask.entity": "sc018605",
			"id": "C5323D73-3320-2009-FA92-5F3F3963C0B2"
		},
		{
			"etask.entity": "sc018607",
			"id": "29662D07-A6CA-469C-77EF-D20A96B1F792"
		},
		{
			"etask.entity": "sc018608",
			"id": "54A1756B-5DD5-A331-9FB5-E1A39AC6BB69"
		},
		{
			"etask.entity": "sc018609",
			"id": "3DF16EC2-5450-3D91-135F-3F29507E30AA"
		},
		{
			"etask.entity": "sc018610",
			"id": "6D0DF8A4-BD87-EEB8-0F6E-077276133482"
		},
		{
			"etask.entity": "sc018612",
			"id": "D5989E73-E7C7-9D61-BB94-5621545189BE"
		},
		{
			"etask.entity": "sc018613",
			"id": "B562ACEA-5DFD-0D13-F7BF-D4ADC2132B0F"
		},
		{
			"etask.entity": "sc018614",
			"id": "20967B86-50B4-DD78-49B9-EE1ED31BC826"
		},
		{
			"etask.entity": "sc018615",
			"id": "ACAC1875-4474-0423-503C-5FA07A966255"
		},
		{
			"etask.entity": "sc018617",
			"id": "E4C0B755-99C8-8D0A-4A08-5E353C50AAF0"
		},
		{
			"etask.entity": "sc015496",
			"id": "85B71FF7-B2A0-1B5B-C444-C1428AF74B60"
		},
		{
			"etask.entity": "sc015498",
			"id": "D07BC5CC-B960-050E-372D-830E9020608D"
		},
		{
			"etask.entity": "sc015503",
			"id": "1058250D-6C1C-F49C-880E-22BD3642404C"
		},
		{
			"etask.entity": "sc015508",
			"id": "B574FFB7-57DF-ED20-E92E-D25693D65530"
		},
		{
			"etask.entity": "sc015513",
			"id": "0F448B61-48E6-1EF3-7F58-87ED9758D444"
		},
		{
			"etask.entity": "sc015518",
			"id": "72F86DE1-54C8-BBF6-096F-C81C382BF750"
		},
		{
			"etask.entity": "sc015520",
			"id": "3EAC836F-829C-E32A-DDF3-24498B91F6D0"
		},
		{
			"etask.entity": "sc015525",
			"id": "7062D639-5EB1-F2D2-A262-C815E6D6BBB4"
		},
		{
			"etask.entity": "sc015530",
			"id": "75719220-0A8C-A1AB-867B-E33BFB7A0F18"
		},
		{
			"etask.entity": "sc015535",
			"id": "EE617808-836B-7ED8-70A0-FFCCBCE0E915"
		},
		{
			"etask.entity": "sc015540",
			"id": "A5158EA8-E357-5150-1E53-AB836AE53C52"
		},
		{
			"etask.entity": "sc015542",
			"id": "D3E62444-259D-183E-D236-70A88E2D700E"
		},
		{
			"etask.entity": "sc015547",
			"id": "F688516B-0566-3F6C-6BD4-643E25B211DB"
		},
		{
			"etask.entity": "sc015552",
			"id": "D59AAFCE-F253-5D30-AE65-0C0DB348A618"
		},
		{
			"etask.entity": "sc015557",
			"id": "32BDC7E9-F3B2-8E20-A4C4-C9820B20245E"
		},
		{
			"etask.entity": "sc015562",
			"id": "A586FFAD-64DD-A64B-FC78-FE58E9C2E361"
		},
		{
			"etask.entity": "sc015564",
			"id": "04DFC632-E819-F047-5B9A-98E7F170E43D"
		},
		{
			"etask.entity": "sc015569",
			"id": "3B666306-3F9C-EB03-46EA-7B9F55D6E25E"
		},
		{
			"etask.entity": "sc023712",
			"id": "65547FAE-6DAE-57A7-1045-BD228CF174C1"
		},
		{
			"etask.entity": "sc018619",
			"id": "EE305C2F-4994-65C3-5EF0-F20477060183"
		},
		{
			"etask.entity": "sc018620",
			"id": "3FCBCE76-20BB-B048-F4F3-034F75655D90"
		},
		{
			"etask.entity": "sc018623",
			"id": "DD2C6788-3F84-F923-CB9F-9D2878E94BDA"
		},
		{
			"etask.entity": "sc018624",
			"id": "FF2928B2-02A7-D3FE-F3D1-F32F3B0D222C"
		},
		{
			"etask.entity": "sc018625",
			"id": "F0886937-3EC5-EEA0-2455-0C68BDFF5EC9"
		},
		{
			"etask.entity": "sc018626",
			"id": "A6B64079-04A7-3B0F-3D24-F78AF7E899A9"
		},
		{
			"etask.entity": "sc018627",
			"id": "EDF2ACC5-B7A6-4067-5FC1-F0886E37BE35"
		},
		{
			"etask.entity": "sc018628",
			"id": "036F8CF8-3300-A478-E39E-A72805AECA69"
		},
		{
			"etask.entity": "sc018629",
			"id": "61F31FBC-5021-621E-E769-5A344AAF98AE"
		},
		{
			"etask.entity": "sc018630",
			"id": "4F3CEEA8-C236-016C-524E-C246B0C1E08D"
		},
		{
			"etask.entity": "sc018631",
			"id": "A9B3E458-50FC-AD91-DE73-422182DBBDB8"
		},
		{
			"etask.entity": "sc018632",
			"id": "A642F194-700E-24FA-ACED-618BD3E14249"
		},
		{
			"etask.entity": "sc018635",
			"id": "8DE92CD5-D13B-0D10-5234-949E81928E70"
		},
		{
			"etask.entity": "sc018636",
			"id": "4A68BED9-A67E-D317-6C85-321DB7F32032"
		},
		{
			"etask.entity": "sc018637",
			"id": "394CDD55-9523-8D58-1FF2-33CD188D8AEB"
		},
		{
			"etask.entity": "sc018638",
			"id": "A2A03A08-8703-3D8C-77AB-E27994CA7465"
		},
		{
			"etask.entity": "sc018639",
			"id": "67643C62-51B4-B2C4-FC9F-CDEBDF4B7FD2"
		},
		{
			"etask.entity": "sc023713",
			"id": "14B294B3-34A8-626A-DB4A-EB08B02DA110"
		},
		{
			"etask.entity": "sc018641",
			"id": "6168607C-ABF3-A631-71B1-4933EB66F252"
		},
		{
			"etask.entity": "sc018642",
			"id": "D014F5DB-741E-1B82-501A-D10CEC04B1D0"
		},
		{
			"etask.entity": "sc018643",
			"id": "EF2BEF8C-2E7B-8C8B-6CA3-971633189857"
		},
		{
			"etask.entity": "sc018644",
			"id": "0CB2A513-02CC-ADB6-A7D4-5303B03300C5"
		},
		{
			"etask.entity": "sc018646",
			"id": "8119E311-A013-7BB7-49E2-31DE37AADC5E"
		},
		{
			"etask.entity": "sc018647",
			"id": "9C4D7B8D-DFBE-920E-0A2D-BDCE217EA745"
		},
		{
			"etask.entity": "sc018648",
			"id": "6B2D1C4F-FCDE-2CAF-D9CE-C472F81CBC49"
		},
		{
			"etask.entity": "sc018649",
			"id": "559335ED-2323-DCFC-F2EF-02ABDC4E69B7"
		},
		{
			"etask.entity": "sc018651",
			"id": "87CFB23C-B124-FC6A-F619-D6E092448DCA"
		},
		{
			"etask.entity": "sc018652",
			"id": "9589F3E0-5610-39B5-DB12-7BE495396E6A"
		},
		{
			"etask.entity": "sc018653",
			"id": "6E3F88D5-8AAC-75AD-E90B-B8B44FC0E9CE"
		},
		{
			"etask.entity": "sc018654",
			"id": "AC484216-AB6A-5481-08F7-683668D498DF"
		},
		{
			"etask.entity": "sc018656",
			"id": "D23BA8A2-FFA6-D9BD-5BB9-2698A72D0937"
		},
		{
			"etask.entity": "sc018657",
			"id": "B3F0E1CB-0725-B6DA-EED4-9112963D161D"
		},
		{
			"etask.entity": "sc018658",
			"id": "456F8C06-79A1-B142-DAF4-D6CBA23CB220"
		},
		{
			"etask.entity": "sc018659",
			"id": "148B56E2-A0FE-E798-FE7B-111A65FD9B28"
		},
		{
			"etask.entity": "sc018661",
			"id": "464D7AB7-093D-9FBE-6B0A-EB7033CC5818"
		},
		{
			"etask.entity": "sc023714",
			"id": "EC96B39E-A276-F6A0-AF1F-BC75C353732B"
		},
		{
			"etask.entity": "sc018663",
			"id": "9685D92A-66EF-C2EA-F990-3E4004E07487"
		},
		{
			"etask.entity": "sc018664",
			"id": "85E13C72-D49C-8EC4-D850-F07DFB201055"
		},
		{
			"etask.entity": "sc018665",
			"id": "1C39A871-444B-9934-141E-0A969218F6A6"
		},
		{
			"etask.entity": "sc018666",
			"id": "9293D309-BDCD-2575-7359-97EB03CFD096"
		},
		{
			"etask.entity": "sc018668",
			"id": "8B7F311D-88E2-8957-61F7-5AE53E8CA9B1"
		},
		{
			"etask.entity": "sc018669",
			"id": "77EAA9D7-FBF8-E4B1-1DAA-437BBE1B0DBA"
		},
		{
			"etask.entity": "sc018670",
			"id": "6978A4D6-746B-6F93-0B73-944B775945E4"
		},
		{
			"etask.entity": "sc018671",
			"id": "6890A816-7A4F-0B0B-B504-C101CAE4AA78"
		},
		{
			"etask.entity": "sc018673",
			"id": "A3472F73-393E-05E7-17F9-EB2F03C7C27B"
		},
		{
			"etask.entity": "sc018674",
			"id": "316D4E21-C0DE-688A-4F27-92074FBB9BBE"
		},
		{
			"etask.entity": "sc018675",
			"id": "8023CEB3-556D-E821-CF33-3785E8257732"
		},
		{
			"etask.entity": "sc018676",
			"id": "C88A45CD-F663-3756-BD42-3AD031985C64"
		},
		{
			"etask.entity": "sc018678",
			"id": "34B761B5-D707-2F73-1858-3E581A0B0BAF"
		},
		{
			"etask.entity": "sc018679",
			"id": "7FBBABBD-C6C8-7DE7-CE12-1C8CEBDC8A08"
		},
		{
			"etask.entity": "sc018680",
			"id": "3E207E17-4EBD-8B86-4BE9-8A9F80FD76A8"
		},
		{
			"etask.entity": "sc018681",
			"id": "F6AF0F26-F0AB-7DFF-AE67-785F04D7FC70"
		},
		{
			"etask.entity": "sc018683",
			"id": "50131901-C2E0-D167-E7E5-B98AADCC3F7A"
		},
		{
			"etask.entity": "sc018684",
			"id": "EE60F53E-970C-7A2A-F287-E0D0E27B44DC"
		},
		{
			"etask.entity": "sc018685",
			"id": "38220525-C639-64CB-471B-2E9249CB2562"
		},
		{
			"etask.entity": "sc018686",
			"id": "C7C5410F-F780-1096-B3B8-793F75AB2286"
		},
		{
			"etask.entity": "sc018687",
			"id": "05F67435-745A-3709-9DC9-85DFD216EF6B"
		},
		{
			"etask.entity": "sc018688",
			"id": "8BFAC4A0-FEF8-4D31-64FE-FF6B879BC038"
		},
		{
			"etask.entity": "sc018689",
			"id": "986849DD-B507-7745-CF45-3C4992FD7777"
		},
		{
			"etask.entity": "sc018690",
			"id": "DCFD9F36-2015-88D7-F25E-31C58F3533F9"
		},
		{
			"etask.entity": "sc018691",
			"id": "3EDB456D-44D8-5D4E-D6DF-174FE2C5B41B"
		},
		{
			"etask.entity": "sc018692",
			"id": "914282EF-E680-F910-E840-85FFFF258596"
		},
		{
			"etask.entity": "sc018693",
			"id": "4B74F3E6-0B4A-B8AF-E292-E2DB56A86470"
		},
		{
			"etask.entity": "sc018694",
			"id": "7D753807-2534-50C4-1CBB-0EFA7117100A"
		},
		{
			"etask.entity": "sc018695",
			"id": "8D54E035-D8B0-65CB-23FF-FFE1C9D18500"
		},
		{
			"etask.entity": "sc018696",
			"id": "1E4DC4E2-51B7-3505-0432-A382A14602F3"
		},
		{
			"etask.entity": "sc018697",
			"id": "144CDE9E-F0C5-87A2-4FAD-1E3BC11CBC55"
		},
		{
			"etask.entity": "sc018698",
			"id": "3E02B58F-9B48-D4D6-55D7-25F40DFF40AD"
		},
		{
			"etask.entity": "sc018699",
			"id": "8BDEA183-8A7E-48FA-EB8F-1AC24091E8CD"
		},
		{
			"etask.entity": "sc023715",
			"id": "750D7F41-A876-07AB-3C88-F51A0BF64179"
		},
		{
			"etask.entity": "sc023716",
			"id": "DDF1062B-C910-A75C-FEBD-5ED845A36373"
		},
		{
			"etask.entity": "sc023717",
			"id": "100ED7C9-6BB3-465C-8FB8-D54F20B220D0"
		},
		{
			"etask.entity": "sc015574",
			"id": "DD6A895B-1782-F076-0B37-2748B00451D1"
		},
		{
			"etask.entity": "sc015579",
			"id": "0AB073E3-B63B-A663-7052-BABFFBDD77B6"
		},
		{
			"etask.entity": "sc015584",
			"id": "8B1D1605-AB03-4CFA-A262-403E4AA785F0"
		},
		{
			"etask.entity": "sc015586",
			"id": "BFAFB42E-0D34-7683-234F-BA41C6140E8F"
		},
		{
			"etask.entity": "sc015591",
			"id": "177C1773-D16B-05C4-DDB5-B29AB38FDCE5"
		},
		{
			"etask.entity": "sc015596",
			"id": "D055EBF5-9691-3220-3B49-C4401F552D53"
		},
		{
			"etask.entity": "sc015601",
			"id": "DE854950-C8EE-8832-B012-230D15F2E505"
		},
		{
			"etask.entity": "sc015606",
			"id": "49490EC3-E3E1-654C-9A3C-FC28C1BAEA20"
		},
		{
			"etask.entity": "sc015608",
			"id": "2902D37E-CB27-C86F-7F27-BD86FBDB69D6"
		},
		{
			"etask.entity": "sc015613",
			"id": "9860CF02-FA13-B33A-44C0-07B799A69390"
		},
		{
			"etask.entity": "sc015618",
			"id": "D6CEBCD5-1E5D-031D-1795-2C2EB29D47EA"
		},
		{
			"etask.entity": "sc015620",
			"id": "54C3676A-BC9B-EF75-EFE9-C97A7EDC7E9E"
		},
		{
			"etask.entity": "sc015621",
			"id": "891E1965-21C5-521A-CD25-F69C07E5A554"
		},
		{
			"etask.entity": "sc015622",
			"id": "EE2B6392-8E36-EC6F-AF05-CA382AFF911B"
		},
		{
			"etask.entity": "sc015623",
			"id": "E719524A-C7AA-F123-93D2-2C01B1361D31"
		},
		{
			"etask.entity": "sc015624",
			"id": "2DB0C980-86D5-1AA7-2AC8-72D5A0BA3359"
		},
		{
			"etask.entity": "sc015625",
			"id": "77F7BD7D-5A45-8BF0-6D49-E9C297C8F53D"
		},
		{
			"etask.entity": "sc015626",
			"id": "3B036B25-74B5-5CB9-1D23-E1C91CF9BD52"
		},
		{
			"etask.entity": "sc015627",
			"id": "0B954EA4-C00C-4990-A038-CB0EC344787D"
		},
		{
			"etask.entity": "sc015628",
			"id": "3CF73946-47CC-0030-CC74-B50E53A730B5"
		},
		{
			"etask.entity": "sc015629",
			"id": "0EDF7406-9798-79F4-F606-23A2C80E3F31"
		},
		{
			"etask.entity": "sc015630",
			"id": "9A0AAA48-7FCD-0C8B-7DA1-5CD744E28C78"
		},
		{
			"etask.entity": "sc015631",
			"id": "D4785A9B-2346-EF41-8856-A98203DEF7A0"
		},
		{
			"etask.entity": "sc015632",
			"id": "429F153B-01EA-D0D2-6877-52140FB45ABB"
		},
		{
			"etask.entity": "sc015633",
			"id": "FA9E0F3C-E0D1-6C00-ED28-974DF3586EC1"
		},
		{
			"etask.entity": "sc015634",
			"id": "6D44E626-EF82-0576-A28F-567B990BC5B4"
		},
		{
			"etask.entity": "sc015635",
			"id": "61DA31A6-1E99-68F6-87BC-98334D014046"
		},
		{
			"etask.entity": "sc015641",
			"id": "6E43EE3B-366C-9BF8-A6E5-CB7815EFB622"
		},
		{
			"etask.entity": "sc015642",
			"id": "C46FF23A-9E38-3703-98F3-1ED2EC12B140"
		},
		{
			"etask.entity": "sc015643",
			"id": "C7E270A7-16CC-E4B8-6378-30E9C502F5E3"
		},
		{
			"etask.entity": "sc015644",
			"id": "68B737C4-5368-53F4-C996-0C985408DB91"
		},
		{
			"etask.entity": "sc015645",
			"id": "5C227DDD-3AC3-07C3-D307-CE707A62141A"
		},
		{
			"etask.entity": "sc015646",
			"id": "0A47FB3D-AAE6-AC44-7845-F2A4CCAC5F3B"
		},
		{
			"etask.entity": "sc015647",
			"id": "3E299E7D-CAC0-2E6E-4BF7-50174A654AC8"
		},
		{
			"etask.entity": "sc015648",
			"id": "26EAA1C6-1535-9034-8EEB-FB1F5A5C809B"
		},
		{
			"etask.entity": "sc015649",
			"id": "EDB58692-76E1-4573-2F7F-BBA55C56C94E"
		},
		{
			"etask.entity": "sc015650",
			"id": "2D0BE2BA-E7EF-9782-5820-13C435229226"
		},
		{
			"etask.entity": "sc015651",
			"id": "4F8DD3A7-DB77-AD6B-8A80-7C13E77A41FA"
		},
		{
			"etask.entity": "sc015652",
			"id": "E92D45B3-6868-4188-A424-51D9CC398DCF"
		},
		{
			"etask.entity": "sc015653",
			"id": "65C8E5A2-0310-9947-76ED-05175C4F2107"
		},
		{
			"etask.entity": "sc015654",
			"id": "85BDA773-8F0D-7422-19BB-DB9DB102ACE7"
		},
		{
			"etask.entity": "sc015655",
			"id": "CCA97E48-2E98-E173-E4E0-69F0536178E1"
		},
		{
			"etask.entity": "sc015656",
			"id": "9D4F0E4F-7723-9083-42F2-186DB225F807"
		},
		{
			"etask.entity": "sc015657",
			"id": "7AA264ED-9166-7C12-481F-DCA2BD1763FA"
		},
		{
			"etask.entity": "sc015658",
			"id": "76CB69B9-A98F-E29E-EAA6-3A9369BDC9E0"
		},
		{
			"etask.entity": "sc015659",
			"id": "E91A9059-453F-5D60-D6D1-88936EEC495E"
		},
		{
			"etask.entity": "sc015660",
			"id": "E2F74F5F-E060-013F-FFA3-A3165F70B24C"
		},
		{
			"etask.entity": "sc015661",
			"id": "A25B8044-991F-D7F2-F998-827316E3EAE3"
		},
		{
			"etask.entity": "sc015662",
			"id": "A9F79F0B-B643-890F-B4D6-1550BEDA09FE"
		},
		{
			"etask.entity": "sc015663",
			"id": "337DB182-627A-1302-786C-6E4A795EE284"
		},
		{
			"etask.entity": "sc015664",
			"id": "5A7AFEA6-0A26-8F20-84AD-B2C0A0033F31"
		},
		{
			"etask.entity": "sc015665",
			"id": "2F6E0FA4-D5F6-D51E-99E3-E4545D7922B0"
		},
		{
			"etask.entity": "sc015666",
			"id": "065CB853-CD4E-6EF2-39FB-EB7AFD070E77"
		},
		{
			"etask.entity": "sc015674",
			"id": "9A372C5D-7544-C014-717C-33854A7347F1"
		},
		{
			"etask.entity": "sc015679",
			"id": "4B73A64B-0EB9-A433-BF66-DB25EEFB30DC"
		},
		{
			"etask.entity": "sc015684",
			"id": "69701403-5CD9-10F3-22B6-A16F76F6D6C0"
		},
		{
			"etask.entity": "sc015689",
			"id": "D755AA55-396F-1B84-3206-02A94B157C11"
		},
		{
			"etask.entity": "sc015694",
			"id": "AE92999E-A103-FEDD-7571-93FB61BBC22C"
		},
		{
			"etask.entity": "sc015696",
			"id": "4772AEA4-731D-3457-DC40-7F5A8F3AC57B"
		},
		{
			"etask.entity": "sc015701",
			"id": "4F0D5D1B-C60E-2BFB-32FB-77FB98A980C0"
		},
		{
			"etask.entity": "sc015706",
			"id": "58452C36-DE08-6E89-62AB-E565CF601E4D"
		},
		{
			"etask.entity": "sc015711",
			"id": "015825BE-4FDD-E047-5034-4EAD827B8DB0"
		},
		{
			"etask.entity": "sc015716",
			"id": "167CABB5-247A-172F-5684-02045565FF56"
		},
		{
			"etask.entity": "sc015718",
			"id": "51725DAC-1157-DAE6-EA58-120B093CEFD8"
		},
		{
			"etask.entity": "sc015723",
			"id": "61FE5113-4178-9203-9517-8570F387923C"
		},
		{
			"etask.entity": "sc015728",
			"id": "F9D9E6E9-B65A-6995-2D04-268DDEC58A4D"
		},
		{
			"etask.entity": "sc015733",
			"id": "3F7E7EAF-1122-05DD-0F7A-9722D8BF5918"
		},
		{
			"etask.entity": "sc015738",
			"id": "6A35E2CB-CFBC-B198-8222-A0251647154A"
		},
		{
			"etask.entity": "sc015740",
			"id": "850F49BE-8AF2-6124-DB93-380E503254E7"
		},
		{
			"etask.entity": "sc015745",
			"id": "5D35BB3B-9E52-176D-D8F8-10178C56FEAD"
		},
		{
			"etask.entity": "sc015750",
			"id": "5E744763-3774-5522-3DC9-EA4620BB9B25"
		},
		{
			"etask.entity": "sc015755",
			"id": "C971CB76-3645-BCF4-4D49-BE7B089FECD0"
		},
		{
			"etask.entity": "sc015760",
			"id": "B13D8F7D-B832-C3AF-0121-F9B613B68840"
		},
		{
			"etask.entity": "sc015762",
			"id": "399A24FF-6513-E33B-1AF5-57D4A83B71AA"
		},
		{
			"etask.entity": "sc015767",
			"id": "852682A9-FAA8-BC4F-4CBF-0F52C67596B6"
		},
		{
			"etask.entity": "sc015772",
			"id": "EB50B4C6-DBD8-169C-1F3D-0B2C13C94C81"
		},
		{
			"etask.entity": "sc015777",
			"id": "A0DEDF6B-CF45-EE53-8AEF-B49D4B8ED621"
		},
		{
			"etask.entity": "sc015782",
			"id": "762A1681-514D-1F2A-8B14-F67C189259E2"
		},
		{
			"etask.entity": "sc015784",
			"id": "1E4024E4-165F-58F1-08AB-ACDAFE1BC3DE"
		},
		{
			"etask.entity": "sc015789",
			"id": "E3FD8C8B-4106-A0F9-704B-B2FFCF3B27DC"
		},
		{
			"etask.entity": "sc015794",
			"id": "EAEF8591-BC03-F90E-CC25-54319DBA70E8"
		},
		{
			"etask.entity": "sc015799",
			"id": "87CAFC16-734E-1D99-C393-898246E81682"
		},
		{
			"etask.entity": "sc015804",
			"id": "DB33BB52-BAD8-FFFF-E1BC-ACB7101DA59B"
		},
		{
			"etask.entity": "sc015806",
			"id": "47A82B5F-3EDF-5AED-6213-4127EEC6083F"
		},
		{
			"etask.entity": "sc015811",
			"id": "12D8CAFE-120F-C886-9D91-A52E1D6F6DD1"
		},
		{
			"etask.entity": "sc015816",
			"id": "3C303F8A-EFB3-6802-C451-696C25BC1D14"
		},
		{
			"etask.entity": "sc015821",
			"id": "17B70187-706E-F50B-E231-E7502CCB5F7E"
		},
		{
			"etask.entity": "sc015826",
			"id": "71712614-2A8A-BABB-00EF-C054A5849C4B"
		},
		{
			"etask.entity": "sc015828",
			"id": "9C9E7B1E-7E93-8202-017C-B8B422ECB1B1"
		},
		{
			"etask.entity": "sc015833",
			"id": "15F8E293-53A6-4AEA-E617-C3B94FB3D08B"
		},
		{
			"etask.entity": "sc015838",
			"id": "A938E81D-413E-2F8E-D76D-40323013EE30"
		},
		{
			"etask.entity": "sc015843",
			"id": "9CC922C7-0B3C-C2CA-763B-BAAA5C4F8350"
		},
		{
			"etask.entity": "sc015848",
			"id": "5F814922-3722-3D51-9FAD-7FF1F607B5F5"
		},
		{
			"etask.entity": "sc015850",
			"id": "D07EE497-5A06-EFAB-1F42-C240B6E82218"
		},
		{
			"etask.entity": "sc015855",
			"id": "9C40FE5C-82FB-1EA0-7A9B-74D41EA74CAF"
		},
		{
			"etask.entity": "sc015860",
			"id": "6B2DE20B-B0CC-3157-3150-3AA416F6B408"
		},
		{
			"etask.entity": "sc015865",
			"id": "E5113C48-1804-346C-5422-A53CFAA13CF8"
		},
		{
			"etask.entity": "sc015870",
			"id": "772A474A-5EBE-EE62-E274-215E81FF0A86"
		},
		{
			"etask.entity": "sc015872",
			"id": "043E69EB-2188-A310-E348-EF73CCC94230"
		},
		{
			"etask.entity": "sc015877",
			"id": "9578A791-BFF8-1B05-27BA-F32BB9095F13"
		},
		{
			"etask.entity": "sc015882",
			"id": "F29991A0-35DB-1AD9-0A44-1C6FC3D62B0F"
		},
		{
			"etask.entity": "sc015887",
			"id": "3751A682-8B76-487E-B385-1EA197AB450E"
		},
		{
			"etask.entity": "sc015892",
			"id": "9F0B8EE0-CD94-F1E4-5369-DD2C4C980663"
		},
		{
			"etask.entity": "sc015894",
			"id": "DF051BB3-DC76-2DE1-77A6-FF1C109DA6BE"
		},
		{
			"etask.entity": "sc015899",
			"id": "FCAC0244-372B-C76F-07AB-B6F3BF5E42C7"
		},
		{
			"etask.entity": "sc015904",
			"id": "E9184F5D-CF84-52F8-9B19-4B7CC0F7C0D4"
		},
		{
			"etask.entity": "sc015909",
			"id": "B28B1A47-BD1A-2108-8D76-C19B6E2E27BC"
		},
		{
			"etask.entity": "sc015914",
			"id": "66FA2AD2-2339-8EE4-DDA5-0F4237FEDB8D"
		},
		{
			"etask.entity": "sc015916",
			"id": "CFF9D573-A59D-8A3D-8B45-A8062CAEEDF0"
		},
		{
			"etask.entity": "sc015921",
			"id": "BE1AB917-12C6-CD9C-F605-BD66EE522245"
		},
		{
			"etask.entity": "sc015926",
			"id": "5A8C8022-6A70-0EC9-B505-07CF0C194090"
		},
		{
			"etask.entity": "sc015931",
			"id": "1F1D18B3-7922-BD0F-A69E-94CBBDEA6B56"
		},
		{
			"etask.entity": "sc015936",
			"id": "46E3862D-FCC6-B159-7A56-C4208351900B"
		},
		{
			"etask.entity": "sc015938",
			"id": "4F9AA3D0-CA61-6731-BC72-9D4E7A2E7BBA"
		},
		{
			"etask.entity": "sc015943",
			"id": "197CA878-E145-24CF-B21F-B889CE8AF4D6"
		},
		{
			"etask.entity": "sc015948",
			"id": "79FCCB7C-1980-C5CD-CFC9-40A64474E180"
		},
		{
			"etask.entity": "sc015953",
			"id": "3770BCA0-B3E6-66F6-573E-FD5BCFAADC1F"
		},
		{
			"etask.entity": "sc015958",
			"id": "82AE7B99-EAF3-DD26-9D90-B7ECBF9F4973"
		},
		{
			"etask.entity": "sc015960",
			"id": "CD1A8ABA-760F-2367-C17C-D8F95F5093E0"
		},
		{
			"etask.entity": "sc015965",
			"id": "E924E2C7-8896-B421-A907-B7934064DDB8"
		},
		{
			"etask.entity": "sc015970",
			"id": "8B5DCD14-7E24-B7A7-6EA1-4F277BFF9C0D"
		},
		{
			"etask.entity": "sc015975",
			"id": "984BC8F9-9AE0-AC4A-2B17-0C461D63F162"
		},
		{
			"etask.entity": "sc015980",
			"id": "1F253D9A-46BD-5C2F-41D3-7B202B87D811"
		},
		{
			"etask.entity": "sc015982",
			"id": "DBEB56AB-F281-7005-031E-7D366C8162DB"
		},
		{
			"etask.entity": "sc015987",
			"id": "D47DBF43-C68F-5ECB-8903-EED179DC0B06"
		},
		{
			"etask.entity": "sc015992",
			"id": "1496AD47-8D84-985D-AA27-EE4C92E5C7AE"
		},
		{
			"etask.entity": "sc015997",
			"id": "B9DF7C49-6023-A7DD-26D4-50A5468E6884"
		},
		{
			"etask.entity": "sc016002",
			"id": "4C6565D5-989A-E311-7CCF-BA0268ED08AC"
		},
		{
			"etask.entity": "sc016004",
			"id": "F3B32943-AC32-70D5-4B46-56A8C07B4C0D"
		},
		{
			"etask.entity": "sc016009",
			"id": "DE4E3F48-90ED-62D1-6E8A-FE9BC2A7D647"
		},
		{
			"etask.entity": "sc016010",
			"id": "6C17677E-FB30-9B35-C5A9-81C3CC32ACA5"
		},
		{
			"etask.entity": "sc016011",
			"id": "0FE0A9FA-D6A9-F84F-4FC2-D826CE94E36F"
		},
		{
			"etask.entity": "sc016012",
			"id": "EE8A66CB-BAFB-827D-9806-F096CA112288"
		},
		{
			"etask.entity": "sc016013",
			"id": "09C38514-A9A9-CCAC-BE5B-71F597913AAC"
		},
		{
			"etask.entity": "sc016014",
			"id": "FC3CCD8E-F7F9-E0D4-EB69-2CAA1AC2AC1C"
		},
		{
			"etask.entity": "sc016017",
			"id": "A25EA465-0FDE-89DE-55A1-8F0ADF86513D"
		},
		{
			"etask.entity": "sc016022",
			"id": "3E673850-1DD8-6A56-F5CA-A1B0E715C18D"
		},
		{
			"etask.entity": "sc016023",
			"id": "24747CB9-26E7-2FE6-261C-73DA53B29615"
		},
		{
			"etask.entity": "sc016024",
			"id": "7F3A4A6F-CA48-3496-6DB2-43521F86F29C"
		},
		{
			"etask.entity": "sc016025",
			"id": "EBBFC4F7-18D9-2964-1022-6BE926E3E629"
		},
		{
			"etask.entity": "sc016026",
			"id": "82CA6A51-E696-98A2-9CDD-7BAC7AE8042D"
		},
		{
			"etask.entity": "sc016027",
			"id": "B61D7092-DED5-8EED-A48F-A0942966D519"
		},
		{
			"etask.entity": "sc016028",
			"id": "A5263EC1-5B44-10C6-96CC-9DC19217BEC5"
		},
		{
			"etask.entity": "sc016029",
			"id": "59DC9941-079C-1D44-FEB9-B21279F5A20C"
		},
		{
			"etask.entity": "sc016030",
			"id": "4E7832A1-3EB5-121A-B8A0-CE881EBBDD18"
		},
		{
			"etask.entity": "sc016031",
			"id": "EDD1ADA3-43BD-9B4E-9A56-C23CA8AE4691"
		},
		{
			"etask.entity": "sc016032",
			"id": "0437F5C5-7F0C-2FA0-13FE-5946AA12A400"
		},
		{
			"etask.entity": "sc016033",
			"id": "695DD3DD-C247-E9B2-A499-FCB1B4D44431"
		},
		{
			"etask.entity": "sc016034",
			"id": "3695328A-03C8-057C-7D46-DA6B63F8951B"
		},
		{
			"etask.entity": "sc016035",
			"id": "AE9EE569-671C-9165-C3EA-F85E4810A3AB"
		},
		{
			"etask.entity": "sc016036",
			"id": "51EE198D-2C2F-8931-7A41-8CC06C0AD100"
		},
		{
			"etask.entity": "sc016037",
			"id": "FEAD5E6A-054B-73CC-D8CD-653779C73C67"
		},
		{
			"etask.entity": "sc016038",
			"id": "BF2B2536-7503-DB11-E0C7-91A52E5C223F"
		},
		{
			"etask.entity": "sc016039",
			"id": "5B326313-1E48-A537-6136-9D311C0CAF34"
		},
		{
			"etask.entity": "sc016040",
			"id": "6201BB07-FA11-208D-7560-E6CE96CC343F"
		},
		{
			"etask.entity": "sc016041",
			"id": "1D332868-95A9-AB4B-0C73-FE0F4919A86E"
		},
		{
			"etask.entity": "sc016042",
			"id": "B0A2A367-1F14-42AE-B773-517E2251E9D5"
		},
		{
			"etask.entity": "sc016043",
			"id": "63538E77-3197-B76D-4330-B11F40BEDA57"
		},
		{
			"etask.entity": "sc016044",
			"id": "CF9144DC-A734-1FCA-07F4-593B03FEF963"
		},
		{
			"etask.entity": "sc016045",
			"id": "D3AFB696-ECCE-45AD-846D-13235A156E1B"
		},
		{
			"etask.entity": "sc016046",
			"id": "1E2F83ED-33AE-6D57-7280-99E74D5014CE"
		},
		{
			"etask.entity": "sc016047",
			"id": "969F6BD3-5507-0287-168E-5C155970D386"
		},
		{
			"etask.entity": "sc016048",
			"id": "7036C9AE-9E7B-DC63-DD99-DAAB3FC92018"
		},
		{
			"etask.entity": "sc016049",
			"id": "9D439FF5-901D-D77A-785D-5F5968CD2AB2"
		},
		{
			"etask.entity": "sc016050",
			"id": "838177BF-D4DC-07FF-00BF-EC5424F30C39"
		},
		{
			"etask.entity": "sc016051",
			"id": "E8E85332-5331-8C5E-D821-2AA9BA968180"
		},
		{
			"etask.entity": "sc016052",
			"id": "6CAE26BE-5E5A-9ADD-2BF4-BADA6C0B81E9"
		},
		{
			"etask.entity": "sc016053",
			"id": "2A410E7B-EBFF-2046-DA82-AE33A0A5FE5D"
		},
		{
			"etask.entity": "sc016054",
			"id": "EF7EE983-09D7-69DA-3E1A-CAB711185513"
		},
		{
			"etask.entity": "sc016055",
			"id": "972E359A-3EB5-91FC-2D40-647DBD3E238E"
		},
		{
			"etask.entity": "sc016056",
			"id": "07C3D96F-486E-9CFF-5364-7B673DF3C259"
		},
		{
			"etask.entity": "sc016057",
			"id": "97891E99-790C-5B54-C809-2F1AF79100D7"
		},
		{
			"etask.entity": "sc016058",
			"id": "75E942F6-C187-0C26-CBF2-4EA212290959"
		},
		{
			"etask.entity": "sc016061",
			"id": "7D99025E-7DCE-F139-DFC1-30EACBE2D69A"
		},
		{
			"etask.entity": "sc016063",
			"id": "C74E6E11-E4EC-8A05-CE13-0FF3DD5327C5"
		},
		{
			"etask.entity": "sc016064",
			"id": "23D4C195-BD41-432D-C3E4-C013397972B1"
		},
		{
			"etask.entity": "sc016065",
			"id": "6FC16B1D-2303-7F05-CE8E-18BCD36ADE25"
		},
		{
			"etask.entity": "sc016066",
			"id": "ED303FE7-5FD3-6A07-195B-721614E9B9AB"
		},
		{
			"etask.entity": "sc016067",
			"id": "3CF3089D-C032-252E-9003-824A2DEC2ECB"
		},
		{
			"etask.entity": "sc016068",
			"id": "5E02F014-D8B4-7CF2-2672-F14A3CF2C7FF"
		},
		{
			"etask.entity": "sc016069",
			"id": "76892EB9-2C53-C3A5-65D9-D1E067FFE592"
		},
		{
			"etask.entity": "sc016070",
			"id": "1ADB6866-E055-EA87-1BB6-1F0DE3B728D9"
		},
		{
			"etask.entity": "sc016071",
			"id": "AD0A2601-9CF9-192B-F809-BA74D2936128"
		},
		{
			"etask.entity": "sc016072",
			"id": "E82A8716-803C-7501-3B67-DE8FC4606560"
		},
		{
			"etask.entity": "sc016073",
			"id": "71CDE3D5-0226-2BD5-7198-EA086592135A"
		},
		{
			"etask.entity": "sc016074",
			"id": "3BA79C9B-2C2D-A185-1E0C-34C50307B32B"
		},
		{
			"etask.entity": "sc016075",
			"id": "A7DC03BF-5850-148C-7CFB-F5D0632E49C0"
		},
		{
			"etask.entity": "sc016076",
			"id": "61531974-0F76-ED73-733F-ABA0DE7BB1B9"
		},
		{
			"etask.entity": "sc016077",
			"id": "8AEE2747-D962-F4CA-5236-CD8640FAD1B3"
		},
		{
			"etask.entity": "sc016078",
			"id": "78904A09-682C-8B03-1BEF-624EA095F680"
		},
		{
			"etask.entity": "sc016079",
			"id": "7564892D-3025-9A53-F583-208B0319573D"
		},
		{
			"etask.entity": "sc016080",
			"id": "382F51E2-14DE-2E16-6DAB-F77AE3BDD224"
		},
		{
			"etask.entity": "sc016081",
			"id": "D77400E9-790A-20C5-3192-A022D5E970F6"
		},
		{
			"etask.entity": "sc016082",
			"id": "C2124BCB-B23F-0C8A-BFE5-CDFAED72DD1D"
		},
		{
			"etask.entity": "sc016083",
			"id": "8DAF32A9-5992-335D-AA41-96EB4C403990"
		},
		{
			"etask.entity": "sc016084",
			"id": "421E8A2A-1B4E-A34B-D3D3-1CA72A54868F"
		},
		{
			"etask.entity": "sc016085",
			"id": "34219069-7C5B-4B40-D7F0-3DB44E1BB8AB"
		},
		{
			"etask.entity": "sc016086",
			"id": "3A8D31A5-A75C-BBF9-B61E-1DF92FB4DBE3"
		},
		{
			"etask.entity": "sc016087",
			"id": "05E9DA5D-6A11-FA3B-224E-4E2A61794A0C"
		},
		{
			"etask.entity": "sc016088",
			"id": "CC6E65E2-4187-76B0-1763-742EE7C20639"
		},
		{
			"etask.entity": "sc016089",
			"id": "933B8FC4-AEE1-E155-4027-59FF9A4CA31E"
		},
		{
			"etask.entity": "sc016090",
			"id": "3636118B-537F-403F-0011-81E75D9C21B1"
		},
		{
			"etask.entity": "sc016091",
			"id": "41947FFE-C01B-B046-4415-0248AA9315D2"
		},
		{
			"etask.entity": "sc016092",
			"id": "656161F8-762B-FDA4-33BF-2E0EFB87A816"
		},
		{
			"etask.entity": "sc016093",
			"id": "92667A8E-9417-9713-6628-4107280D19E5"
		},
		{
			"etask.entity": "sc016094",
			"id": "025F1CFC-353C-7335-D92A-7A171CA6C511"
		},
		{
			"etask.entity": "sc016095",
			"id": "64D33847-EEBD-ECFC-1F4C-706D15632ED6"
		},
		{
			"etask.entity": "sc016096",
			"id": "3CD46388-1002-D3B8-0888-67D32B50E502"
		},
		{
			"etask.entity": "sc016097",
			"id": "5A16CFCE-9DE1-96A6-1A94-34DF4144D59B"
		},
		{
			"etask.entity": "sc016098",
			"id": "C77E0101-3A21-461F-E0EA-DE967002B24D"
		},
		{
			"etask.entity": "sc016099",
			"id": "1A457A42-55FB-54C8-C03D-A32C1FC14AA7"
		},
		{
			"etask.entity": "sc016100",
			"id": "03428395-C633-4EC4-A93A-C986A75EBC5B"
		},
		{
			"etask.entity": "sc016101",
			"id": "4B9262F2-63A8-111F-3282-231BED49A07B"
		},
		{
			"etask.entity": "sc016102",
			"id": "63A190D7-67D6-44B7-E3C0-BB84B9444700"
		},
		{
			"etask.entity": "sc016104",
			"id": "192AB6E4-C21E-80DE-CBA3-EDECC3B75ECC"
		},
		{
			"etask.entity": "sc016105",
			"id": "787800D5-BFCA-9B37-1588-F0AE4224D8B2"
		},
		{
			"etask.entity": "sc016106",
			"id": "1AA6589C-5250-85EB-8162-781AD61FDE09"
		},
		{
			"etask.entity": "sc016108",
			"id": "11FC5D4C-21AB-8A5F-789F-4CF5EDF1841F"
		},
		{
			"etask.entity": "sc016109",
			"id": "9C3B7762-FB24-C593-F9DF-A450EB2F82D1"
		},
		{
			"etask.entity": "sc016110",
			"id": "08B7DADC-6E49-02E7-7611-F6372D09C4FD"
		},
		{
			"etask.entity": "sc016111",
			"id": "0EE4BF32-DFD7-E42A-BE10-B6F68A4E242E"
		},
		{
			"etask.entity": "sc016113",
			"id": "C90DCF60-DB0E-D0AA-5E51-D13AA69031D5"
		},
		{
			"etask.entity": "sc016114",
			"id": "137D083A-547E-8641-EC39-453464EFA74C"
		},
		{
			"etask.entity": "sc016115",
			"id": "A75ACDB6-8CDD-3D80-B450-E4D061229816"
		},
		{
			"etask.entity": "sc016116",
			"id": "12196AE8-84E2-6346-1806-6EA64A8DF7CB"
		},
		{
			"etask.entity": "sc016117",
			"id": "3B5AF549-C9DB-7C28-FC33-442F27184BF0"
		},
		{
			"etask.entity": "sc016118",
			"id": "094B70B7-8A06-1B89-742F-0CAB9D2745D9"
		},
		{
			"etask.entity": "sc016120",
			"id": "ED978E3F-0371-5E3D-FC0E-04DAC6054AC4"
		},
		{
			"etask.entity": "sc016121",
			"id": "C9E71D81-6D8D-F9CD-35A5-3903EC7776A9"
		},
		{
			"etask.entity": "sc016125",
			"id": "E3202222-E810-6987-B63B-502CA4B8F795"
		},
		{
			"etask.entity": "sc016127",
			"id": "4CE40CE3-D42E-22A6-C2C3-640C95568ED8"
		},
		{
			"etask.entity": "sc016128",
			"id": "B2EFFE15-C34F-8A9E-3EA0-0B3B8F139CD9"
		},
		{
			"etask.entity": "sc016129",
			"id": "20127207-2FF2-7835-0ED7-15F91AA36411"
		},
		{
			"etask.entity": "sc016131",
			"id": "BFBB802C-3861-1550-F15C-85774DEC34F6"
		},
		{
			"etask.entity": "sc016132",
			"id": "320CC086-A3C9-4F22-BE90-688B5138944A"
		},
		{
			"etask.entity": "sc016133",
			"id": "CC572650-8AE7-C033-C0DC-0E9C5AF45B75"
		},
		{
			"etask.entity": "sc016135",
			"id": "5FD23A3B-E1A5-A690-4AAA-668CAC1D587B"
		},
		{
			"etask.entity": "sc016136",
			"id": "199F0648-769A-7E02-8976-42BFEE9BDFEF"
		},
		{
			"etask.entity": "sc016137",
			"id": "A8ED0490-AA0A-5438-876C-9E754DCC0966"
		},
		{
			"etask.entity": "sc016138",
			"id": "86D308C2-7B35-C99F-D39E-94F32DAD24CF"
		},
		{
			"etask.entity": "sc016139",
			"id": "E70FEADB-46CE-3E20-C004-AD18E570DDFC"
		},
		{
			"etask.entity": "sc016141",
			"id": "32A9E6C4-A41E-23D4-589A-98F083D254A9"
		},
		{
			"etask.entity": "sc016142",
			"id": "564E0B83-2348-A6E1-3914-CEE0A5A99FE1"
		},
		{
			"etask.entity": "sc016143",
			"id": "D3A20E47-7C11-F2E6-E0FC-13F8F7CFFE10"
		},
		{
			"etask.entity": "sc016144",
			"id": "C370D711-06A4-763E-29E2-C68392167BA1"
		},
		{
			"etask.entity": "sc016146",
			"id": "6C8293ED-E20D-EEEA-D175-5427C46C0686"
		},
		{
			"etask.entity": "sc016147",
			"id": "404E9AB9-E015-1068-9CEB-F7C942FBF109"
		},
		{
			"etask.entity": "sc016149",
			"id": "15EEA7D5-5031-28DE-FC14-B1BF1B171690"
		},
		{
			"etask.entity": "sc016150",
			"id": "4AA01C9B-E8C9-7C56-4028-63E68FB54D8B"
		},
		{
			"etask.entity": "sc016151",
			"id": "759B420C-6CFC-44FD-44B6-280D5FB95380"
		},
		{
			"etask.entity": "sc016152",
			"id": "6CF8116C-D600-758A-CF09-068FA889AC9D"
		},
		{
			"etask.entity": "sc016153",
			"id": "57DD3AEC-8551-CCCD-EE63-4D551A1952AB"
		},
		{
			"etask.entity": "sc016154",
			"id": "21332A8F-364C-8356-1DE2-902F6430A464"
		},
		{
			"etask.entity": "sc016155",
			"id": "000AEC7E-C801-6B1E-8205-698B48473135"
		},
		{
			"etask.entity": "sc016156",
			"id": "63A61E0A-2C2D-7BF3-D384-D19CA79F743B"
		},
		{
			"etask.entity": "sc016157",
			"id": "4522706A-6E10-EC1F-185F-E453A81A3474"
		},
		{
			"etask.entity": "sc016158",
			"id": "AB34DDB5-FDF8-6A4C-D0E8-FEE61E04CF32"
		},
		{
			"etask.entity": "sc016159",
			"id": "18725A94-DD8A-74E7-53F4-46C02ECC978E"
		},
		{
			"etask.entity": "sc016160",
			"id": "4A6DC766-251B-F030-4867-993A26D065DA"
		},
		{
			"etask.entity": "sc016161",
			"id": "6FFDB7B2-F8EC-1102-C9B3-2395793F630A"
		},
		{
			"etask.entity": "sc016162",
			"id": "DF9C53BC-D8E2-33F9-4EFE-3383DE8EC69C"
		},
		{
			"etask.entity": "sc016163",
			"id": "66DECB94-7D1C-1BF3-C3E7-35D1A8CA6896"
		},
		{
			"etask.entity": "sc016164",
			"id": "C726F83E-0DBA-6E28-DCB2-C4DE17FBC0C8"
		},
		{
			"etask.entity": "sc016165",
			"id": "7B63BDFB-0DB2-60B0-9096-1A9253F8F9EB"
		},
		{
			"etask.entity": "sc016166",
			"id": "F1215629-6D80-F729-BEDC-0DD4CCCD3D1E"
		},
		{
			"etask.entity": "sc016167",
			"id": "82387FEE-EFE3-4BCB-D594-8C79366D9A95"
		},
		{
			"etask.entity": "sc016168",
			"id": "79A2A322-A85A-6E0C-03E3-4F33CF274C52"
		},
		{
			"etask.entity": "sc016169",
			"id": "672BDD62-7400-921B-89A2-10BFAC94D247"
		},
		{
			"etask.entity": "sc016170",
			"id": "BDFB8592-E322-7628-D562-3D666087F46E"
		},
		{
			"etask.entity": "sc016171",
			"id": "59160BB1-5B33-07CB-0411-80BB4361A9D8"
		},
		{
			"etask.entity": "sc016173",
			"id": "F56A2F46-D213-FF13-8F63-3608B95EC071"
		},
		{
			"etask.entity": "sc016174",
			"id": "9ECCF548-BAA1-DFB0-9ADF-34105F46BD15"
		},
		{
			"etask.entity": "sc016175",
			"id": "FE9CB9F7-60C5-451A-4DF0-8B7B80EA6D54"
		},
		{
			"etask.entity": "sc016176",
			"id": "8ED1456C-87A3-5AEE-BEB5-54EC31B14C5E"
		},
		{
			"etask.entity": "sc016177",
			"id": "23F0E3ED-4707-5039-42C3-C665E58DA681"
		},
		{
			"etask.entity": "sc016178",
			"id": "14D32525-E89A-00BA-1C12-498C24D1CFEE"
		},
		{
			"etask.entity": "sc016179",
			"id": "FAFD3E28-2A50-1202-1C3A-A1160252D8E9"
		},
		{
			"etask.entity": "sc016180",
			"id": "062DA1AE-8F88-120F-23D2-FBADC51F63C1"
		},
		{
			"etask.entity": "sc016181",
			"id": "759A26FC-A01E-5B39-4187-CFD382B98F76"
		},
		{
			"etask.entity": "sc016182",
			"id": "2A5A4CD1-61B8-DB44-58A2-099FA870AB0D"
		},
		{
			"etask.entity": "sc016183",
			"id": "938C82D3-06B7-082B-4EE1-07B17F1C4904"
		},
		{
			"etask.entity": "sc016184",
			"id": "53C7D8EE-58CC-2EBA-626D-EC6059AC8C4B"
		},
		{
			"etask.entity": "sc016185",
			"id": "DB0F910F-23EA-B337-F696-019DEAAA00AA"
		},
		{
			"etask.entity": "sc016187",
			"id": "29980329-357C-3ACC-6C52-A71867D39ABB"
		},
		{
			"etask.entity": "sc016188",
			"id": "0BD22423-DDCE-5D88-4CCA-5C413A1AF42C"
		},
		{
			"etask.entity": "sc016189",
			"id": "F6332106-97B4-36E6-FC3B-6CF94B94D504"
		},
		{
			"etask.entity": "sc016191",
			"id": "B10904EC-014D-B7B7-5CB4-722CDB237AC6"
		},
		{
			"etask.entity": "sc016192",
			"id": "28B809A3-29C8-2C95-D874-7B84F4738B8E"
		},
		{
			"etask.entity": "sc016194",
			"id": "C950EA1E-59ED-0DE7-EA20-E39D84CE83B0"
		},
		{
			"etask.entity": "sc016195",
			"id": "F7EE9CE6-10D0-6439-EDE3-E5956A21A726"
		},
		{
			"etask.entity": "sc016196",
			"id": "F7906569-8824-C171-06A0-1DBCB844934B"
		},
		{
			"etask.entity": "sc016197",
			"id": "450B1C51-1358-B1CD-7C24-10144494F2FA"
		},
		{
			"etask.entity": "sc016198",
			"id": "ED679F9C-C1FA-5207-FA02-13021408AF82"
		},
		{
			"etask.entity": "sc016199",
			"id": "B11CDAB7-0DA0-D86A-B268-D7D6A2F3EDF8"
		},
		{
			"etask.entity": "sc016200",
			"id": "2ED72751-71E9-C3DB-1DD3-229F3477DF17"
		},
		{
			"etask.entity": "sc016201",
			"id": "C1CA489F-A3D6-BC93-2221-0E961623D4A7"
		},
		{
			"etask.entity": "sc016202",
			"id": "35D1352A-31F9-CA37-FF86-11B724704123"
		},
		{
			"etask.entity": "sc016203",
			"id": "6814F935-A933-F690-7C8E-CA2CAB4B7B74"
		},
		{
			"etask.entity": "sc016204",
			"id": "694BEA59-2CBD-0D2F-6255-8F3D24A602A3"
		},
		{
			"etask.entity": "sc016205",
			"id": "8042B041-1FE2-D88B-52BE-3DFB99BC8946"
		},
		{
			"etask.entity": "sc016206",
			"id": "C61F463D-8752-71F6-BE31-CF0D587AABCC"
		},
		{
			"etask.entity": "sc016207",
			"id": "AE2AD71F-C692-47CA-A8BF-2CB47FEF8167"
		},
		{
			"etask.entity": "sc016208",
			"id": "5939043D-6AB8-A3E6-6DDD-7732AA643870"
		},
		{
			"etask.entity": "sc016209",
			"id": "E74D378D-06C2-38BB-C154-51E6DDD46735"
		},
		{
			"etask.entity": "sc016210",
			"id": "824ABD72-544E-A43A-B55C-0D46CAA50207"
		},
		{
			"etask.entity": "sc016211",
			"id": "B02142EB-302A-1254-A770-F03D1F6E3578"
		},
		{
			"etask.entity": "sc016212",
			"id": "13549B98-3D20-22DA-4452-DD71DE1FF8E0"
		},
		{
			"etask.entity": "sc016213",
			"id": "4532C941-D8C9-96F5-06A0-55C1CA0A92A2"
		},
		{
			"etask.entity": "sc016214",
			"id": "B1F12EAA-367D-9A0C-FB1C-4319E8ECC5D2"
		},
		{
			"etask.entity": "sc016215",
			"id": "F3B34047-CD50-EB83-939A-5092CC822F52"
		},
		{
			"etask.entity": "sc016216",
			"id": "81AC429D-DBF9-9D33-0FEE-FB7010816137"
		},
		{
			"etask.entity": "sc016218",
			"id": "E8C8004C-7280-DBFF-4892-1D14FC8F84FA"
		},
		{
			"etask.entity": "sc016219",
			"id": "EABB2E25-6D45-ED7A-1C24-498B227C5ECE"
		},
		{
			"etask.entity": "sc016220",
			"id": "05C8D802-7BCA-4399-D2BD-4AF3DAFEB401"
		},
		{
			"etask.entity": "sc016221",
			"id": "32B972CC-D4E5-7E46-5302-97EB446F4ABA"
		},
		{
			"etask.entity": "sc016222",
			"id": "659B24FE-B84D-12D2-7FAA-895891301F08"
		},
		{
			"etask.entity": "sc016223",
			"id": "E5C804C9-18EA-5E66-4D47-3FB3171AD9AE"
		},
		{
			"etask.entity": "sc016225",
			"id": "BFD9D617-CB29-8835-12BC-B45E9B75DC9E"
		},
		{
			"etask.entity": "sc016226",
			"id": "A78C5891-8637-DE63-CD82-0F5C98EDC9F6"
		},
		{
			"etask.entity": "sc016227",
			"id": "81E2E42C-C2F6-61D3-6282-13A9A95F38C1"
		},
		{
			"etask.entity": "sc016228",
			"id": "8F1ADA1C-88E3-8EED-B055-9B1DB1B51F69"
		},
		{
			"etask.entity": "sc016230",
			"id": "79581F73-B39D-E0E0-F52D-E3648E075BBC"
		},
		{
			"etask.entity": "sc016231",
			"id": "D960BF07-92F3-D066-D97F-62C121266E93"
		},
		{
			"etask.entity": "sc016232",
			"id": "105B624A-9EAC-F7D8-7AF6-A740AD64EB2A"
		},
		{
			"etask.entity": "sc016233",
			"id": "C4E30C15-5848-A18C-3C12-E7D5138FF4A6"
		},
		{
			"etask.entity": "sc016235",
			"id": "7650A47D-7B59-FA6B-E4F8-17EEDE05290F"
		},
		{
			"etask.entity": "sc016236",
			"id": "7F1805A2-5EF5-6444-E4BE-B24BBCCC5773"
		},
		{
			"etask.entity": "sc016237",
			"id": "4F0B505E-E3E9-4789-3DA8-4EB89BD7654B"
		},
		{
			"etask.entity": "sc016238",
			"id": "7E9822C9-B1D3-D899-E14C-EDCACE838F6A"
		},
		{
			"etask.entity": "sc016239",
			"id": "A77FB0B5-F701-59D7-DC27-B5A96A3222C0"
		},
		{
			"etask.entity": "sc016240",
			"id": "FAE3A56A-208A-3E8F-249C-B411010BE743"
		},
		{
			"etask.entity": "sc016241",
			"id": "F395EE86-D6CC-4A44-391C-D52169015B5C"
		},
		{
			"etask.entity": "sc016242",
			"id": "10593622-EAFC-DC34-C06E-184D0ABBBF5B"
		},
		{
			"etask.entity": "sc016243",
			"id": "D771DF6D-4789-C8AA-1640-74390DD93484"
		},
		{
			"etask.entity": "sc016244",
			"id": "1A8254DC-9396-8135-76D6-9B64BA8B0DC3"
		},
		{
			"etask.entity": "sc016245",
			"id": "041752AD-8C66-0082-1ABE-635ED3B24FA9"
		},
		{
			"etask.entity": "sc016246",
			"id": "D0ED700F-0AE0-4201-DEA3-6A5B0743C8DC"
		},
		{
			"etask.entity": "sc016247",
			"id": "B4F44F2F-1CA9-6EFD-1910-1D6209E0B619"
		},
		{
			"etask.entity": "sc016248",
			"id": "E6C67E4E-C5D9-3026-995C-711DE3FC3EE4"
		},
		{
			"etask.entity": "sc016249",
			"id": "73CF2E99-B5DF-4B3C-2F70-8D2589753EE3"
		},
		{
			"etask.entity": "sc016250",
			"id": "92D5425E-837F-7A40-24EF-42579B9F1059"
		},
		{
			"etask.entity": "sc016251",
			"id": "25C958F6-45B3-C178-BBD7-7BB03108A65F"
		},
		{
			"etask.entity": "sc016252",
			"id": "96AD22F3-D336-2491-0724-FA293E81F660"
		},
		{
			"etask.entity": "sc016253",
			"id": "039E4527-B421-E50E-FAD5-80D13E072C1D"
		},
		{
			"etask.entity": "sc016254",
			"id": "7739445C-5A59-EAC9-A9BB-E72DA226CAAD"
		},
		{
			"etask.entity": "sc016255",
			"id": "FA7EF125-9EFE-1988-D1AF-0A68D0AF23DF"
		},
		{
			"etask.entity": "sc016256",
			"id": "BAB0E4D0-10CB-11FC-4E98-69CAA4B2191C"
		},
		{
			"etask.entity": "sc016258",
			"id": "662C14B8-622D-D01E-B3F9-8FC7B7CD6AAF"
		},
		{
			"etask.entity": "sc016263",
			"id": "1FE77BD9-486B-7508-C2D9-0661777310AA"
		},
		{
			"etask.entity": "sc016269",
			"id": "3D1961B4-724C-596D-7AC8-85435C7434B6"
		},
		{
			"etask.entity": "sc016274",
			"id": "7B789CE3-FAD8-7082-7E09-17DE8F761D30"
		},
		{
			"etask.entity": "sc016279",
			"id": "2A8EA29A-F3E3-528A-16DC-3BBD39B1F0B6"
		},
		{
			"etask.entity": "sc016281",
			"id": "2BE5F831-000A-8592-05E2-20DF332E92E2"
		},
		{
			"etask.entity": "sc016283",
			"id": "29494B8A-B026-270B-2690-892CBB2A15C5"
		},
		{
			"etask.entity": "sc016285",
			"id": "575F7B7C-CEBA-274B-2B22-429C2C47A577"
		},
		{
			"etask.entity": "sc016286",
			"id": "F0543710-CFF7-7120-7C0E-80E907604D5A"
		},
		{
			"etask.entity": "sc016291",
			"id": "758A9AC4-F9CB-9640-1F48-840CBF717152"
		},
		{
			"etask.entity": "sc016296",
			"id": "6EA86412-DD8B-8872-07E9-287AEB7BA5FA"
		},
		{
			"etask.entity": "sc016301",
			"id": "A06A78DD-BE69-CC75-8649-61C6FCFEE4C0"
		},
		{
			"etask.entity": "sc016306",
			"id": "3DACE886-D810-1167-BF24-7827290D6694"
		},
		{
			"etask.entity": "sc016308",
			"id": "72C350AD-B692-E7FC-0813-E7E256225A6D"
		},
		{
			"etask.entity": "sc016313",
			"id": "7F219B98-842A-EBDA-8802-BD115A5D1530"
		},
		{
			"etask.entity": "sc016318",
			"id": "A06D895C-D6A4-BEE1-4884-FB33E2835CFA"
		},
		{
			"etask.entity": "sc016323",
			"id": "448C04ED-9718-1A07-66ED-311C87DE9824"
		},
		{
			"etask.entity": "sc016328",
			"id": "162F82E0-7191-48A4-2CFC-03D1C6E20D27"
		},
		{
			"etask.entity": "sc016330",
			"id": "E9A00CEB-FBFD-5629-81FB-91C9D231A930"
		},
		{
			"etask.entity": "sc016335",
			"id": "326B0B1B-E378-A959-77B4-0D1FFCFCAAC4"
		},
		{
			"etask.entity": "sc016340",
			"id": "92F6A896-EF01-3799-D9ED-70F05A8E2A48"
		},
		{
			"etask.entity": "sc016345",
			"id": "4EFC1C9F-2568-D80E-E10C-BF637F6DE7E9"
		},
		{
			"etask.entity": "sc016350",
			"id": "D36A0311-3ACF-295C-6702-C6231585CEEE"
		},
		{
			"etask.entity": "sc016352",
			"id": "F2C15646-8C68-ED31-89B0-5D3F57BE0953"
		},
		{
			"etask.entity": "sc016357",
			"id": "D483D9C0-A9CA-A3A6-6F56-A528E647B89C"
		},
		{
			"etask.entity": "sc016362",
			"id": "3EA6EBC5-ED24-61F4-4CC1-423402CD0B00"
		},
		{
			"etask.entity": "sc016367",
			"id": "DA56CD65-160A-33A4-4524-775D9583CA83"
		},
		{
			"etask.entity": "sc016372",
			"id": "BD9350BD-68EC-9B6D-6A0D-433FCF443CFD"
		},
		{
			"etask.entity": "sc016374",
			"id": "785ABAD9-A652-9917-C8DB-F2B477389EDF"
		},
		{
			"etask.entity": "sc016379",
			"id": "740C9A7C-0B54-025A-8047-52B55D05C43D"
		},
		{
			"etask.entity": "sc016384",
			"id": "5CB3EC05-E0D5-102A-CF2D-696B52B4EC48"
		},
		{
			"etask.entity": "sc016389",
			"id": "FFB9C0FA-A638-FC3B-56B4-84ED750E19A0"
		},
		{
			"etask.entity": "sc016394",
			"id": "9E504817-6310-9C0F-2799-94C59BC7D416"
		},
		{
			"etask.entity": "sc016396",
			"id": "B6CB3083-6B81-E307-56EE-E3B849EBC7A6"
		},
		{
			"etask.entity": "sc016401",
			"id": "DAEA6256-D6AC-5839-DE19-AB2BFD03F10B"
		},
		{
			"etask.entity": "sc016406",
			"id": "BE54A650-966E-ABAA-4BCE-EE47804CD87F"
		},
		{
			"etask.entity": "sc016411",
			"id": "80112946-E28F-A7CC-F896-E306A9EEACFE"
		},
		{
			"etask.entity": "sc016416",
			"id": "4218F1C7-78A0-03D8-F895-AC4EBBADC3D9"
		},
		{
			"etask.entity": "sc016418",
			"id": "670E1DD3-BD71-B6A4-27CD-819DA4977891"
		},
		{
			"etask.entity": "sc016423",
			"id": "84DC452D-9BFB-E6AE-2B9A-57D420B585CA"
		},
		{
			"etask.entity": "sc016428",
			"id": "F9F1E02B-ECB3-DE55-C2DC-48E92B5266AE"
		},
		{
			"etask.entity": "sc016433",
			"id": "2135D8EA-B3F9-D3B4-8E23-8BAD996E9B78"
		},
		{
			"etask.entity": "sc016438",
			"id": "9075E3CD-A5BA-4184-D55D-4CEF25C5D160"
		},
		{
			"etask.entity": "sc016440",
			"id": "B02731FC-48A8-B403-56FB-7483D7CA0D89"
		},
		{
			"etask.entity": "sc016445",
			"id": "61C9EB68-82F0-4335-2621-8E398E63767C"
		},
		{
			"etask.entity": "sc016450",
			"id": "ED254225-B0B4-29DA-5934-3F4384C96353"
		},
		{
			"etask.entity": "sc016455",
			"id": "FA143DBD-8EEC-98C5-FA81-256413C57545"
		},
		{
			"etask.entity": "sc016460",
			"id": "32AD7450-2BDA-05F7-9562-B06AD5F93FD4"
		},
		{
			"etask.entity": "sc016462",
			"id": "799C41DA-1C63-4C64-FA2F-F6ACA19A5552"
		},
		{
			"etask.entity": "sc016467",
			"id": "9007DBB8-C2A1-342B-5F3E-941FB43F8FBD"
		},
		{
			"etask.entity": "sc016472",
			"id": "561F7B9A-C471-EB70-9479-CDC8B7AEF547"
		},
		{
			"etask.entity": "sc016477",
			"id": "A4A4CA77-E449-6942-EE93-6A771C0C8560"
		},
		{
			"etask.entity": "sc016482",
			"id": "2019661C-229D-7044-42D3-31B9A02FD782"
		},
		{
			"etask.entity": "sc016484",
			"id": "6987044E-C901-68B9-204F-414D2240B110"
		},
		{
			"etask.entity": "sc016489",
			"id": "C67FC23C-C215-A0DB-9FEF-1DF5DB386A45"
		},
		{
			"etask.entity": "sc016494",
			"id": "470FCA2A-C0C5-F3DB-F219-41C5035D837C"
		},
		{
			"etask.entity": "sc016499",
			"id": "2FC0E506-F35E-E57D-124B-88CA6555F2D2"
		},
		{
			"etask.entity": "sc016504",
			"id": "A842E8D9-7CDA-E075-C47D-AC1318AE575D"
		},
		{
			"etask.entity": "sc016506",
			"id": "5B52FA38-EAE4-5260-1A83-D48ED06604F3"
		},
		{
			"etask.entity": "sc016511",
			"id": "0203BF49-6564-4DF6-A2B5-E08F9C4F3B10"
		},
		{
			"etask.entity": "sc016516",
			"id": "22F31B87-9CD8-1000-32BB-780214B7F1AA"
		},
		{
			"etask.entity": "sc016521",
			"id": "0FD262A3-5C21-BFFD-3FC3-858E982D03E1"
		},
		{
			"etask.entity": "sc016526",
			"id": "F7CE269A-EC2D-30C6-E49D-F5822B5DEE3B"
		},
		{
			"etask.entity": "sc016528",
			"id": "01CCC9B9-59D6-B888-75A8-58381ADFC6EC"
		},
		{
			"etask.entity": "sc016533",
			"id": "D4F9C837-7BFB-36A3-6927-1D0D7C8A102C"
		},
		{
			"etask.entity": "sc016538",
			"id": "78ED7BFD-FB27-4612-93C2-760AACFD454A"
		},
		{
			"etask.entity": "sc016543",
			"id": "DF943EBD-39E1-9E60-089C-351A16CD4B38"
		},
		{
			"etask.entity": "sc016548",
			"id": "03AE9DDF-A026-C4D6-13DC-AC793133E747"
		},
		{
			"etask.entity": "sc016550",
			"id": "3433357E-88B9-1C7A-8E53-5B000ECFE680"
		},
		{
			"etask.entity": "sc016555",
			"id": "3130D34C-4DE9-C0C1-EC9C-2F7531D9E28F"
		},
		{
			"etask.entity": "sc016560",
			"id": "FA73C7E0-D81A-B6A3-B102-9F57812760EE"
		},
		{
			"etask.entity": "sc016565",
			"id": "8A26E47B-0ED5-F272-6AF3-946ACC3D8546"
		},
		{
			"etask.entity": "sc016570",
			"id": "B58C3F38-BBCD-4CB0-7EF6-350867F7C721"
		},
		{
			"etask.entity": "sc016572",
			"id": "24DACEB5-88BA-4EA2-6FB1-A90E41722B1B"
		},
		{
			"etask.entity": "sc016577",
			"id": "A497035D-D363-CC7F-3BC1-2D7928B30927"
		},
		{
			"etask.entity": "sc016582",
			"id": "07A5D28C-CA2A-B4A4-463D-4E8F35A0D2CA"
		},
		{
			"etask.entity": "sc016587",
			"id": "7A59B64E-03EC-8948-AA71-D172766AE47F"
		},
		{
			"etask.entity": "sc016592",
			"id": "37DC7B09-E488-D30A-1811-033DD5E5EE56"
		},
		{
			"etask.entity": "sc016594",
			"id": "605466CB-BD8E-DECE-9DA0-31E304112188"
		},
		{
			"etask.entity": "sc016599",
			"id": "FF8E3283-6C0B-D103-5D03-449E25FF45A5"
		},
		{
			"etask.entity": "sc016604",
			"id": "81C48E99-B5A3-AD5E-B690-C73DD50B0656"
		},
		{
			"etask.entity": "sc016609",
			"id": "E3FE93C9-A695-187F-000F-639B37D78506"
		},
		{
			"etask.entity": "sc016614",
			"id": "6F76F8F5-C1E6-8407-D968-75140EDA4ED1"
		},
		{
			"etask.entity": "sc016616",
			"id": "40624E28-D1DB-169A-E7AF-C009E09F484B"
		},
		{
			"etask.entity": "sc016621",
			"id": "46EBE61F-B6B3-E22D-668E-B66B6176A188"
		},
		{
			"etask.entity": "sc016626",
			"id": "83B46538-E70C-CB2F-E628-947A9E396189"
		},
		{
			"etask.entity": "sc016631",
			"id": "04FBE404-18FE-C9A9-B51A-A1231158F8F3"
		},
		{
			"etask.entity": "sc016636",
			"id": "3BD28909-CC42-B6F9-7B0E-BDB87B2F2675"
		},
		{
			"etask.entity": "sc016638",
			"id": "46F4B776-BAD7-B4C4-E560-964B42B1C72B"
		},
		{
			"etask.entity": "sc016643",
			"id": "F529963C-E6B2-571F-4972-60DB8A51C578"
		},
		{
			"etask.entity": "sc016648",
			"id": "28870E69-2AF1-4444-AEDB-C158ED66C05B"
		},
		{
			"etask.entity": "sc016653",
			"id": "2DAF38C8-ADA3-9BCE-0040-B26CCAE2B15E"
		},
		{
			"etask.entity": "sc016658",
			"id": "D6FDFE3A-06FF-0339-0F31-801E1AEC175C"
		},
		{
			"etask.entity": "sc016660",
			"id": "EC548CF8-5D11-6AAA-6EDC-AFB52CE8C59F"
		},
		{
			"etask.entity": "sc016665",
			"id": "41D7A7C7-7DE9-4E5F-E8E3-E79120C15B0F"
		},
		{
			"etask.entity": "sc016670",
			"id": "91CBEE2B-78B7-AB69-AF21-7B68D05E7696"
		},
		{
			"etask.entity": "sc016675",
			"id": "D95E5742-AE90-4A42-E92A-8BDA9B95421D"
		},
		{
			"etask.entity": "sc016680",
			"id": "FA0AD3D5-EB33-5154-E6C4-0ECFEDCDC3A2"
		},
		{
			"etask.entity": "sc016682",
			"id": "B46C8D3E-6ED8-15F8-CD63-6526FF7DE991"
		},
		{
			"etask.entity": "sc016687",
			"id": "EA3C604E-62F7-874A-7919-279FE8B58CBB"
		},
		{
			"etask.entity": "sc016692",
			"id": "68DADE16-44FF-CCF5-8F0F-B9CBC69E4E51"
		},
		{
			"etask.entity": "sc016697",
			"id": "7CAC3739-3778-5D4A-26A3-5E27A9C668D5"
		},
		{
			"etask.entity": "sc016702",
			"id": "0C5D8E76-310B-0F63-4F46-C56B58B6CBF5"
		},
		{
			"etask.entity": "sc016704",
			"id": "8FBD19C2-F195-3F85-6DD4-C596608C268C"
		},
		{
			"etask.entity": "sc016709",
			"id": "BAEEFF09-3310-88BD-E60F-31262FF69A3E"
		},
		{
			"etask.entity": "sc016714",
			"id": "04BAAC04-773A-544D-8219-CC12DB95B113"
		},
		{
			"etask.entity": "sc016719",
			"id": "CCE0CE5A-9A49-1416-754E-6DADA92C6133"
		},
		{
			"etask.entity": "sc016724",
			"id": "CB690B47-BC68-0BF1-B888-374463FD876F"
		},
		{
			"etask.entity": "sc016726",
			"id": "9674A364-B674-37E3-6785-3CEE32885B27"
		},
		{
			"etask.entity": "sc016731",
			"id": "B4DDD6DD-BAF6-CBE2-B9CC-79299E3C81FC"
		},
		{
			"etask.entity": "sc016736",
			"id": "798FDC61-1652-AF32-DFDC-F60672F87921"
		},
		{
			"etask.entity": "sc016741",
			"id": "7BE1E675-A0E5-37E2-EED5-859305289C3E"
		},
		{
			"etask.entity": "sc016746",
			"id": "6741EDDD-12D1-A17D-9B42-0689F05E6B30"
		},
		{
			"etask.entity": "sc016748",
			"id": "459FC016-23E0-8543-C713-DDE6CEFC88B1"
		},
		{
			"etask.entity": "sc016753",
			"id": "D10DCCE4-95D6-5815-9C36-3446D64BBC8F"
		},
		{
			"etask.entity": "sc016758",
			"id": "3F22F897-FB5A-C083-BA41-C221880C6420"
		},
		{
			"etask.entity": "sc016763",
			"id": "DC86ACFF-DD11-2306-7025-F6B200B7FF48"
		},
		{
			"etask.entity": "sc016768",
			"id": "D757C6E5-9C3F-0F63-E000-80A30954D4C5"
		},
		{
			"etask.entity": "sc016770",
			"id": "F00E4D16-21F6-B180-73F7-2D34369372C9"
		},
		{
			"etask.entity": "sc016775",
			"id": "F30E5CB7-BEC8-B0AD-7744-A85A36BD7654"
		},
		{
			"etask.entity": "sc016780",
			"id": "B7143AD1-1E60-670C-7056-CB81AEB7374E"
		},
		{
			"etask.entity": "sc016785",
			"id": "B01F9D44-449C-94DC-38B0-D0B1526E3E94"
		},
		{
			"etask.entity": "sc016790",
			"id": "272A1F79-AB79-39C4-9EA0-36F107BFB51A"
		},
		{
			"etask.entity": "sc016792",
			"id": "FFF65D5E-3DC1-D3E8-4D33-074AA264798D"
		},
		{
			"etask.entity": "sc016797",
			"id": "CA2043F9-D107-3C1E-CD78-9B0AA3909BAA"
		},
		{
			"etask.entity": "sc016802",
			"id": "743AB3FD-D075-A704-6CB5-33C200A0AD25"
		},
		{
			"etask.entity": "sc016807",
			"id": "14D40304-4EC1-2CB7-8E45-8FB38F7A49DF"
		},
		{
			"etask.entity": "sc016809",
			"id": "628C803A-24D9-E55B-B1DC-ADB2F8C4B3C7"
		},
		{
			"etask.entity": "sc016810",
			"id": "D1B7072B-26D0-FD02-AF77-0B3328617FF0"
		},
		{
			"etask.entity": "sc016814",
			"id": "46CE69F2-5787-23DD-977D-1C06F6C109A1"
		},
		{
			"etask.entity": "sc016819",
			"id": "38AFFA6D-4C9F-E5BE-F58A-AD0D77D8BE2C"
		},
		{
			"etask.entity": "sc016824",
			"id": "48376F95-5955-DA88-ED29-D83A48BF4312"
		},
		{
			"etask.entity": "sc016829",
			"id": "3348CC13-A6F3-E0A1-313D-29EF18E109D7"
		},
		{
			"etask.entity": "sc016834",
			"id": "0AD1CA09-B696-11C1-26E1-80D8DD7844BA"
		},
		{
			"etask.entity": "sc016836",
			"id": "CCF7E7AC-EC54-6750-C013-E9C3E81DB911"
		},
		{
			"etask.entity": "sc016841",
			"id": "526DFE77-807C-0CA1-13A8-AE92C73B41D2"
		},
		{
			"etask.entity": "sc016842",
			"id": "CA547B80-9B3F-B680-3E4F-55E6C17BB505"
		},
		{
			"etask.entity": "sc016851",
			"id": "5D68B1B5-8172-18F7-69D4-A0FB10B78EB0"
		},
		{
			"etask.entity": "sc016856",
			"id": "994B3AF5-93D8-A294-0EEF-FD99D98107D9"
		},
		{
			"etask.entity": "sc016858",
			"id": "73472BC3-253C-B9AB-351A-C25388087A5B"
		},
		{
			"etask.entity": "sc016863",
			"id": "45713E1C-D72A-57E6-0DE0-E9328F122A9C"
		},
		{
			"etask.entity": "sc016868",
			"id": "4D5D3DD3-890E-4269-E405-5C83154CF191"
		},
		{
			"etask.entity": "sc016870",
			"id": "6A81725E-96F3-20A7-EFED-91573426B96F"
		},
		{
			"etask.entity": "sc016871",
			"id": "B44491D6-6BBC-D2FD-8DF2-C4DF78F48D8E"
		},
		{
			"etask.entity": "sc016880",
			"id": "E560577E-73AC-982B-8F4B-DCAC6F2BDD74"
		},
		{
			"etask.entity": "sc016885",
			"id": "833398BF-9559-A9D7-1600-254FB38530B1"
		},
		{
			"etask.entity": "sc016890",
			"id": "40223F67-EBAE-CBFC-97AC-91412BF9DA4C"
		},
		{
			"etask.entity": "sc016894",
			"id": "3002AB4C-7380-3C02-0527-BE26BF1EFCD1"
		},
		{
			"etask.entity": "sc016895",
			"id": "BE889157-3B6F-0FA5-315F-653D4A3F970A"
		},
		{
			"etask.entity": "sc016902",
			"id": "17E247EE-8D28-A489-9F3F-47A799AB245D"
		},
		{
			"etask.entity": "sc016907",
			"id": "C29562A8-562C-6CF3-1DC6-5382F7FABEDE"
		},
		{
			"etask.entity": "sc016912",
			"id": "46920CEC-9D61-6E14-0162-1FF96C49D738"
		},
		{
			"etask.entity": "sc016917",
			"id": "666210D2-1414-0DE4-E04B-3F054E3A48EC"
		},
		{
			"etask.entity": "sc016919",
			"id": "9EE4A49C-578E-93CF-F82B-7D381FCC7BB4"
		},
		{
			"etask.entity": "sc016924",
			"id": "460D16D4-1CE3-F8BB-2B85-0E5D616F938B"
		},
		{
			"etask.entity": "sc016929",
			"id": "76287DE1-F1D3-E14A-911D-75B7DC4621E3"
		},
		{
			"etask.entity": "sc016934",
			"id": "F9069F45-16FD-2456-088D-08E4D20B1AE3"
		},
		{
			"etask.entity": "sc016939",
			"id": "5903A29D-05ED-DB96-312E-D16E64D4FA01"
		},
		{
			"etask.entity": "sc016940",
			"id": "0C6F7C75-9B74-2B92-89B1-19E21B31412A"
		},
		{
			"etask.entity": "sc016941",
			"id": "738F2A8D-6E27-3568-D2D7-DA0A2B440539"
		},
		{
			"etask.entity": "sc016946",
			"id": "1605E800-20B3-7594-0FDA-D04913764171"
		},
		{
			"etask.entity": "sc016951",
			"id": "7A18BC65-DEF7-4171-A06B-BC67835FC5B8"
		},
		{
			"etask.entity": "sc016956",
			"id": "D4C3D944-3F25-A5BC-8576-0E382BE596A6"
		},
		{
			"etask.entity": "sc016958",
			"id": "B80F441F-0F98-7F63-219F-0611FFAACFE3"
		},
		{
			"etask.entity": "sc016959",
			"id": "0923EF1D-C250-7D26-7D28-FBC89B5D9AC9"
		},
		{
			"etask.entity": "sc016968",
			"id": "00348597-2EA6-1D5B-DDE1-82BDC8B79F71"
		},
		{
			"etask.entity": "sc016973",
			"id": "79655213-54CC-FFDF-AF05-C1AD331C19DF"
		},
		{
			"etask.entity": "sc016976",
			"id": "43C2BA89-67C2-87A5-F496-8BD2BD45E822"
		},
		{
			"etask.entity": "sc016977",
			"id": "C9C01E54-E8D3-B212-A4EE-10CA3E2DC2E4"
		},
		{
			"etask.entity": "sc016988",
			"id": "BAC835DB-648B-62E0-9B58-06F3679E681A"
		},
		{
			"etask.entity": "sc016990",
			"id": "1350EE28-60AD-DAEA-02F8-F7F86D53D5F5"
		},
		{
			"etask.entity": "sc016994",
			"id": "00885426-7EA1-5311-069C-AED8445D629E"
		},
		{
			"etask.entity": "sc016995",
			"id": "2D1237D9-B648-EB71-A3FA-D2A7D0E360E2"
		},
		{
			"etask.entity": "sc017004",
			"id": "E5CDF8D8-CAB1-E5B7-2F36-4B6B4A82F43B"
		},
		{
			"etask.entity": "sc017010",
			"id": "95154A55-1AB4-1FB6-F124-5DE62F6FFCE7"
		},
		{
			"etask.entity": "sc017012",
			"id": "232740A0-F154-BFBB-725A-09563C9D4FE8"
		},
		{
			"etask.entity": "sc017015",
			"id": "98009570-F86B-88A8-6BD9-89332B66286A"
		},
		{
			"etask.entity": "sc017016",
			"id": "AF7E851E-C919-CD81-A359-B1E03C0735EB"
		},
		{
			"etask.entity": "sc017027",
			"id": "19F3C4C2-99EE-1EAC-3AC6-98AE53406715"
		},
		{
			"etask.entity": "sc017029",
			"id": "EF58ED80-40D4-8C98-A47E-2FA74F6BDF68"
		},
		{
			"etask.entity": "sc017034",
			"id": "1AFC40A5-24FC-5785-C18E-60A513903681"
		},
		{
			"etask.entity": "sc017039",
			"id": "632B0E25-13C5-931E-F45A-D8210FDFB9C2"
		},
		{
			"etask.entity": "sc017043",
			"id": "E0BBBFC2-092E-7F2C-F186-F53896AA0D1E"
		},
		{
			"etask.entity": "sc017044",
			"id": "6DD76270-ED0E-CC36-EADA-2311A53CDEEF"
		},
		{
			"etask.entity": "sc017054",
			"id": "9D4BEED5-A714-4818-2EA4-514EA487D0EC"
		},
		{
			"etask.entity": "sc017056",
			"id": "04B149FA-018F-B284-744F-90307EF645BF"
		},
		{
			"etask.entity": "sc017061",
			"id": "1BA3859D-2809-2D6B-CA6D-E17644FCFD6D"
		},
		{
			"etask.entity": "sc017066",
			"id": "57B65BC8-E86A-C2C8-8925-58678F136E64"
		},
		{
			"etask.entity": "sc017071",
			"id": "0A3A65F2-D873-7F92-5BAE-D1B3763C2339"
		},
		{
			"etask.entity": "sc017076",
			"id": "8DB10BFB-9B8F-2826-660B-53D85BB1B6F5"
		},
		{
			"etask.entity": "sc017078",
			"id": "8605DBA0-DB3C-97F0-9B73-96DDEC1C1B63"
		},
		{
			"etask.entity": "sc017083",
			"id": "2790AAB0-67BF-35F7-F380-A859F930966E"
		},
		{
			"etask.entity": "sc017088",
			"id": "6FACE5D5-C4A9-B38C-9A85-22FC4E5EAAC8"
		},
		{
			"etask.entity": "sc017093",
			"id": "A1A033BB-86EB-D79C-2126-D4404C6ACBA2"
		},
		{
			"etask.entity": "sc017098",
			"id": "EA1186C7-3395-4924-519A-82EFFFD8429F"
		},
		{
			"etask.entity": "sc017100",
			"id": "4C7E51B5-0991-41D0-92E2-DBBBFC50DFC3"
		},
		{
			"etask.entity": "sc017105",
			"id": "87AD3D1B-AA97-2282-FF2A-9DBF803B4693"
		},
		{
			"etask.entity": "sc017110",
			"id": "B32EA431-2D59-F9EE-E4C8-22CA62B9BE9D"
		},
		{
			"etask.entity": "sc017115",
			"id": "3F101ECE-E7A9-BD45-2D4C-6E7828E2D26C"
		},
		{
			"etask.entity": "sc017120",
			"id": "6844AB74-8684-0154-BB46-06BE35490BA7"
		},
		{
			"etask.entity": "sc017122",
			"id": "6BB7E03B-D794-9C50-35D1-3629F2934042"
		},
		{
			"etask.entity": "sc017127",
			"id": "9E962D94-076E-F6C7-E548-C34336886393"
		},
		{
			"etask.entity": "sc017132",
			"id": "72903120-BB66-235F-8483-486C4BA6C116"
		},
		{
			"etask.entity": "sc017137",
			"id": "61835B2E-6A9D-B3E3-581A-54E5D1411F4F"
		},
		{
			"etask.entity": "sc017142",
			"id": "4AED2F48-6D80-C5B3-E794-24871C3B5209"
		},
		{
			"etask.entity": "sc017144",
			"id": "A88C09A3-27F2-3577-229D-E1AF262790B2"
		},
		{
			"etask.entity": "sc017149",
			"id": "D567A356-DB90-5D43-44D9-3858B12DC817"
		},
		{
			"etask.entity": "sc017154",
			"id": "AD070B5B-815C-514F-661B-0BC1F045C54F"
		},
		{
			"etask.entity": "sc017159",
			"id": "089B53EB-D94E-36FE-C8A0-5923CA764D5C"
		},
		{
			"etask.entity": "sc017164",
			"id": "31000975-F3E3-43D7-62E6-994CB1EBF68C"
		},
		{
			"etask.entity": "sc017166",
			"id": "6A7CCFAC-5A86-B204-5306-D0E30555C58B"
		},
		{
			"etask.entity": "sc017171",
			"id": "9CA08698-9071-8DCC-AADE-99275731B9DE"
		},
		{
			"etask.entity": "sc017176",
			"id": "9B897DD8-D07C-8F4D-B713-3466A83B5CCA"
		},
		{
			"etask.entity": "sc017181",
			"id": "E9B1C2F0-1E96-BAB0-2BC0-167464725E6A"
		},
		{
			"etask.entity": "sc017186",
			"id": "39DA80E5-1A2C-54A6-0E12-65D70DD2F805"
		},
		{
			"etask.entity": "sc017188",
			"id": "098CD760-58DE-975D-C823-E87B7DA39EB6"
		},
		{
			"etask.entity": "sc017193",
			"id": "A0468D84-417A-801E-12EF-4D6A75460E63"
		},
		{
			"etask.entity": "sc017198",
			"id": "FE66C438-2CA1-082A-6F58-F956A6C551DD"
		},
		{
			"etask.entity": "sc017203",
			"id": "74C248FC-F6EC-465D-59E9-CABAFC28BE28"
		},
		{
			"etask.entity": "sc017208",
			"id": "6D9E5E50-4DC8-48A3-E78B-75158CD4135C"
		},
		{
			"etask.entity": "sc017210",
			"id": "EFEF0DD3-CBB1-76F3-F5E4-18FDD938F9A1"
		},
		{
			"etask.entity": "sc017215",
			"id": "C359BD81-886F-3D74-01E7-2D9D0CE7014D"
		},
		{
			"etask.entity": "sc017220",
			"id": "CCAB2CAB-CD66-8100-8AA0-FFB0AEBC5211"
		},
		{
			"etask.entity": "sc017225",
			"id": "6F6CE028-7B73-B3BF-87B7-7A1CD2C45F68"
		},
		{
			"etask.entity": "sc017230",
			"id": "13FF33CB-F658-6EAC-4743-E7E62AEE26AE"
		},
		{
			"etask.entity": "sc017232",
			"id": "EA587B48-72DB-1F67-60F6-A067BE0B6D30"
		},
		{
			"etask.entity": "sc017237",
			"id": "D7ACCC87-5066-8CF5-A3E7-ABAF38471625"
		},
		{
			"etask.entity": "sc017242",
			"id": "7E75EDE1-46DE-A6EE-3BFD-2FD74E8D7BAE"
		},
		{
			"etask.entity": "sc017247",
			"id": "AD46EF0E-2C83-732F-5610-894BBE05C0E0"
		},
		{
			"etask.entity": "sc017252",
			"id": "DB08CC66-FEB1-7635-F4F8-B481FDAC8C7B"
		},
		{
			"etask.entity": "sc017254",
			"id": "3F8BDFF9-58D2-F9AC-CB33-28E7D8877173"
		},
		{
			"etask.entity": "sc017259",
			"id": "292D380A-D611-D89E-9507-A32B2BFE0D0B"
		},
		{
			"etask.entity": "sc017264",
			"id": "C4AECB28-56B2-EEEF-9A5E-539190E15162"
		},
		{
			"etask.entity": "sc017269",
			"id": "A4CDB03C-ED0A-95AD-892B-0CBB4EFC28EC"
		},
		{
			"etask.entity": "sc017274",
			"id": "9AAF6C73-871D-D515-8115-C96035C47FDF"
		},
		{
			"etask.entity": "sc017276",
			"id": "01C1A48A-F743-F988-7CC3-3377E0FD4E3A"
		},
		{
			"etask.entity": "sc017281",
			"id": "FA3BD74B-35A5-434C-C0EF-8433342847D0"
		},
		{
			"etask.entity": "sc017286",
			"id": "14D04CA2-D3E5-9DDA-4049-0A7BB2BF9FC6"
		},
		{
			"etask.entity": "sc017291",
			"id": "D7A371F7-7BB7-5433-16EF-64ACF35E29E4"
		},
		{
			"etask.entity": "sc017296",
			"id": "18A89D50-2005-28B7-2153-18F413FC5681"
		},
		{
			"etask.entity": "sc017298",
			"id": "FB89E5A2-1EA9-5C88-6FEF-EBFCE7410FC0"
		},
		{
			"etask.entity": "sc017303",
			"id": "0BAD8A9E-5AFA-FF50-FCFF-138A0068736B"
		},
		{
			"etask.entity": "sc017308",
			"id": "9870657D-27C5-6DE3-2FD1-E46220A0664B"
		},
		{
			"etask.entity": "sc017313",
			"id": "C5E05CFB-E379-C482-E50B-05A6CDFB462F"
		},
		{
			"etask.entity": "sc017318",
			"id": "0CD19753-3DB2-5202-6E2E-0508FFCC6F87"
		},
		{
			"etask.entity": "sc017320",
			"id": "7584FCEF-7E56-BF44-31B9-A48A5CA85907"
		},
		{
			"etask.entity": "sc017325",
			"id": "EE460C32-AC5A-64EC-58B3-57F71EA133A3"
		},
		{
			"etask.entity": "sc017330",
			"id": "C95752A5-D7E8-5501-C934-18AB2F1002B5"
		},
		{
			"etask.entity": "sc017335",
			"id": "EE988152-585C-E85A-D9A3-9E65C8B8FAC2"
		},
		{
			"etask.entity": "sc017340",
			"id": "000C165E-0262-411C-EB8E-C7C8D14129B1"
		},
		{
			"etask.entity": "sc017342",
			"id": "E0BF57D8-27DD-E3C5-4F85-FD663B0459CA"
		},
		{
			"etask.entity": "sc017347",
			"id": "95A87F37-1B6D-D7F6-1998-8587F40B8166"
		},
		{
			"etask.entity": "sc017352",
			"id": "70FE2C14-315B-5660-4F5A-4FC4886296E7"
		},
		{
			"etask.entity": "sc017357",
			"id": "B4E6EE35-8839-40A9-3D66-FEAAFFA909E9"
		},
		{
			"etask.entity": "sc017362",
			"id": "ECDDB417-D990-071A-341C-247D91844A39"
		},
		{
			"etask.entity": "sc017364",
			"id": "97E563D7-65A6-1582-7F18-DE3F69B84DBB"
		},
		{
			"etask.entity": "sc017369",
			"id": "A750B997-62B3-EA85-628A-6508364580F4"
		},
		{
			"etask.entity": "sc017374",
			"id": "FC39AF6A-99C1-D887-3B0B-515992C0006A"
		},
		{
			"etask.entity": "sc017379",
			"id": "69AE8B51-0DCD-C324-2313-AF9A34C09D82"
		},
		{
			"etask.entity": "sc017384",
			"id": "7DD37AB2-6E3B-6D04-91DD-2EF892AD3BE6"
		},
		{
			"etask.entity": "sc017386",
			"id": "A6D8FBAD-2E32-471A-3A48-D32454395261"
		},
		{
			"etask.entity": "sc017391",
			"id": "493139C0-C066-91C7-13CA-BE69B5201F84"
		},
		{
			"etask.entity": "sc017396",
			"id": "C695CB31-AD81-0E71-9C8D-26277FC86BC1"
		},
		{
			"etask.entity": "sc017401",
			"id": "0EAB4C7F-DDC6-248B-6310-80C1CB3E5930"
		},
		{
			"etask.entity": "sc017406",
			"id": "8886D632-02C2-503A-5FFD-B32047B9AFA1"
		},
		{
			"etask.entity": "sc017408",
			"id": "5D1A3D85-C8B3-05D6-79B6-9A35A8D56A18"
		},
		{
			"etask.entity": "sc017413",
			"id": "BF958590-E4E0-43F6-67FA-1BB27708C459"
		},
		{
			"etask.entity": "sc017418",
			"id": "F1DD6ACB-F4E2-4046-8024-3126744EE6EF"
		},
		{
			"etask.entity": "sc017423",
			"id": "8CDEF98D-50E5-5D1F-6CD3-E2AD196F1C90"
		},
		{
			"etask.entity": "sc017428",
			"id": "E1100FBB-A3E8-E1B3-8CC6-2B496A1B8DF0"
		},
		{
			"etask.entity": "sc017430",
			"id": "C973D9A5-9DF7-224F-FABB-C07B2A665107"
		},
		{
			"etask.entity": "sc017435",
			"id": "5576AE22-51DF-C9FA-8E47-5AB416F12283"
		},
		{
			"etask.entity": "sc017440",
			"id": "6CF7F82B-72B1-907C-8555-B639E579F46D"
		},
		{
			"etask.entity": "sc017445",
			"id": "4CE50C0F-6A37-AB97-1A00-95663C5355FE"
		},
		{
			"etask.entity": "sc017450",
			"id": "26779315-FFA0-9B33-6EA9-23C64B3E4700"
		},
		{
			"etask.entity": "sc017452",
			"id": "DB4F6BAE-D9C9-38BE-176A-6E92E2C8EEE3"
		},
		{
			"etask.entity": "sc017457",
			"id": "35DAD9EB-F7C6-33B0-DF83-5DDF56D86969"
		},
		{
			"etask.entity": "sc017462",
			"id": "2B57A6A8-09B9-73E8-1AFA-4607FD4B3AF3"
		},
		{
			"etask.entity": "sc017467",
			"id": "44003408-7B02-211B-7877-15A222A26D95"
		},
		{
			"etask.entity": "sc017472",
			"id": "963670D6-FC8F-4368-FE3D-BDBFEED88FE0"
		},
		{
			"etask.entity": "sc017474",
			"id": "3ABB47ED-3ABD-A7F7-9E83-568F3FA22E38"
		},
		{
			"etask.entity": "sc017479",
			"id": "EAB755D1-B119-3AFB-CC0D-00182A43CD8B"
		},
		{
			"etask.entity": "sc017484",
			"id": "EB65DBA3-2A4B-E9C5-24AB-ECD5373A329F"
		},
		{
			"etask.entity": "sc017489",
			"id": "7789C9B6-EAF3-33A7-711E-20094328D010"
		},
		{
			"etask.entity": "sc017494",
			"id": "4B60B92D-03A2-3E60-FD56-A5F0ECCC8044"
		},
		{
			"etask.entity": "sc017496",
			"id": "01313ECA-89E1-5C44-B734-15AB86C69F60"
		},
		{
			"etask.entity": "sc017501",
			"id": "7198A312-155F-5B93-55F7-478497EDCEE5"
		},
		{
			"etask.entity": "sc017506",
			"id": "CDC99AAB-5EFB-9998-91A9-68110D7B97CA"
		},
		{
			"etask.entity": "sc017511",
			"id": "BEF30B0F-064A-173B-BDFA-64D8E36FDB2B"
		},
		{
			"etask.entity": "sc017516",
			"id": "57C1E93F-210B-DF0C-1331-224385405ACC"
		},
		{
			"etask.entity": "sc017518",
			"id": "BF1B5D2C-B153-42E2-8524-CB2EC7FAC19E"
		},
		{
			"etask.entity": "sc017523",
			"id": "609F9EFC-0B71-1AE0-1237-DFAF645D1305"
		},
		{
			"etask.entity": "sc017528",
			"id": "60519ABF-4EB8-A49E-F6C0-C66DE5DFFFB7"
		},
		{
			"etask.entity": "sc017533",
			"id": "41554B45-266B-A816-8CD8-4EC5B692A22A"
		},
		{
			"etask.entity": "sc017538",
			"id": "AE4DB396-C4A6-5FD6-FE9E-52A6E2B94617"
		},
		{
			"etask.entity": "sc017540",
			"id": "EBB4E392-BBD0-88B9-B780-89458DEC8C1A"
		},
		{
			"etask.entity": "sc017545",
			"id": "38F9B903-46C9-F7D0-0A12-D1267F299E54"
		},
		{
			"etask.entity": "sc017550",
			"id": "4A0FB625-13D2-DF95-6576-24017AD50F54"
		},
		{
			"etask.entity": "sc017555",
			"id": "80AC6CAC-89AD-DA68-EC19-C86C37AFFE3A"
		},
		{
			"etask.entity": "sc017560",
			"id": "D25AC0CA-263B-F6C3-2681-ED9159FBD85D"
		},
		{
			"etask.entity": "sc017562",
			"id": "09F9C858-18F1-2BBC-2EC5-AF48C4E07752"
		},
		{
			"etask.entity": "sc017567",
			"id": "DC4DE316-2757-FD9E-9F4C-D2B7868FB687"
		},
		{
			"etask.entity": "sc017572",
			"id": "ED5F7CC1-FAB5-CB43-5FFB-D2273F035C2A"
		},
		{
			"etask.entity": "sc017577",
			"id": "C1BE2C7B-7566-0228-08B8-C1706CCA7AB2"
		},
		{
			"etask.entity": "sc017582",
			"id": "F2102DBD-1EEC-734F-555B-BAB4D71DFC60"
		},
		{
			"etask.entity": "sc017584",
			"id": "C9A6DC9A-C8C0-E162-812D-E74AEFE6A449"
		},
		{
			"etask.entity": "sc017589",
			"id": "BA021D08-1E5F-97FE-E969-0FE283E00C74"
		},
		{
			"etask.entity": "sc017594",
			"id": "FA8DDFB2-D70F-DFE0-E913-0380084FB69E"
		},
		{
			"etask.entity": "sc017599",
			"id": "2C2F3610-2D04-10A7-B383-C73456F35C87"
		},
		{
			"etask.entity": "sc017604",
			"id": "1F529D06-ED60-16E2-0835-4024C97B1181"
		},
		{
			"etask.entity": "sc017606",
			"id": "22B62657-2B4E-4DBB-3D82-80EAB142C3D4"
		},
		{
			"etask.entity": "sc017611",
			"id": "78205721-8D8B-14B7-BDDF-5FC1D14EBA5B"
		},
		{
			"etask.entity": "sc017616",
			"id": "9A8A27A8-2CC9-0CE2-C0AF-4D86F1BBF086"
		},
		{
			"etask.entity": "sc017621",
			"id": "AB23408D-D193-78B5-5B25-053D1F8221CC"
		},
		{
			"etask.entity": "sc017626",
			"id": "0DD6F80A-9885-602F-1F87-797C71F672CF"
		},
		{
			"etask.entity": "sc017628",
			"id": "76A31DC5-5E69-8EEA-0256-69AEB83899E8"
		},
		{
			"etask.entity": "sc017633",
			"id": "47129603-90CF-A799-DD35-FD593F2F1CB9"
		},
		{
			"etask.entity": "sc017638",
			"id": "0907759D-5CC1-1D1A-619B-D36C8981B771"
		},
		{
			"etask.entity": "sc017643",
			"id": "DB103741-B36D-E56F-4508-CE03DABA008D"
		},
		{
			"etask.entity": "sc017648",
			"id": "EA5A7DC6-C181-05DB-0324-48A8C68E21C3"
		},
		{
			"etask.entity": "sc017650",
			"id": "AD9BC4EB-4F04-1FF9-B371-609245B1D7A1"
		},
		{
			"etask.entity": "sc017655",
			"id": "9DF7A20A-D29D-DE5F-4518-B23940526AA6"
		},
		{
			"etask.entity": "sc017660",
			"id": "505F22AC-5114-FE4D-94B3-541294AEE6AD"
		},
		{
			"etask.entity": "sc017665",
			"id": "4F137688-50B2-AF9C-A396-B602ABE78BDB"
		},
		{
			"etask.entity": "sc017670",
			"id": "76DC1727-AB96-B1F3-2786-97C769896946"
		},
		{
			"etask.entity": "sc017672",
			"id": "3473C05C-DB21-570A-36ED-16CE125EBBBC"
		},
		{
			"etask.entity": "sc017677",
			"id": "D813303B-5BC3-C4AF-47BD-9C097E343BE8"
		},
		{
			"etask.entity": "sc017682",
			"id": "ECC3DABE-AC86-D707-FC7A-A7A238072E03"
		},
		{
			"etask.entity": "sc017687",
			"id": "4A607647-E6D8-7A3B-A453-9759B140234B"
		},
		{
			"etask.entity": "sc017692",
			"id": "F1D19DE0-0028-3CCA-80AB-92BE1095D4BD"
		},
		{
			"etask.entity": "sc017694",
			"id": "AF284B6B-021A-D683-5D44-5370A8B9DFA1"
		},
		{
			"etask.entity": "sc017699",
			"id": "DCA46E6A-FDE3-FFDD-2717-F26A98ED650C"
		},
		{
			"etask.entity": "sc017704",
			"id": "CAEFFEF6-B88A-DF86-4E8F-94CBEFD5B3C0"
		},
		{
			"etask.entity": "sc017709",
			"id": "9DF9879F-11FB-51EE-089C-3C836178BD75"
		},
		{
			"etask.entity": "sc017714",
			"id": "B0B38BFD-33C6-BE1D-6C63-3F9722D94C16"
		},
		{
			"etask.entity": "sc017716",
			"id": "FC111BAE-D9B0-87B2-6810-CD9FD6AF3DA5"
		},
		{
			"etask.entity": "sc017721",
			"id": "007F39A9-7101-BE94-1010-E541C71CA783"
		},
		{
			"etask.entity": "sc017726",
			"id": "3B50413B-7F3F-1DB2-BAAF-FE201AC7A261"
		},
		{
			"etask.entity": "sc017731",
			"id": "6B0E23B8-F861-82BE-A5F2-7E161F483F4F"
		},
		{
			"etask.entity": "sc017736",
			"id": "DF4BD894-5888-3C9F-3F09-1A4CD66114BA"
		},
		{
			"etask.entity": "sc017738",
			"id": "98916D45-991A-D33E-A41C-2418BFFF82A7"
		},
		{
			"etask.entity": "sc017743",
			"id": "FAE4F3A8-72F7-F18D-C924-D562DB34F05E"
		},
		{
			"etask.entity": "sc017748",
			"id": "17BF6678-3507-C5F1-8B01-4E1A48B2B879"
		},
		{
			"etask.entity": "sc017753",
			"id": "E3BE9BC2-B55E-ECD7-DEFB-05796ED72D7B"
		},
		{
			"etask.entity": "sc017758",
			"id": "8CFD9EF3-697E-2FFA-5075-7CEFF7E01906"
		},
		{
			"etask.entity": "sc017760",
			"id": "71C92BC8-DCB7-A324-EA14-3464B872D033"
		},
		{
			"etask.entity": "sc017765",
			"id": "17F875FD-C0B6-ACF8-48FF-471CE97E64D6"
		},
		{
			"etask.entity": "sc017770",
			"id": "6EB2A2D5-D7D5-2751-CCA5-0465973C726C"
		},
		{
			"etask.entity": "sc017775",
			"id": "1AF3721C-1EB3-1275-D6E3-C9F34C6DB920"
		},
		{
			"etask.entity": "sc017780",
			"id": "C88BFBF6-7F32-AF73-78ED-2E688D56DE55"
		},
		{
			"etask.entity": "sc017782",
			"id": "E7FC20FE-1FF9-0862-41F4-122599912DF3"
		},
		{
			"etask.entity": "sc017787",
			"id": "B4B66BDC-A040-7384-4B08-E430B4BAECD7"
		},
		{
			"etask.entity": "sc017792",
			"id": "33846A0A-93E7-71AA-14AC-C4A7DFA606AE"
		},
		{
			"etask.entity": "sc017797",
			"id": "666D6FEA-F58A-7D7D-8B4C-6A62E6557E5E"
		},
		{
			"etask.entity": "sc017802",
			"id": "10054B5A-3049-5971-C29A-FC80DCAC62B8"
		},
		{
			"etask.entity": "sc017804",
			"id": "EDFF0A9F-4E9C-2FA1-9F20-39E33ED9FBC3"
		},
		{
			"etask.entity": "sc017809",
			"id": "AA1FF81D-01F3-AF62-ACDC-4EA9D5C4B336"
		},
		{
			"etask.entity": "sc017814",
			"id": "E5ED4F1B-D26A-E9DB-9DB2-A766BE7DD549"
		},
		{
			"etask.entity": "sc017819",
			"id": "91A64E2A-DB34-3536-32DE-3600AC6963BF"
		},
		{
			"etask.entity": "sc017824",
			"id": "815134B9-2C2B-8AB4-F460-6404EFAB9858"
		},
		{
			"etask.entity": "sc017825",
			"id": "C258EB04-3B08-1139-E0E7-1C54116AD5A9"
		},
		{
			"etask.entity": "sc017826",
			"id": "5F69A9F0-CF96-1B9B-6864-AA50F1DB7A76"
		},
		{
			"etask.entity": "sc017831",
			"id": "621229F0-CEA6-56F5-5630-D29085AA56AF"
		},
		{
			"etask.entity": "sc017836",
			"id": "CA933646-5DD8-C665-534D-6E7A30DC5A5D"
		},
		{
			"etask.entity": "sc017841",
			"id": "C8BCD7EC-B738-87CF-D7E1-DA2E9B45E536"
		},
		{
			"etask.entity": "sc017846",
			"id": "9E629B3C-7473-B351-59AA-1F0CDCD577EF"
		},
		{
			"etask.entity": "sc017848",
			"id": "25D20174-E894-17E4-2772-C19164102B0B"
		},
		{
			"etask.entity": "sc017853",
			"id": "96C42CE4-9D8A-C479-65F6-EDA491DB4B68"
		},
		{
			"etask.entity": "sc017855",
			"id": "6F09A645-0444-629E-D136-1A47D15BF165"
		},
		{
			"etask.entity": "sc017863",
			"id": "5377912B-0509-CC13-EDF8-B88C4B13A320"
		},
		{
			"etask.entity": "sc017864",
			"id": "ECD7F6D9-14FC-2BC1-ADDE-D1E1A01CE7FC"
		},
		{
			"etask.entity": "sc017870",
			"id": "E420485C-E0AA-487B-EF5E-14B261A98A7B"
		},
		{
			"etask.entity": "sc017875",
			"id": "5266F5ED-0BE7-0F8F-5390-40164F369E02"
		},
		{
			"etask.entity": "sc017876",
			"id": "C504738E-39A2-646B-3DDA-5B3596F320E6"
		},
		{
			"etask.entity": "sc017877",
			"id": "A74100D8-1E89-CE55-7AC1-D929EF561520"
		},
		{
			"etask.entity": "sc017888",
			"id": "B3282AF1-74A5-C3BD-1032-85D6CB8771E5"
		},
		{
			"etask.entity": "sc017889",
			"id": "30F478AB-E902-A416-09D3-8CFADEBB32D1"
		},
		{
			"etask.entity": "sc017892",
			"id": "5863A2B0-AD8B-0AB1-CA1B-1E14590D500E"
		},
		{
			"etask.entity": "sc017897",
			"id": "57CA0D35-6930-E64C-AAD2-7B0F2B45B859"
		},
		{
			"etask.entity": "sc017902",
			"id": "E423E953-7FC6-028C-7A31-01499871982F"
		},
		{
			"etask.entity": "sc017907",
			"id": "273D92A9-983C-5444-C46F-0844B521C1BB"
		},
		{
			"etask.entity": "sc017912",
			"id": "F3F10513-4833-2312-4472-F725E5589AF1"
		},
		{
			"etask.entity": "sc017914",
			"id": "3ACF3966-3085-A545-9B88-A2EDC923C6DA"
		},
		{
			"etask.entity": "sc017919",
			"id": "E6545AC5-A131-AF4B-ABA4-8B7A64A2D07A"
		},
		{
			"etask.entity": "sc017920",
			"id": "8E493BB7-55AA-3651-BCF6-5C57ACB4D329"
		},
		{
			"etask.entity": "sc017921",
			"id": "BD166568-683C-414F-6546-4FE40FC61AB0"
		},
		{
			"etask.entity": "sc017934",
			"id": "3CFC193E-4416-E36D-DB13-1E0E24035CB0"
		},
		{
			"etask.entity": "sc017936",
			"id": "8DDC2BB7-18C2-564F-7141-9C82A5976684"
		},
		{
			"etask.entity": "sc017941",
			"id": "5B39C3AC-C661-F09A-16DC-DE2060B0C43F"
		},
		{
			"etask.entity": "sc017946",
			"id": "1B2855AA-C04A-D786-EAA8-BBE2C65CE48A"
		},
		{
			"etask.entity": "sc017951",
			"id": "2EB97F40-E54C-A27D-E709-D5BE7D5C6A5C"
		},
		{
			"etask.entity": "sc017956",
			"id": "9C148D57-5C0A-D210-944B-9AF6CDF78EB8"
		},
		{
			"etask.entity": "sc017958",
			"id": "3BBDAC6A-5A2E-BD21-FB15-7FF07B8690DE"
		},
		{
			"etask.entity": "sc017963",
			"id": "1F3ED0E9-BDC8-3CB5-340E-8A1E638C3CEC"
		},
		{
			"etask.entity": "sc017968",
			"id": "D99B1BB9-61D5-A2AE-90C6-2EFF5377DF9E"
		},
		{
			"etask.entity": "sc017973",
			"id": "CF55D440-10F8-35A3-18F1-01AACEB8D6C5"
		},
		{
			"etask.entity": "sc017978",
			"id": "C980F744-2386-240D-AF77-81915C0E1664"
		},
		{
			"etask.entity": "sc017980",
			"id": "38F70894-12E4-BF09-1666-8CA0FD9CD12F"
		},
		{
			"etask.entity": "sc017985",
			"id": "2C2F4322-54A7-48DA-388F-38DDA5586182"
		},
		{
			"etask.entity": "sc017990",
			"id": "3AB44FEB-CE68-0746-4296-BD69842917B9"
		},
		{
			"etask.entity": "sc017995",
			"id": "EFCCC8DC-5EA0-709A-2BB1-F2D99E72BCA6"
		},
		{
			"etask.entity": "sc018000",
			"id": "919947EC-6F93-CB2A-B873-6558A41F6C7C"
		},
		{
			"etask.entity": "sc018002",
			"id": "931E2741-E7B2-D009-D111-57EE2AEC2925"
		},
		{
			"etask.entity": "sc018007",
			"id": "DB6DAD8F-8683-F40C-E065-B522C24AF072"
		},
		{
			"etask.entity": "sc018012",
			"id": "7E9D8DDC-3818-8B8E-AD02-FAA08ED02AC4"
		},
		{
			"etask.entity": "sc018017",
			"id": "4386DA3B-198C-1B3F-F820-596EEA5C7D51"
		},
		{
			"etask.entity": "sc018022",
			"id": "2CD3D3A1-7BD5-7779-32FE-4EC2C0A4BD13"
		},
		{
			"etask.entity": "sc018024",
			"id": "72E80716-5A57-9EDC-EFFD-2A6B1315C970"
		},
		{
			"etask.entity": "sc018029",
			"id": "43A7937B-E31E-4C11-50CE-4F6DD1AF5FF3"
		},
		{
			"etask.entity": "sc018034",
			"id": "38A15FDA-4A8D-02C2-2253-42B1D0BEE8AB"
		},
		{
			"etask.entity": "sc018039",
			"id": "25E7CA3A-CB50-5B5E-8BB3-BB08BEE9B159"
		},
		{
			"etask.entity": "sc018044",
			"id": "1BB6069E-0941-53B2-E8C7-637C3D399F76"
		},
		{
			"etask.entity": "sc018046",
			"id": "B82D6B9D-64AC-6D19-3E9E-E7544F5A16DC"
		},
		{
			"etask.entity": "sc018051",
			"id": "E7408797-2109-4EB6-918A-F6FD643BE2D4"
		},
		{
			"etask.entity": "sc018056",
			"id": "0AFC68CA-CA38-DFC8-FAD8-8C11F14637DA"
		},
		{
			"etask.entity": "sc018061",
			"id": "A7C83657-3C62-F7AF-4BC8-7C94C1C584F7"
		},
		{
			"etask.entity": "sc018066",
			"id": "FE68DE4D-2713-EA85-FA95-81682D473719"
		},
		{
			"etask.entity": "sc018068",
			"id": "6EB198D3-FCF1-500C-15C0-D68B438164ED"
		},
		{
			"etask.entity": "sc018073",
			"id": "3BCE1D91-9076-2A55-ACDA-C805D0E45226"
		},
		{
			"etask.entity": "sc018078",
			"id": "17CF4E19-D774-0D11-AFC0-5CC1587CB35E"
		},
		{
			"etask.entity": "sc018083",
			"id": "1F8F2AAD-CC51-A002-0951-6C1C48A5ED50"
		},
		{
			"etask.entity": "sc018088",
			"id": "6B42E9DA-A313-FF41-508A-00F5DCDC9ADE"
		},
		{
			"etask.entity": "sc018090",
			"id": "8636DD4C-5D9F-856C-45DA-5D16FFD26739"
		},
		{
			"etask.entity": "sc018095",
			"id": "476E34CC-16A1-1255-39E5-5C73C95A1B8C"
		},
		{
			"etask.entity": "sc018100",
			"id": "9F942EF0-49EA-B718-DE80-B9BB59FC4A42"
		},
		{
			"etask.entity": "sc018105",
			"id": "D089BF9D-E9FC-6D9E-21CD-8BD2067EBBEA"
		},
		{
			"etask.entity": "sc018110",
			"id": "EE34222E-FF8E-3682-7E15-5B5BEF3B17AF"
		},
		{
			"etask.entity": "sc018112",
			"id": "10D23279-270B-132D-499E-3F6C7BE8948F"
		},
		{
			"etask.entity": "sc018117",
			"id": "9977E03C-FEB5-6D07-779E-7E5A1BAE8B1D"
		},
		{
			"etask.entity": "sc018122",
			"id": "504F7370-99FA-C3EA-E99A-B6A780D95B3E"
		},
		{
			"etask.entity": "sc018127",
			"id": "DE2D2A33-42EB-E8D9-54DF-71518B1F18C1"
		},
		{
			"etask.entity": "sc018132",
			"id": "ABC62EB8-AA1A-7EB6-C011-242E2056A2C7"
		},
		{
			"etask.entity": "sc018134",
			"id": "EED92D9B-3427-D927-7D9B-D4A92AE41721"
		},
		{
			"etask.entity": "sc018139",
			"id": "DA29449A-7CCA-E3E8-7FDF-69A0D9791027"
		},
		{
			"etask.entity": "sc018144",
			"id": "D4E9F321-AD86-E6BF-BEB4-421D9FF049BF"
		},
		{
			"etask.entity": "sc018149",
			"id": "0AFCF157-B246-06BA-FD04-A55AC25182C6"
		},
		{
			"etask.entity": "sc018154",
			"id": "77A07213-1D4A-A7C9-5424-B8E62A2F31B8"
		},
		{
			"etask.entity": "sc018156",
			"id": "68F5E108-5B09-7490-8466-40DDB614A3D6"
		},
		{
			"etask.entity": "sc018161",
			"id": "AAC6D9DE-F94D-BB94-AF0D-589F1B9C4981"
		},
		{
			"etask.entity": "sc018166",
			"id": "63D74E5D-F616-5134-B782-AF589ACDCBE7"
		},
		{
			"etask.entity": "sc018171",
			"id": "1BBB883B-15E1-900B-7FE4-6AC651FFB60F"
		},
		{
			"etask.entity": "sc018176",
			"id": "621271DE-C0ED-FE80-DE0F-519AF90FE7A3"
		},
		{
			"etask.entity": "sc018178",
			"id": "EC7502FD-A00D-242C-3BA8-D9AC2E7D8626"
		},
		{
			"etask.entity": "sc018183",
			"id": "F2637BE7-E41D-A6D7-F902-00320562D0E5"
		},
		{
			"etask.entity": "sc018188",
			"id": "C0E1BF27-255B-51A0-CFDC-384A19D3E7FB"
		},
		{
			"etask.entity": "sc018193",
			"id": "5507C546-AA92-2BB2-40FE-F46F8103F68B"
		},
		{
			"etask.entity": "sc018198",
			"id": "CCC0DB08-F3C0-7AB1-F733-7FC2B312BD09"
		},
		{
			"etask.entity": "sc018200",
			"id": "2C3CEFCE-6333-C250-79E9-5D8A1C0011CC"
		},
		{
			"etask.entity": "sc018205",
			"id": "8D4FC6EB-A34C-2300-3867-93AB92C4907D"
		},
		{
			"etask.entity": "sc018210",
			"id": "1CE1531D-17DD-9AD5-6EC3-561574E620CF"
		},
		{
			"etask.entity": "sc018215",
			"id": "4A143293-B055-E4AF-2B96-F217182A51E0"
		},
		{
			"etask.entity": "sc018220",
			"id": "688BB354-09FC-14FE-6B37-AC92CBFED5B6"
		},
		{
			"etask.entity": "sc018222",
			"id": "149B9EE9-B5CD-01E8-F04F-FB9F3DFF681D"
		},
		{
			"etask.entity": "sc018227",
			"id": "3114BEBC-42B5-6051-35EA-6250C675E3E1"
		},
		{
			"etask.entity": "sc018232",
			"id": "611CF309-C6C7-3AD5-67AF-768F181D6A12"
		},
		{
			"etask.entity": "sc018237",
			"id": "8B544384-C3EF-9869-00E5-FCC257CF3B85"
		},
		{
			"etask.entity": "sc018239",
			"id": "0D241305-E606-140C-CB3F-088F45FC1803"
		},
		{
			"etask.entity": "sc018240",
			"id": "16B9C2EA-03D4-C318-9FC3-4E34FDDB14B7"
		},
		{
			"etask.entity": "sc018241",
			"id": "E97015AC-9324-BA75-54EC-2C8E2541505A"
		},
		{
			"etask.entity": "sc018244",
			"id": "E539101D-AD19-27EA-D2DA-2431B49CD2E2"
		},
		{
			"etask.entity": "sc018249",
			"id": "47F1D8DE-E190-7CB1-E9E8-00F43EC2A530"
		},
		{
			"etask.entity": "sc018254",
			"id": "DAA3915C-50ED-B799-757A-033438C1E8E5"
		},
		{
			"etask.entity": "sc018259",
			"id": "DB497F5D-DB69-98A9-E94A-A0E12375DD26"
		},
		{
			"etask.entity": "sc018264",
			"id": "B9E7BFAB-6BC9-0F84-46A3-319355E2B90B"
		},
		{
			"etask.entity": "sc018265",
			"id": "6AD84D47-3B9D-A5C1-BB5D-B16C956F8EFF"
		},
		{
			"etask.entity": "sc018266",
			"id": "BDB67819-AA3E-3674-74AF-0B5E2CA1A0E3"
		},
		{
			"etask.entity": "sc018267",
			"id": "78E1AD3F-FDC9-BAF6-18A7-B16DBA2A83AD"
		},
		{
			"etask.entity": "sc018268",
			"id": "A3F1D923-77FE-DCE6-AD32-876F0DE29095"
		},
		{
			"etask.entity": "sc018281",
			"id": "0369E0C1-5AC1-C570-B4F3-C28F82ABB613"
		},
		{
			"etask.entity": "sc018286",
			"id": "1964843A-F565-4347-F7B7-BB41281DAE38"
		},
		{
			"etask.entity": "sc018288",
			"id": "18ADF755-7BBB-8D40-BEC6-622C9FA9654D"
		},
		{
			"etask.entity": "sc018293",
			"id": "28102598-9B33-B144-F2FC-59CD83AED840"
		},
		{
			"etask.entity": "sc018295",
			"id": "C21CB6FF-6455-397C-04D1-E8B2051432E3"
		},
		{
			"etask.entity": "sc018296",
			"id": "8461E473-376E-52A2-910F-EBA9B0B76004"
		},
		{
			"etask.entity": "sc018297",
			"id": "2AA6BC8B-7C88-B939-E577-A5EFBB7F27F0"
		},
		{
			"etask.entity": "sc018298",
			"id": "E9D920B1-2146-FBC6-964C-FE53CA929F13"
		},
		{
			"etask.entity": "sc018302",
			"id": "A1C1F446-8603-E2ED-5485-3E10513DBBC0"
		},
		{
			"etask.entity": "sc018303",
			"id": "97B8EDD8-00CD-FCD9-8577-7BF4D32EEB53"
		},
		{
			"etask.entity": "sc018304",
			"id": "ADCFCFBB-D78C-8210-8E73-E6CB5AD36AC1"
		},
		{
			"etask.entity": "sc018305",
			"id": "0890E17F-D2F8-8944-0559-097D48C10CC0"
		},
		{
			"etask.entity": "sc018306",
			"id": "778BB868-9DF9-3A73-B641-5FF961AD5973"
		},
		{
			"etask.entity": "sc018307",
			"id": "B0DB6CF0-ED09-D148-DAFE-BC7FE5324C2D"
		},
		{
			"etask.entity": "sc018308",
			"id": "E0DEB6CA-EB5F-33C3-FF5F-BD2902645E9A"
		},
		{
			"etask.entity": "sc018309",
			"id": "7CC94546-0CBC-86F6-8F81-6826C5207699"
		},
		{
			"etask.entity": "sc018310",
			"id": "EC3A951D-5F69-DC0B-6DA3-B111DB170398"
		},
		{
			"etask.entity": "sc018311",
			"id": "20E7D05B-6B8B-76CA-0A08-04ACF82E417B"
		},
		{
			"etask.entity": "sc018312",
			"id": "7B2BDA88-CADD-52C7-FD58-CC43510A0EA2"
		},
		{
			"etask.entity": "sc018321",
			"id": "C6682980-A2BD-CB4D-875C-230E73A93844"
		},
		{
			"etask.entity": "sc018322",
			"id": "16672FBA-D2F7-74F6-33A8-E4D197A5CE27"
		},
		{
			"etask.entity": "sc018323",
			"id": "24934919-4838-3376-4D69-525B5D2B5EB8"
		},
		{
			"etask.entity": "sc018332",
			"id": "6411EB6C-6045-AA18-AEEC-37B7065C8894"
		},
		{
			"etask.entity": "sc018337",
			"id": "445A58DB-8443-B7BD-5D24-B5147924616B"
		},
		{
			"etask.entity": "sc018342",
			"id": "0BFF5B29-EC21-ED3B-386F-A6E498737F6B"
		},
		{
			"etask.entity": "sc018347",
			"id": "6997A0B0-FB13-0E69-B8C5-F35BB4DAC159"
		},
		{
			"etask.entity": "sc018348",
			"id": "9D4EEAB7-F495-4906-85BA-7BF918DEF3C9"
		},
		{
			"etask.entity": "sc018349",
			"id": "9C9ED6C1-8006-A078-936E-6F490BF71169"
		},
		{
			"etask.entity": "sc018350",
			"id": "72C7FA8D-F57E-9D2B-29BD-6FC3148EF557"
		},
		{
			"etask.entity": "sc018354",
			"id": "3DB267A2-C466-728D-6996-B78FA4632060"
		},
		{
			"etask.entity": "sc018359",
			"id": "ED99E781-0F8D-59CC-8147-B33FEE89E2E0"
		},
		{
			"etask.entity": "sc018364",
			"id": "DE401785-852C-D3A5-D7CB-62BBFD925F79"
		},
		{
			"etask.entity": "sc018369",
			"id": "9271166E-E20A-52B6-F1ED-BF6795BAE167"
		},
		{
			"etask.entity": "sc018374",
			"id": "0756C39B-53F5-AE29-1361-66D961890B5B"
		},
		{
			"etask.entity": "sc018375",
			"id": "9FF048B0-EF33-9931-FF15-7D9AA2A23042"
		},
		{
			"etask.entity": "sc018376",
			"id": "0302F4BB-2151-7EA8-315C-1E55583AD176"
		},
		{
			"etask.entity": "sc018377",
			"id": "B31383AA-FD53-184A-694D-86996DA66C36"
		},
		{
			"etask.entity": "sc018386",
			"id": "9A24CF5E-C8C5-F875-1E4C-D1BA20633C32"
		},
		{
			"etask.entity": "sc018391",
			"id": "8933ACF9-2D8E-BC2D-0870-E38A97C4CD7B"
		},
		{
			"etask.entity": "sc018396",
			"id": "2CE5E86E-F584-2C13-DCCE-D40D4E7A9618"
		},
		{
			"etask.entity": "sc018398",
			"id": "451E7775-4C8A-49B3-2FB7-730EA35530F7"
		},
		{
			"etask.entity": "sc018403",
			"id": "483396EB-4F3E-53CF-9120-2B26BA82A301"
		},
		{
			"etask.entity": "sc018408",
			"id": "FFA38ACC-BCFF-A84A-D937-526CD67F1628"
		},
		{
			"etask.entity": "sc018413",
			"id": "EE99089A-BA01-91FD-9B72-B5EC1253B24F"
		},
		{
			"etask.entity": "sc018418",
			"id": "FA3E75C4-3402-472D-19F6-6794DFE0C729"
		},
		{
			"etask.entity": "sc018420",
			"id": "70CC6AC9-3D4E-26B4-1D68-F3DEABF17501"
		},
		{
			"etask.entity": "sc018425",
			"id": "391AA3CD-C5A4-B141-4A0E-8ADFB2FA9992"
		},
		{
			"etask.entity": "sc018430",
			"id": "4DA11E1B-59B9-31A0-8F24-6997DA6F52F3"
		},
		{
			"etask.entity": "sc018435",
			"id": "AB6FB420-0FAF-3601-D19D-4DB22F29F895"
		},
		{
			"etask.entity": "sc018440",
			"id": "DAB4454E-1768-2EBB-959E-1C39ED388A06"
		},
		{
			"etask.entity": "sc018442",
			"id": "1DD889BE-54F1-055F-3FB8-1ED725B13BDC"
		},
		{
			"etask.entity": "sc018447",
			"id": "748021D2-A0CF-AD08-A7C9-8E61B63DF845"
		},
		{
			"etask.entity": "sc018452",
			"id": "46BC0A95-A5E0-C86B-8D4F-85F8CC11694A"
		},
		{
			"etask.entity": "sc018457",
			"id": "9D49F8EB-BCEC-CA3F-E6E7-893D0DE2BA94"
		},
		{
			"etask.entity": "sc018462",
			"id": "AD66BA5E-7172-8AA3-3CC0-BD3566062DDA"
		},
		{
			"etask.entity": "sc018464",
			"id": "35DB11B6-CA31-2555-DBA2-2B4FF3CCDB9B"
		},
		{
			"etask.entity": "sc018469",
			"id": "8C73FF70-FA9D-6A63-3244-036605FDC12B"
		},
		{
			"etask.entity": "sc018474",
			"id": "A05ABE79-C506-035F-1FD7-FB220AD7C651"
		},
		{
			"etask.entity": "sc018479",
			"id": "439D4DD3-57D5-5BD4-9FC4-EA63B601F00B"
		},
		{
			"etask.entity": "sc018484",
			"id": "22ED1281-E297-B3B5-6412-4495D7770896"
		},
		{
			"etask.entity": "sc018486",
			"id": "3796DDC5-D7FA-AE69-DF22-7A2174DA9A3F"
		},
		{
			"etask.entity": "sc018491",
			"id": "C20364D6-75EC-F939-4210-2677A4DFE2D2"
		},
		{
			"etask.entity": "sc018496",
			"id": "7BE6DE06-ABAB-DFBF-D51E-ED64F8A54192"
		},
		{
			"etask.entity": "sc018501",
			"id": "7D81A4D7-A5AA-002C-2621-61EB669C40E9"
		},
		{
			"etask.entity": "sc018506",
			"id": "955AA00A-082A-C4A3-B4B7-801CABAE8412"
		},
		{
			"etask.entity": "sc018508",
			"id": "12E14960-10EC-FD17-8088-33218EA5844C"
		},
		{
			"etask.entity": "sc018513",
			"id": "60380AA7-1F5B-ACC9-044A-C2DDF117EFC4"
		},
		{
			"etask.entity": "sc018518",
			"id": "1CF35204-33C5-DA82-8517-EA49BB9BEE80"
		},
		{
			"etask.entity": "sc018523",
			"id": "23A64238-448F-FECE-940C-8700C8EE670F"
		},
		{
			"etask.entity": "sc018528",
			"id": "3B10FF35-CF05-254B-E4DB-548E0F4C1FE9"
		},
		{
			"etask.entity": "sc018530",
			"id": "7725FEA0-14A1-23EE-E485-71807CE7863A"
		},
		{
			"etask.entity": "sc018535",
			"id": "0567BB5F-7FA5-1643-39BF-699CC262E486"
		},
		{
			"etask.entity": "sc018540",
			"id": "C1514E62-18E6-704E-DA3E-F8DF7A1711B5"
		},
		{
			"etask.entity": "sc018545",
			"id": "A41FE052-6480-95DC-5EB3-78A6D68ABD36"
		},
		{
			"etask.entity": "sc018550",
			"id": "9111ECED-2DE6-0B4B-ED36-0485DA30D443"
		},
		{
			"etask.entity": "sc018552",
			"id": "25A7C1BE-DF20-E182-3E15-797C609D9101"
		},
		{
			"etask.entity": "sc018557",
			"id": "38FD9EEC-AC32-E3F5-D717-9715A9037164"
		},
		{
			"etask.entity": "sc018562",
			"id": "FC675422-0049-4983-53E9-12DE5CA4264C"
		},
		{
			"etask.entity": "sc018567",
			"id": "12DC47FD-4476-C2FB-5DB7-F03BCD5D9813"
		},
		{
			"etask.entity": "sc018572",
			"id": "C8331A8E-E3C6-FCA9-D696-B859CFE6117B"
		},
		{
			"etask.entity": "sc018574",
			"id": "9D7E166F-49EE-DC3B-31B3-53B927BC8F35"
		},
		{
			"etask.entity": "sc018579",
			"id": "723F2303-355F-17AB-968D-428AD9AFC5EE"
		},
		{
			"etask.entity": "sc018584",
			"id": "7032EFEF-A8E5-19BF-0D6F-08B0399ED176"
		},
		{
			"etask.entity": "sc018589",
			"id": "4C60D9B1-6FED-BFDE-50AC-768044D1C14C"
		},
		{
			"etask.entity": "sc018594",
			"id": "547959D8-3BB5-DAD3-C342-8BBF293C4F39"
		},
		{
			"etask.entity": "sc018596",
			"id": "CF10FC4B-23AF-C03A-EA89-4E31F8F0AA38"
		},
		{
			"etask.entity": "sc018601",
			"id": "3AEC6257-2DB5-0FEB-91E7-0C65A9A7BF35"
		},
		{
			"etask.entity": "sc018606",
			"id": "1D291782-FB7D-EA31-26B0-913F0B459DC4"
		},
		{
			"etask.entity": "sc018611",
			"id": "2F01E4AB-155C-1887-AFB6-3EBA13E243D3"
		},
		{
			"etask.entity": "sc018616",
			"id": "79F94CA8-BAC3-1F30-AF57-BCB9C0BEC354"
		},
		{
			"etask.entity": "sc018618",
			"id": "4DE0A53A-B6C1-1C95-DE05-2C3C0ABB6E36"
		},
		{
			"etask.entity": "sc018621",
			"id": "8D37D8F2-8E95-1A34-16E3-FCF6945905B0"
		},
		{
			"etask.entity": "sc018622",
			"id": "400E35CB-C82C-591A-B1E1-01F67D48BAB9"
		},
		{
			"etask.entity": "sc018633",
			"id": "4FBAA259-B741-8C8B-A4BE-8ED88D9DC4F7"
		},
		{
			"etask.entity": "sc018634",
			"id": "CCA793E4-BFAA-FDAB-4379-0B33C64DE137"
		},
		{
			"etask.entity": "sc018640",
			"id": "D3E49056-12DB-9B10-0F03-ABAE124CEADB"
		},
		{
			"etask.entity": "sc018645",
			"id": "10037739-7A65-F902-4DF7-8ABA6AE23F66"
		},
		{
			"etask.entity": "sc018650",
			"id": "D22F60C5-0C3E-4CD3-9008-074E37BB6706"
		},
		{
			"etask.entity": "sc018655",
			"id": "FF95C6D0-EC2B-C663-C758-098F7CE8B80F"
		},
		{
			"etask.entity": "sc018660",
			"id": "B9271102-BFD1-5742-094F-FA8562CB6391"
		},
		{
			"etask.entity": "sc018662",
			"id": "40A21502-4644-1783-56A2-9EBFE2C6FE6A"
		},
		{
			"etask.entity": "sc018667",
			"id": "86EE0701-BD8F-31B2-BE4E-126650127901"
		},
		{
			"etask.entity": "sc018672",
			"id": "ED1BD0E6-E924-42C7-9460-9035D277AC40"
		},
		{
			"etask.entity": "sc018677",
			"id": "6BF544E3-153F-2505-128F-D61F08E8DBD2"
		},
		{
			"etask.entity": "sc018682",
			"id": "B76CF200-BB31-CBC5-F9EC-F19A27CDFB37"
		},
		{
			"etask.entity": "sc018700",
			"id": "4E8097F5-A38B-7DBC-6DCF-8FA58E2228E4"
		},
		{
			"etask.entity": "sc018701",
			"id": "DAE5A6B2-5610-03E7-98B9-944786306098"
		},
		{
			"etask.entity": "sc018702",
			"id": "8FB8E7B5-50D3-8A50-7C63-B2F001D30B76"
		},
		{
			"etask.entity": "sc018703",
			"id": "3F38E6A2-6346-BC26-07CE-4F9418C097E1"
		},
		{
			"etask.entity": "sc018704",
			"id": "2537E90E-D4FE-9621-3077-E9B35D06ADA9"
		},
		{
			"etask.entity": "sc018705",
			"id": "A548BDAF-93FB-6A5D-648D-B4A9C5A54F43"
		},
		{
			"etask.entity": "sc018706",
			"id": "2DE7C7A6-9C17-EB33-4666-6C5D5D5CB6ED"
		},
		{
			"etask.entity": "sc018707",
			"id": "061A7EE1-DC5B-389A-A77B-A74C75178BAC"
		},
		{
			"etask.entity": "sc018708",
			"id": "6A956B3E-74E6-AA18-CEA3-DB1CE2FD257D"
		},
		{
			"etask.entity": "sc018709",
			"id": "33B23562-BC66-F9CE-AF83-81B8DE5D45E7"
		},
		{
			"etask.entity": "sc018710",
			"id": "76705316-2077-FA1D-53E8-634D035A7424"
		},
		{
			"etask.entity": "sc018711",
			"id": "669463FF-21C2-588E-4213-48BD22DA61A7"
		},
		{
			"etask.entity": "sc018712",
			"id": "DE8F7ECA-559B-267E-05DF-0D20ECE7F757"
		},
		{
			"etask.entity": "sc018713",
			"id": "2887E039-315F-F6E5-B6BB-F71FBC6C8C74"
		},
		{
			"etask.entity": "sc018714",
			"id": "5E158AE4-3F86-BC5A-7918-843A3347E18E"
		},
		{
			"etask.entity": "sc018715",
			"id": "38E14B9C-F47F-A838-A965-10C3E28AF824"
		},
		{
			"etask.entity": "sc018716",
			"id": "218507DB-7F09-8B0B-97F1-55C59D1E3B93"
		},
		{
			"etask.entity": "sc018717",
			"id": "244BEC26-65A5-297D-EBDA-0CC98C338065"
		},
		{
			"etask.entity": "sc018718",
			"id": "F956538F-9C9E-6A6C-9D30-CEF4D5542780"
		},
		{
			"etask.entity": "sc018719",
			"id": "949A7173-DC9A-B96F-1493-0111F8AC1420"
		},
		{
			"etask.entity": "sc018720",
			"id": "88963730-6419-22A0-5680-3D8E69650E9D"
		},
		{
			"etask.entity": "sc018721",
			"id": "E493E36B-4099-028E-4A12-946565F5B6DE"
		},
		{
			"etask.entity": "sc018722",
			"id": "708FEEFA-0BEC-A29A-19BB-428B83AA9ED4"
		},
		{
			"etask.entity": "sc018723",
			"id": "AC9317C1-5359-1EC3-CF8F-7FBB501417DB"
		},
		{
			"etask.entity": "sc018724",
			"id": "FE2020AA-0FF7-5C44-E8BB-C4601E828A30"
		},
		{
			"etask.entity": "sc018725",
			"id": "518F186A-5707-EAA5-6F73-B9F8DD9B3B39"
		},
		{
			"etask.entity": "sc018726",
			"id": "193EF600-885C-1260-83D0-0A31EB02EE2F"
		},
		{
			"etask.entity": "sc018727",
			"id": "E23819B9-0455-7516-7836-63EDC07CECC7"
		},
		{
			"etask.entity": "sc018728",
			"id": "8F8F6AF4-63D8-A883-15E1-1316D4F75588"
		},
		{
			"etask.entity": "sc018729",
			"id": "AA52FBCB-FBD9-8006-EDB7-BC14AF437BA5"
		},
		{
			"etask.entity": "sc018730",
			"id": "5D255400-3580-0F6F-3463-63F48A6F52B0"
		},
		{
			"etask.entity": "sc018731",
			"id": "6BBFF7DA-0424-5AEA-E48D-851812CEE93C"
		},
		{
			"etask.entity": "sc018732",
			"id": "B12E7B16-1589-7B9D-A6B6-69CD511EE8D1"
		},
		{
			"etask.entity": "sc018733",
			"id": "06141E54-2497-DCE5-93E1-26F265AC6249"
		},
		{
			"etask.entity": "sc018734",
			"id": "1D6167B2-B1EB-1750-6E70-AECB4BEA35CD"
		},
		{
			"etask.entity": "sc018735",
			"id": "2137361C-E14F-6D19-A662-28AE84DA8CF2"
		},
		{
			"etask.entity": "sc018736",
			"id": "5236EE36-7958-99AF-D03C-FAF13ECC7D90"
		},
		{
			"etask.entity": "sc018737",
			"id": "8C87004B-38E2-8228-3FEE-05186897AE89"
		},
		{
			"etask.entity": "sc018738",
			"id": "B0913102-CB75-EB35-0FE9-B296C2BCCFED"
		},
		{
			"etask.entity": "sc018739",
			"id": "5F8BBAC4-BF72-8AFF-AE2C-DA578B8082B5"
		},
		{
			"etask.entity": "sc018740",
			"id": "CB1045A0-43A8-AB80-8C6E-CBE6F7766123"
		},
		{
			"etask.entity": "sc018741",
			"id": "1EE8929D-78B8-4AD9-ACD2-36D06519A2BB"
		},
		{
			"etask.entity": "sc018742",
			"id": "A61C69D2-817C-F86D-7DB3-8DA837CA8CD5"
		},
		{
			"etask.entity": "sc018743",
			"id": "07CDA85B-CD2D-12EB-E450-1E0BAEF3C49B"
		},
		{
			"etask.entity": "sc018744",
			"id": "3DCA4F68-0563-3CA6-CE67-B05BBAE4E2EE"
		},
		{
			"etask.entity": "sc018745",
			"id": "6C8A0511-63D0-2A62-6F54-B1B969B79206"
		},
		{
			"etask.entity": "sc018746",
			"id": "2AC172AB-AEF7-F3D8-13EA-BC9D5DA9FB55"
		},
		{
			"etask.entity": "sc018747",
			"id": "D43741EB-18CD-305B-926A-866F01109EE8"
		},
		{
			"etask.entity": "sc018748",
			"id": "02EB9707-B818-DEDB-E38B-1446682AD440"
		},
		{
			"etask.entity": "sc018749",
			"id": "A81660A1-3AF1-0397-C09C-4E2C4CD13412"
		},
		{
			"etask.entity": "sc018750",
			"id": "F1E71246-6159-F961-9512-E8FD63F8EBE8"
		},
		{
			"etask.entity": "sc018751",
			"id": "CA3BB84A-ADDD-C9F4-EAF8-6ACDB2AA2896"
		},
		{
			"etask.entity": "sc018752",
			"id": "26A8012B-396F-53EA-1B34-11CAFC989760"
		},
		{
			"etask.entity": "sc018753",
			"id": "4E34D987-9855-7812-368B-5A7284F22D0F"
		},
		{
			"etask.entity": "sc018754",
			"id": "431D5026-B994-987D-ECF5-65583ABA002E"
		},
		{
			"etask.entity": "sc018755",
			"id": "E38BB3F4-54A0-7B71-56F0-D414EB04D149"
		},
		{
			"etask.entity": "sc018756",
			"id": "CCBE7C1C-1E3C-F562-78A3-51F937327632"
		},
		{
			"etask.entity": "sc018757",
			"id": "98BFAA27-D9CD-CE39-5037-0AB507D68EB4"
		},
		{
			"etask.entity": "sc018758",
			"id": "1609ECF1-1522-3696-0F69-FF6A29A75FFD"
		},
		{
			"etask.entity": "sc018759",
			"id": "D00D88DD-97A0-4699-4B3E-9F28D32D33E7"
		},
		{
			"etask.entity": "sc018760",
			"id": "8F45D370-89B4-002A-5976-4170D0B1699C"
		},
		{
			"etask.entity": "sc018761",
			"id": "DDC3C270-EDE6-D198-1D58-85B7012FB50E"
		},
		{
			"etask.entity": "sc018762",
			"id": "D90B5947-ACA4-D8C0-D2DE-692A15F8E20B"
		},
		{
			"etask.entity": "sc018763",
			"id": "6F27E9E2-44C4-4C8C-3737-955BFEEF7571"
		},
		{
			"etask.entity": "sc018764",
			"id": "3BEB54A0-BB9A-5EF9-7199-08D4472C7B78"
		},
		{
			"etask.entity": "sc018765",
			"id": "CAAB1A01-99FD-8B72-C0CF-C62F1255EA0B"
		},
		{
			"etask.entity": "sc018766",
			"id": "44256135-F788-F59D-7848-8E0FD5158760"
		},
		{
			"etask.entity": "sc018767",
			"id": "E77B4FAC-D795-CE79-2CC4-0898DD2CEF15"
		},
		{
			"etask.entity": "sc018768",
			"id": "B8395C8D-8FB1-3CA6-8507-52FA152E8DB5"
		},
		{
			"etask.entity": "sc018769",
			"id": "CD1F0959-4A0B-1169-810E-C51E03C66CDB"
		},
		{
			"etask.entity": "sc018770",
			"id": "4F12A9CF-E8E6-7F2D-895C-C2D61F186CAD"
		},
		{
			"etask.entity": "sc018771",
			"id": "EDA76ACD-C2B4-3B9F-ABF4-B0E33FB15AC3"
		},
		{
			"etask.entity": "sc018772",
			"id": "8D22F590-21B1-657A-B21E-01EAB706E798"
		},
		{
			"etask.entity": "sc018773",
			"id": "66ABA546-117C-4434-4564-D97B934AD0F1"
		},
		{
			"etask.entity": "sc018774",
			"id": "663B3728-4EF7-1743-C4E0-DB56326E2F8D"
		},
		{
			"etask.entity": "sc018775",
			"id": "85750951-1E89-971F-5F2B-9125C1933FB1"
		},
		{
			"etask.entity": "sc018776",
			"id": "F620047C-344A-F29B-C4DD-57FB53B793D0"
		},
		{
			"etask.entity": "sc018777",
			"id": "D8E3A433-3443-A68C-39B0-02559B63E745"
		},
		{
			"etask.entity": "sc018778",
			"id": "8C20915B-A72B-03F1-236A-4701B4634F54"
		},
		{
			"etask.entity": "sc018779",
			"id": "C2898268-A78B-963E-25F0-89C559C4B8F7"
		},
		{
			"etask.entity": "sc018780",
			"id": "5BF1CB85-BA2E-1EB4-FCB1-8EA37CE51377"
		},
		{
			"etask.entity": "sc018781",
			"id": "6886D803-8C6E-6112-0F9B-FE4D91EC0F62"
		},
		{
			"etask.entity": "sc018782",
			"id": "065C9B54-005F-841B-0D5A-6E171FBE4F97"
		},
		{
			"etask.entity": "sc018783",
			"id": "429D4BBD-845F-BCF6-1428-D563FBED4493"
		},
		{
			"etask.entity": "sc018784",
			"id": "6461FF18-4ADD-C0D3-1324-BD8DE1CEB0E8"
		},
		{
			"etask.entity": "sc018785",
			"id": "5BD568FB-8A0F-6B2E-6901-488212674545"
		},
		{
			"etask.entity": "sc018786",
			"id": "0DEA4A28-EE2F-C579-5C17-5148B76BD46B"
		},
		{
			"etask.entity": "sc018787",
			"id": "19D8AC81-8DC0-415E-A937-F423063273D0"
		},
		{
			"etask.entity": "sc018788",
			"id": "62235179-5FCA-4E12-A404-917044CA4C89"
		},
		{
			"etask.entity": "sc018789",
			"id": "3508135D-F3DF-08D7-4DE9-292AF5E8C290"
		},
		{
			"etask.entity": "sc018790",
			"id": "03AB8F3C-3184-14E9-AF56-529510536672"
		},
		{
			"etask.entity": "sc018791",
			"id": "D4F4FCB1-4E15-CB3A-A6DD-D7B879E1E30A"
		},
		{
			"etask.entity": "sc018792",
			"id": "0B31976A-88C7-D7C9-0961-7ED21D4E9551"
		},
		{
			"etask.entity": "sc018793",
			"id": "C05504CE-D8D1-B46A-3BE8-22513237C813"
		},
		{
			"etask.entity": "sc018794",
			"id": "CE03AA62-2924-1DAD-9044-E3659E358366"
		},
		{
			"etask.entity": "sc018795",
			"id": "E106CEE9-CFFB-0268-610B-7161A3E1C928"
		},
		{
			"etask.entity": "sc018796",
			"id": "9C74615E-A193-6E98-76D1-6DFD7D67D405"
		},
		{
			"etask.entity": "sc018797",
			"id": "D27A7382-6FFF-6AEA-93E7-9ABEDB7AC3E1"
		},
		{
			"etask.entity": "sc018798",
			"id": "63628353-270F-09F0-1096-3F1E16445DDE"
		},
		{
			"etask.entity": "sc018799",
			"id": "94CDA701-0BD6-AB78-1D78-EE4751B3CE8A"
		},
		{
			"etask.entity": "sc018800",
			"id": "B7BD0488-3022-B1A0-B76D-44BA16A265B6"
		},
		{
			"etask.entity": "sc018801",
			"id": "11887E4C-2914-E487-41F0-6611BD2909A6"
		},
		{
			"etask.entity": "sc018802",
			"id": "BE06C9A0-2FED-11A9-50CD-FD32646D3308"
		},
		{
			"etask.entity": "sc018803",
			"id": "27FA44DC-9833-CC20-4EF9-BBD17A64D6FC"
		},
		{
			"etask.entity": "sc018804",
			"id": "8898D9A3-7598-557A-1913-A2D31A37FC12"
		},
		{
			"etask.entity": "sc018805",
			"id": "52199DBE-4A39-6313-3A2A-40083929236E"
		},
		{
			"etask.entity": "sc018806",
			"id": "41BAFA80-836B-E2CB-8BD0-855BFB718608"
		},
		{
			"etask.entity": "sc018807",
			"id": "CCD9993F-D7BE-F426-3803-B38D5302A8B7"
		},
		{
			"etask.entity": "sc018808",
			"id": "D14C47D3-27E8-34F5-AC0B-EBDD291FEC9F"
		},
		{
			"etask.entity": "sc018809",
			"id": "0044833D-770D-9D0D-89E7-7EB342FF941A"
		},
		{
			"etask.entity": "sc018810",
			"id": "1417EB2A-0676-911D-14D4-AA4BEB7CE857"
		},
		{
			"etask.entity": "sc018811",
			"id": "52FC86AD-CF9A-B724-3ADD-1CD56C0EED41"
		},
		{
			"etask.entity": "sc018812",
			"id": "5A48D4D2-BDAF-C5DE-CE7E-E5A9B29B2ED0"
		},
		{
			"etask.entity": "sc018813",
			"id": "1B38C726-9B1C-4A54-AE25-A26ADC34F4C4"
		},
		{
			"etask.entity": "sc018814",
			"id": "BC7FEA4A-34BA-2667-7D84-D4AF4272711D"
		},
		{
			"etask.entity": "sc018815",
			"id": "2F41CD06-A613-47AC-4363-69DBDD87B84D"
		},
		{
			"etask.entity": "sc018816",
			"id": "729A544A-6A89-2BFB-C0EA-A62F737DA956"
		},
		{
			"etask.entity": "sc018817",
			"id": "D53F1E0D-D3EB-B987-1B2F-8F6D135BD4A6"
		},
		{
			"etask.entity": "sc018818",
			"id": "F7B4BE90-6068-B2A8-9371-5A6567BEB503"
		},
		{
			"etask.entity": "sc018819",
			"id": "FDE96803-DAB4-3770-29CD-CB9BC15F4014"
		},
		{
			"etask.entity": "sc018820",
			"id": "901427AD-AD3F-83F6-1F5A-485B85B924FE"
		},
		{
			"etask.entity": "sc018821",
			"id": "37C0A23E-D96C-8A83-9940-EFE558902BF4"
		},
		{
			"etask.entity": "sc018822",
			"id": "C8FB4F9F-591A-E79F-581E-85682A80CB2F"
		},
		{
			"etask.entity": "sc018823",
			"id": "1506DBA3-9734-B2CF-A8BD-3C8C228CEAC1"
		},
		{
			"etask.entity": "sc018824",
			"id": "3B421999-5491-30E0-0C96-A398AD3316C8"
		},
		{
			"etask.entity": "sc018825",
			"id": "B05142E2-1F01-D43C-7F2E-A4AC67298637"
		},
		{
			"etask.entity": "sc018826",
			"id": "B344133D-7156-1EF3-C5E2-70CF58210849"
		},
		{
			"etask.entity": "sc018827",
			"id": "F59BD5C2-9B90-EA1C-42BD-6B8FE68836B0"
		},
		{
			"etask.entity": "sc018828",
			"id": "45CB37B8-5017-BF75-9C0E-44A8434A0EE8"
		},
		{
			"etask.entity": "sc018829",
			"id": "DE65F627-BF23-1786-E95C-11130D41B9C1"
		},
		{
			"etask.entity": "sc018830",
			"id": "8A86C37C-5969-F8AC-F3FE-22F1BFAD2B04"
		},
		{
			"etask.entity": "sc018831",
			"id": "51B5B7F0-7A24-4ACD-70E2-938F53A4F634"
		},
		{
			"etask.entity": "sc018832",
			"id": "977C3E85-E5E4-8CD9-AC7E-3F4CA1037BBB"
		},
		{
			"etask.entity": "sc018833",
			"id": "BDAAC95D-E605-052F-7676-B2963911A29E"
		},
		{
			"etask.entity": "sc018834",
			"id": "64870851-4A38-9ED5-5E0A-3FC403C880CA"
		},
		{
			"etask.entity": "sc018835",
			"id": "BCA190D6-9915-719A-63FB-EF2CE3142016"
		},
		{
			"etask.entity": "sc018836",
			"id": "5226C1D5-43E5-E2CD-AF84-F734E88A9D87"
		},
		{
			"etask.entity": "sc018837",
			"id": "08B3AEB1-C393-9A32-C5FB-B1610A7E0715"
		},
		{
			"etask.entity": "sc018838",
			"id": "5F9C3524-407B-EE9E-4F42-1EFAF635B822"
		},
		{
			"etask.entity": "sc018839",
			"id": "7CF4C12B-D9AD-A25D-3649-8B62435618CB"
		},
		{
			"etask.entity": "sc018840",
			"id": "271398A0-F190-C551-0898-479D477C32A8"
		},
		{
			"etask.entity": "sc018841",
			"id": "B4F06A3E-BBAE-5071-C92A-9FDBC0F28990"
		},
		{
			"etask.entity": "sc018842",
			"id": "F42AFB14-B69E-6A9A-C181-86DCE2FAD973"
		},
		{
			"etask.entity": "sc018843",
			"id": "FCDC6826-8DCC-EE08-2C20-A97073EF9E70"
		},
		{
			"etask.entity": "sc018844",
			"id": "77C31F05-6975-33AC-1A3A-19AEFAF26663"
		},
		{
			"etask.entity": "sc018845",
			"id": "9B7AC9F3-67C1-BBAB-3241-3AFF12F28686"
		},
		{
			"etask.entity": "sc018846",
			"id": "61AFEC5F-D73A-4384-EF13-2216F3FAB39D"
		},
		{
			"etask.entity": "sc018847",
			"id": "A748BE96-F58D-26FE-D0C4-98CD8A46EFAE"
		},
		{
			"etask.entity": "sc018848",
			"id": "F8C73D0C-A31D-79F8-8267-3206017EBBDD"
		},
		{
			"etask.entity": "sc018849",
			"id": "AEFF02C0-39CD-3995-D116-66918A3EAF8B"
		},
		{
			"etask.entity": "sc018850",
			"id": "B05EEA8C-B3FE-6DD9-ECD1-4CDE3809B232"
		},
		{
			"etask.entity": "sc018851",
			"id": "01FA56B4-5748-A48D-4FA6-EFA73AD89E3A"
		},
		{
			"etask.entity": "sc018852",
			"id": "F72BA0C7-302C-80B5-BF46-F7539E01B0D7"
		},
		{
			"etask.entity": "sc018853",
			"id": "63A63AC8-4A6B-F675-80B4-437792D3886B"
		},
		{
			"etask.entity": "sc018854",
			"id": "8EA79A0D-6AD4-9C9A-895B-99A5294D3EDE"
		},
		{
			"etask.entity": "sc018855",
			"id": "8083CEDD-F21F-F198-0B67-24B5863FC84E"
		},
		{
			"etask.entity": "sc018856",
			"id": "82136065-EEAC-0AC1-3E5A-E78AF6520F23"
		},
		{
			"etask.entity": "sc018857",
			"id": "B556FA92-FBF7-8D17-B3FC-BC0FA4404FB1"
		},
		{
			"etask.entity": "sc018858",
			"id": "3AC239BD-17E7-26D2-4D74-C168FD44948D"
		},
		{
			"etask.entity": "sc018859",
			"id": "B211FC66-99D3-4DB2-A7A0-EE12E61D10CB"
		},
		{
			"etask.entity": "sc018860",
			"id": "DA70B673-BE9A-7859-C733-A9A5ED630E32"
		},
		{
			"etask.entity": "sc018861",
			"id": "EC68FF50-9E7C-7B4E-3BE0-B75393797F23"
		},
		{
			"etask.entity": "sc018862",
			"id": "5280A588-5008-9C71-7C38-0DA47383364A"
		},
		{
			"etask.entity": "sc018863",
			"id": "4E431E8E-FAA6-8A37-AE8D-71D86DD3EE6F"
		},
		{
			"etask.entity": "sc018864",
			"id": "3109E2D2-ED06-5080-412F-F52928AB7FC3"
		},
		{
			"etask.entity": "sc018865",
			"id": "3CD193F6-9B4F-5FF5-5E0D-162C546F01B3"
		},
		{
			"etask.entity": "sc018866",
			"id": "7C5F7668-96D8-6786-5209-947558880F12"
		},
		{
			"etask.entity": "sc018867",
			"id": "A863C27C-5A23-FED4-8F5B-80E455FB13CB"
		},
		{
			"etask.entity": "sc018868",
			"id": "7EA95CEA-157F-B438-6502-320ED1C873A3"
		},
		{
			"etask.entity": "sc018869",
			"id": "2F78CF5E-14A0-7D63-D6C2-9A6D96519226"
		},
		{
			"etask.entity": "sc018870",
			"id": "61F3D548-B3D2-3F0C-69BD-776A84B2A7AA"
		},
		{
			"etask.entity": "sc018871",
			"id": "E9D3F46D-1791-814B-2305-30EE7D552DA6"
		},
		{
			"etask.entity": "sc018872",
			"id": "EC15E0DA-EC4C-1F90-DA69-D683EBE17344"
		},
		{
			"etask.entity": "sc018873",
			"id": "3AE8D596-1225-A777-8FFB-FFBFD6640C3F"
		},
		{
			"etask.entity": "sc018874",
			"id": "87B409F2-ED30-78B5-E05E-23C9183B054A"
		},
		{
			"etask.entity": "sc018875",
			"id": "348A8D92-9796-B56A-86E8-90DEEB2A5CD6"
		},
		{
			"etask.entity": "sc018876",
			"id": "A08BC358-0971-D5D0-7FF6-890C7FA1B376"
		},
		{
			"etask.entity": "sc018877",
			"id": "C8B00066-E149-950D-31C0-97DDB9FB8502"
		},
		{
			"etask.entity": "sc018878",
			"id": "522F47F5-D260-64C2-5362-E015EA99D0D6"
		},
		{
			"etask.entity": "sc018879",
			"id": "91A8E9C8-FCAB-6687-D0A3-9E399669D091"
		},
		{
			"etask.entity": "sc018880",
			"id": "62E28443-3981-E69C-6A86-5E191477C5F3"
		},
		{
			"etask.entity": "sc018881",
			"id": "ED446809-8721-115F-F6DB-C5018FEC1221"
		},
		{
			"etask.entity": "sc018882",
			"id": "8D14BD51-897D-8BB9-1256-4D3BE5CE1598"
		},
		{
			"etask.entity": "sc018883",
			"id": "426B5B86-137D-5527-FB38-55C8B734FEE9"
		},
		{
			"etask.entity": "sc018884",
			"id": "8E8B90A6-54B1-C0F9-A087-B48E68DC66FB"
		},
		{
			"etask.entity": "sc018885",
			"id": "6913D8CE-C156-E356-A21B-8B1159AC5B75"
		},
		{
			"etask.entity": "sc018886",
			"id": "A8499264-8B04-9CD0-9407-019718F6AF08"
		},
		{
			"etask.entity": "sc018887",
			"id": "1423EF95-4C46-328E-479A-95B3618C7527"
		},
		{
			"etask.entity": "sc018888",
			"id": "8E895B00-2723-D2E7-3FF1-F91D1325679A"
		},
		{
			"etask.entity": "sc018889",
			"id": "A70F580E-BAA3-2DD5-C99A-7138A1D0B730"
		},
		{
			"etask.entity": "sc018890",
			"id": "0F439AA6-835D-285B-7267-3F1748D4A095"
		},
		{
			"etask.entity": "sc018891",
			"id": "DE662827-EA78-DA82-260B-7D8656F4D147"
		},
		{
			"etask.entity": "sc018892",
			"id": "92F7C498-7E1D-A358-4263-F05AECD075E0"
		},
		{
			"etask.entity": "sc018893",
			"id": "685E7EEF-7F0C-8603-E382-CAEBD2E9A96C"
		},
		{
			"etask.entity": "sc018894",
			"id": "F64AD7E6-5C27-A219-6149-669CB39F0820"
		},
		{
			"etask.entity": "sc018895",
			"id": "C47491D2-46DD-274C-5500-0786CF697DCD"
		},
		{
			"etask.entity": "sc018896",
			"id": "C128D5F5-98E5-2501-0E77-5DB5F90B5D11"
		},
		{
			"etask.entity": "sc018897",
			"id": "DBFE0717-E2A4-8B7E-65CF-6FA2F870B10F"
		},
		{
			"etask.entity": "sc018898",
			"id": "80308332-BB6C-DEAA-D063-E99C2F915765"
		},
		{
			"etask.entity": "sc018899",
			"id": "3063EC7B-9647-FCA6-BED9-29F8CF81F432"
		},
		{
			"etask.entity": "sc018900",
			"id": "98D014E9-D483-2F2F-E4BC-18A036B5B127"
		},
		{
			"etask.entity": "sc018901",
			"id": "50F80AC6-BC2D-9753-694F-1A6377126BE4"
		},
		{
			"etask.entity": "sc018902",
			"id": "F0D40C1E-4AAD-6AA2-FAB4-299F9D15DD15"
		},
		{
			"etask.entity": "sc018903",
			"id": "C2865DD3-69F4-28F1-BF64-6B525DDF018A"
		},
		{
			"etask.entity": "sc018904",
			"id": "0253D34A-25E5-E3EC-E668-D361AD656DDF"
		},
		{
			"etask.entity": "sc018905",
			"id": "3BC54706-4E87-A7A1-FDB7-331824ACA24D"
		},
		{
			"etask.entity": "sc018906",
			"id": "419BC7AB-BAD0-26BC-16C6-BC1F429C552D"
		},
		{
			"etask.entity": "sc018907",
			"id": "D5B65F0C-5C24-A272-C663-260E0A5AED84"
		},
		{
			"etask.entity": "sc018908",
			"id": "759A8E58-5918-3E9E-9686-D47B85A189BD"
		},
		{
			"etask.entity": "sc018909",
			"id": "621113F0-F57A-DD0A-9C8E-219C350AB719"
		},
		{
			"etask.entity": "sc018910",
			"id": "78E9D5B5-5EFF-134C-CC75-044BB153E3E0"
		},
		{
			"etask.entity": "sc018911",
			"id": "A061C236-EE67-0D5D-BBD9-E13F509D891D"
		},
		{
			"etask.entity": "sc018912",
			"id": "21CBCB39-3AA5-3282-5041-CF30770A0A73"
		},
		{
			"etask.entity": "sc018913",
			"id": "B598089D-5C8A-18FD-7439-5E7F78915150"
		},
		{
			"etask.entity": "sc018914",
			"id": "EBD46B40-FFD3-3FCC-A684-29D9697C4697"
		},
		{
			"etask.entity": "sc018915",
			"id": "91C3AC20-7A03-7750-EA13-FFC7CF0AB20A"
		},
		{
			"etask.entity": "sc018916",
			"id": "C81D760B-3425-2844-67D4-FA91EB12CC71"
		},
		{
			"etask.entity": "sc018917",
			"id": "57FD81B1-4D87-BF73-14DE-B3C6E1629BE4"
		},
		{
			"etask.entity": "sc018918",
			"id": "826D4224-E43E-3AE1-4A30-BF9AB72C9221"
		},
		{
			"etask.entity": "sc018919",
			"id": "EB3C6897-5832-C5BF-5E29-197924DA5BDE"
		},
		{
			"etask.entity": "sc018920",
			"id": "216FF9A2-1243-3C38-C074-8F6667114BFB"
		},
		{
			"etask.entity": "sc018921",
			"id": "19ABA1BD-E8BC-409F-6E28-50C5AFF5846A"
		},
		{
			"etask.entity": "sc018922",
			"id": "91112E2B-1369-DF73-F5A5-31DB4BE2D009"
		},
		{
			"etask.entity": "sc018923",
			"id": "F3C4299A-6897-7303-653B-4E3CBAE6E4F0"
		},
		{
			"etask.entity": "sc018924",
			"id": "7C2AF6B2-2DED-C39B-3EA2-8C9992F986D4"
		},
		{
			"etask.entity": "sc018925",
			"id": "0AC5AFB5-EEEE-80A6-6F71-CF365A0E943E"
		},
		{
			"etask.entity": "sc018926",
			"id": "AA3FF635-2345-5827-E797-0028B0BF4721"
		},
		{
			"etask.entity": "sc018927",
			"id": "298940C5-4CD9-1DA0-5277-3EFDC53CF487"
		},
		{
			"etask.entity": "sc018928",
			"id": "E2FC16A7-0260-4755-64F3-A5BB4017E5E5"
		},
		{
			"etask.entity": "sc018929",
			"id": "7E11206F-83CD-877F-A703-01EA12C0DCD0"
		},
		{
			"etask.entity": "sc018930",
			"id": "A35419A1-E412-F026-8F51-3DCEFED810A4"
		},
		{
			"etask.entity": "sc018931",
			"id": "8F4F3215-DD50-C582-56CA-05B4221F4EA9"
		},
		{
			"etask.entity": "sc018932",
			"id": "A9B796E9-043D-29F5-2292-5EBC71CBB9D1"
		},
		{
			"etask.entity": "sc018933",
			"id": "D0195251-8513-BE41-A786-31DE5EFBD1E6"
		},
		{
			"etask.entity": "sc018934",
			"id": "282FD17C-6D5E-9474-5947-0DC0C44DD508"
		},
		{
			"etask.entity": "sc018935",
			"id": "F56E00F0-146D-4763-A1AB-E0CED20657AF"
		},
		{
			"etask.entity": "sc018936",
			"id": "A734BDCC-13FE-7B13-4A77-086C0647D5D2"
		},
		{
			"etask.entity": "sc018937",
			"id": "44203775-52F8-177C-0C9C-9DD8E4F65963"
		},
		{
			"etask.entity": "sc018938",
			"id": "D83750BE-4229-A302-B744-578BB99B9083"
		},
		{
			"etask.entity": "sc018939",
			"id": "8C726025-5175-48DC-F6E6-D772B37D8E3B"
		},
		{
			"etask.entity": "sc018940",
			"id": "60BA8DF2-17AF-A468-E057-09A2CBBB7AB2"
		},
		{
			"etask.entity": "sc018941",
			"id": "5DD034BD-88E7-1BC6-3496-BE41602A1E62"
		},
		{
			"etask.entity": "sc018942",
			"id": "4383B818-5FE8-848E-4FF9-7DFFA293D8F3"
		},
		{
			"etask.entity": "sc018943",
			"id": "DF511D2C-5945-E5D6-6A6D-F5BA614C2B69"
		},
		{
			"etask.entity": "sc018944",
			"id": "13CEC076-B5FE-3C7A-0E75-40324975680D"
		},
		{
			"etask.entity": "sc018945",
			"id": "24FA9012-BEAC-4BAA-2CDF-0EF7327DE504"
		},
		{
			"etask.entity": "sc018946",
			"id": "71A44D37-B63C-26C2-A148-80C793F4C306"
		},
		{
			"etask.entity": "sc018947",
			"id": "BD8C4F2C-F20E-F66A-C106-B2D1BD5C00D2"
		},
		{
			"etask.entity": "sc018948",
			"id": "FDFBD911-CE65-2AD7-5497-D0387AA66902"
		},
		{
			"etask.entity": "sc018949",
			"id": "05FB60F6-988E-4C10-CEF0-045D7043C797"
		},
		{
			"etask.entity": "sc018950",
			"id": "1009AD9F-F584-A880-1DBE-004691B92483"
		},
		{
			"etask.entity": "sc018951",
			"id": "C2883C2F-5E62-B4C4-3D34-EAF1141A285A"
		},
		{
			"etask.entity": "sc018952",
			"id": "00726A80-20FD-5869-108A-74DD4BE09BF6"
		},
		{
			"etask.entity": "sc018953",
			"id": "A9DCC897-F104-CC6A-0C31-34C50F746495"
		},
		{
			"etask.entity": "sc018954",
			"id": "56E38C08-238E-F31A-5428-F72865DF152C"
		},
		{
			"etask.entity": "sc018955",
			"id": "29803BA3-EFC4-FF3B-09EF-FADF91EBC489"
		},
		{
			"etask.entity": "sc018956",
			"id": "1B5BBEA5-AF46-F750-A2AD-EE133273C89E"
		},
		{
			"etask.entity": "sc018957",
			"id": "F40CD6A2-CD6C-7F70-86F6-30B7BADDBC71"
		},
		{
			"etask.entity": "sc018958",
			"id": "2EF84760-0B6A-6C37-CBF3-4193C0C91156"
		},
		{
			"etask.entity": "sc018959",
			"id": "4D2A3E8F-919E-DB7B-708C-B4B8A572C0BF"
		},
		{
			"etask.entity": "sc018960",
			"id": "70E11784-950F-4F0F-456E-020B5356E427"
		},
		{
			"etask.entity": "sc018961",
			"id": "2D8D1D46-24E8-1176-6BC2-8566B16ECD46"
		},
		{
			"etask.entity": "sc018962",
			"id": "8BCAF280-95A0-9378-4336-0F2CD96BC086"
		},
		{
			"etask.entity": "sc018963",
			"id": "317914F3-8440-89FA-7FD3-1488C6C754AA"
		},
		{
			"etask.entity": "sc018964",
			"id": "7D88BD6E-886E-6CE8-BC8B-1D62CF88CB8C"
		},
		{
			"etask.entity": "sc018965",
			"id": "5F023FFB-213E-019B-B25C-9549337F2F3F"
		},
		{
			"etask.entity": "sc018966",
			"id": "35948010-0C1D-90B2-EE89-7B3B7203F9AB"
		},
		{
			"etask.entity": "sc018967",
			"id": "B19C063F-D00D-18FE-0CD7-286103D452FB"
		},
		{
			"etask.entity": "sc018968",
			"id": "C4B4F0E5-776F-8F18-A8CE-0250519F905B"
		},
		{
			"etask.entity": "sc018969",
			"id": "7C3C09AA-12F6-7BE7-6393-6BA8EE9C7F99"
		},
		{
			"etask.entity": "sc018970",
			"id": "410C37CC-671B-F968-A7D8-92A8E8F0BCF8"
		},
		{
			"etask.entity": "sc018971",
			"id": "67393877-EA6A-FFC3-E7BE-DF6484B0B294"
		},
		{
			"etask.entity": "sc018972",
			"id": "2EB624A2-0113-DF5E-DBF3-29252996F93B"
		},
		{
			"etask.entity": "sc018973",
			"id": "A45E1652-4421-7A7E-D27A-1EFC81F90485"
		},
		{
			"etask.entity": "sc018974",
			"id": "DD9B8FCA-4CD8-E458-4B96-09FCD4056987"
		},
		{
			"etask.entity": "sc018975",
			"id": "7F3A3A52-3D3F-ABA7-F820-8B1978E6A3C7"
		},
		{
			"etask.entity": "sc018976",
			"id": "21ADBF7E-56B2-AEF0-A35B-7BA1A02270FE"
		},
		{
			"etask.entity": "sc018977",
			"id": "4133E581-FBC2-1A41-8605-F11496C54899"
		},
		{
			"etask.entity": "sc018978",
			"id": "0DF63668-A2AA-ABD5-4248-D9E7D8BE4147"
		},
		{
			"etask.entity": "sc018979",
			"id": "00C4480C-99D9-9F49-A579-CF35FA4361E5"
		},
		{
			"etask.entity": "sc018980",
			"id": "41DBFA18-D8B7-3495-DFB2-27DD132796ED"
		},
		{
			"etask.entity": "sc018981",
			"id": "6A7376BE-D2D1-A603-874D-5CD426C2B457"
		},
		{
			"etask.entity": "sc018982",
			"id": "C58BA007-F253-10DD-3D75-4F0772B9151A"
		},
		{
			"etask.entity": "sc018983",
			"id": "CD986262-8361-41F9-B9F4-3E3547C5A0B3"
		},
		{
			"etask.entity": "sc018984",
			"id": "5BC6DC83-C4D6-063F-3411-854A052D7824"
		},
		{
			"etask.entity": "sc018985",
			"id": "02E6813D-7B89-EA35-713D-2B1A991546E4"
		},
		{
			"etask.entity": "sc018986",
			"id": "97265DC0-3B25-CB26-C850-0754FBDFAE46"
		},
		{
			"etask.entity": "sc018987",
			"id": "D1C5E2B4-D380-5972-FFCB-5A6604F4F9CA"
		},
		{
			"etask.entity": "sc018988",
			"id": "CFC6155B-7628-44F5-A644-70C79DBE39C9"
		},
		{
			"etask.entity": "sc018989",
			"id": "D433E5DF-FCD6-C2C1-3676-EB6F587BFA18"
		},
		{
			"etask.entity": "sc018990",
			"id": "82058A88-5E4B-8549-1E63-47B13BA9488E"
		},
		{
			"etask.entity": "sc018991",
			"id": "98E9A3EF-245B-5017-F4A2-90860ADC403A"
		},
		{
			"etask.entity": "sc018992",
			"id": "3A93F33B-85BD-396E-0A88-FB8134641FD2"
		},
		{
			"etask.entity": "sc018993",
			"id": "60244D32-D70F-A6D9-7781-50C591CF8BB1"
		},
		{
			"etask.entity": "sc018994",
			"id": "F847BAD7-87DD-DB56-C5CB-D998273292D7"
		},
		{
			"etask.entity": "sc018995",
			"id": "01175FAF-2B20-512D-02E0-8525D7BE68B4"
		},
		{
			"etask.entity": "sc018996",
			"id": "3359C2C9-B2B1-F491-9CBB-7F32FFC5919F"
		},
		{
			"etask.entity": "sc018997",
			"id": "7A31ADEB-0B89-75B4-AD30-D87E5F2FAF11"
		},
		{
			"etask.entity": "sc018998",
			"id": "95BAE847-9A8B-EA30-BA1C-A04AB1689AB1"
		},
		{
			"etask.entity": "sc018999",
			"id": "D7401AEE-EC1C-7513-B1C1-302C68089C30"
		},
		{
			"etask.entity": "sc019000",
			"id": "A20F6945-7B1F-A608-2237-6277E48EB126"
		},
		{
			"etask.entity": "sc019001",
			"id": "22208FD7-B9D9-36C9-0233-995C5BEA0A26"
		},
		{
			"etask.entity": "sc019002",
			"id": "848E7C33-9417-FB95-7FD7-D4D1A0B33731"
		},
		{
			"etask.entity": "sc019003",
			"id": "5E780D90-73E9-36B9-3BEE-9A632CAB709D"
		},
		{
			"etask.entity": "sc019004",
			"id": "8C63EB42-D1E7-F525-F07B-6E12A5B15B1F"
		},
		{
			"etask.entity": "sc019005",
			"id": "FE9232A5-7648-0EA7-9397-3255151F3D7E"
		},
		{
			"etask.entity": "sc019006",
			"id": "AAB1D62F-0D05-371F-5958-C07F5E296590"
		},
		{
			"etask.entity": "sc019007",
			"id": "38C85D55-219B-E09A-B8E4-1B6500CD8C8F"
		},
		{
			"etask.entity": "sc019008",
			"id": "66154AA7-7991-AD10-1456-0BBBFD12C8D5"
		},
		{
			"etask.entity": "sc019009",
			"id": "89212E32-6DA4-0C50-961E-376EE8E5DBFA"
		},
		{
			"etask.entity": "sc019010",
			"id": "4CF10034-6FE1-7E03-0F36-1C2816A99E51"
		},
		{
			"etask.entity": "sc019011",
			"id": "DEDF1B08-9B44-8E01-9FD6-97D93D8901B5"
		},
		{
			"etask.entity": "sc019012",
			"id": "589CE5FF-78D7-9374-275B-E19B5E8AF958"
		},
		{
			"etask.entity": "sc019013",
			"id": "17BD9AA9-4631-C3FE-7B80-BB0706165B33"
		},
		{
			"etask.entity": "sc019014",
			"id": "13CFEB15-9140-0179-5C67-72688B85C93B"
		},
		{
			"etask.entity": "sc019015",
			"id": "A133D7A8-FC84-6B94-89A7-D4F47453EF79"
		},
		{
			"etask.entity": "sc019016",
			"id": "8787F33E-43C5-E0F6-AA4A-923973F70715"
		},
		{
			"etask.entity": "sc019017",
			"id": "BCC9F292-58FE-C7DA-6E9D-1B9C323DE20B"
		},
		{
			"etask.entity": "sc019018",
			"id": "BDB45BE8-7CCB-1A3A-F4A7-76A030B71DDC"
		},
		{
			"etask.entity": "sc019019",
			"id": "09ED3EBA-0F17-CDBD-F239-8855BFE5F9E2"
		},
		{
			"etask.entity": "sc019020",
			"id": "F6FAEB52-CD66-73D6-9074-C8365B8C9689"
		},
		{
			"etask.entity": "sc019021",
			"id": "9916BD9E-A63F-3280-F857-CFFF491125A3"
		},
		{
			"etask.entity": "sc019022",
			"id": "B6C7AF22-85A5-3ED0-EE0B-0D0036A56F61"
		},
		{
			"etask.entity": "sc019023",
			"id": "8523FD30-9EFD-4BF5-622F-009DF7BD76D4"
		},
		{
			"etask.entity": "sc019024",
			"id": "90B3F700-5E07-D835-9AB4-9A719FB0366C"
		},
		{
			"etask.entity": "sc019025",
			"id": "D98392DE-07CB-B1F0-CB12-04F1AB249DEA"
		},
		{
			"etask.entity": "sc019026",
			"id": "7E58E585-34E2-1B34-B467-0F5D82459DBE"
		},
		{
			"etask.entity": "sc019027",
			"id": "A3E13E13-2A08-6682-43EB-D206C0AF4C25"
		},
		{
			"etask.entity": "sc019028",
			"id": "6324DC0F-F39B-549E-638B-10B4F24FDDE9"
		},
		{
			"etask.entity": "sc019029",
			"id": "640F55EC-265D-6EBB-E19F-2254806C9D4E"
		},
		{
			"etask.entity": "sc019030",
			"id": "6EEF0053-7844-97A3-6B91-C27486AA93B3"
		},
		{
			"etask.entity": "sc019031",
			"id": "4E1CC2D4-CBB9-91E2-7FBD-BDA8E273ED4F"
		},
		{
			"etask.entity": "sc019032",
			"id": "8F9DBDB1-841B-C13A-9AEC-3F6007D7D152"
		},
		{
			"etask.entity": "sc019033",
			"id": "4DED8DCB-BE73-1970-D6C4-702D6B610B7B"
		},
		{
			"etask.entity": "sc019034",
			"id": "759931F7-8FFA-9FC9-D005-F8891C3A8AFC"
		},
		{
			"etask.entity": "sc019035",
			"id": "7FB6F9DB-A645-77D5-821F-02A460148316"
		},
		{
			"etask.entity": "sc019036",
			"id": "DBE76CCC-DC71-0E9D-35F5-E40831747819"
		},
		{
			"etask.entity": "sc019037",
			"id": "86652A16-887E-13B0-A68C-0807198729B2"
		},
		{
			"etask.entity": "sc019038",
			"id": "EFBC98E2-5A93-2B4B-0D1D-F81582487E16"
		},
		{
			"etask.entity": "sc019039",
			"id": "E3D1171A-8275-82E6-D38F-16EE1CB085CD"
		},
		{
			"etask.entity": "sc019040",
			"id": "8DFD3C75-9B3C-26A6-1BE0-4D7168E144F9"
		},
		{
			"etask.entity": "sc019041",
			"id": "CA354009-541F-D81A-CB62-175B814F5DE5"
		},
		{
			"etask.entity": "sc019042",
			"id": "E7EB63FD-5B72-5EEF-841D-42C43AE322A2"
		},
		{
			"etask.entity": "sc019043",
			"id": "1F8EB47A-77BF-6693-9FDC-88FBBF174BA0"
		},
		{
			"etask.entity": "sc019044",
			"id": "C42C2532-2E37-7BC4-4065-7CE3C2BAD303"
		},
		{
			"etask.entity": "sc019045",
			"id": "F4CDCA76-5ED6-074C-644E-B8E40244B2B3"
		},
		{
			"etask.entity": "sc019046",
			"id": "41DEEC82-E7C1-694D-3F89-67F343CF232E"
		},
		{
			"etask.entity": "sc019047",
			"id": "DC6750D1-E2D4-BD8F-FDEC-064CBDCA5305"
		},
		{
			"etask.entity": "sc019048",
			"id": "36B746DA-E447-320D-4085-A6FCB5B25BC7"
		},
		{
			"etask.entity": "sc019049",
			"id": "FEF86BCE-02E2-CFE0-526F-97389D98AC62"
		},
		{
			"etask.entity": "sc019050",
			"id": "6C257D74-7F51-5EA7-AEEE-8483BDB523DD"
		},
		{
			"etask.entity": "sc019051",
			"id": "E0D610E3-E91A-AD21-A5EC-9F2FBB839E70"
		},
		{
			"etask.entity": "sc019052",
			"id": "9649657F-B724-98C3-82C0-555D38B8136E"
		},
		{
			"etask.entity": "sc019053",
			"id": "56A2F5F7-796B-AA5A-1A6D-C9F92A630810"
		},
		{
			"etask.entity": "sc019054",
			"id": "FC41955E-FFD6-00AF-0020-EE8BA4E8C8B3"
		},
		{
			"etask.entity": "sc019055",
			"id": "62192C63-50A4-913A-74F5-EFA746FF6291"
		},
		{
			"etask.entity": "sc019056",
			"id": "CBD81E72-ADEA-418A-9B7A-7A6B1E5EC82D"
		},
		{
			"etask.entity": "sc019057",
			"id": "F8DD2A16-6EDB-54CE-BD98-31528CECEA6A"
		},
		{
			"etask.entity": "sc019058",
			"id": "8C861520-0470-F312-3902-53D53E987BBF"
		},
		{
			"etask.entity": "sc019059",
			"id": "AE3A5C28-057A-ECE7-1983-A69DD2DCC780"
		},
		{
			"etask.entity": "sc019060",
			"id": "6AB81240-CCF1-4177-1A93-11D0C7D535AA"
		},
		{
			"etask.entity": "sc019061",
			"id": "9431E06F-EE7A-41C7-2442-DBB49608375F"
		},
		{
			"etask.entity": "sc019062",
			"id": "0BCCFAEF-1A86-D4DF-7DEC-B069FD6FB9BD"
		},
		{
			"etask.entity": "sc019063",
			"id": "23DB827E-83E5-BEFB-E83C-4797D4D1BC86"
		},
		{
			"etask.entity": "sc019064",
			"id": "69914BF7-E44D-DD55-E5AD-DC8D423FB685"
		},
		{
			"etask.entity": "sc019065",
			"id": "AD01B95E-4C09-8E10-F12E-3E5FD3F21D04"
		},
		{
			"etask.entity": "sc019066",
			"id": "D47D16B1-050E-BE90-AA7D-7E47AF99C5A5"
		},
		{
			"etask.entity": "sc019067",
			"id": "D184CE3E-4650-3969-E3AA-9ED039AE5CBC"
		},
		{
			"etask.entity": "sc019068",
			"id": "E04A2428-CB12-0B0B-A5B0-25B7F56047E3"
		},
		{
			"etask.entity": "sc019069",
			"id": "EE44A93C-8888-E6A9-3A9D-C4CC0A781F2F"
		},
		{
			"etask.entity": "sc019070",
			"id": "893B36CA-2965-57BC-F9BD-2EA3DF520B8D"
		},
		{
			"etask.entity": "sc019071",
			"id": "62B16383-C66A-0105-3903-678DE86CB257"
		},
		{
			"etask.entity": "sc019072",
			"id": "FC583192-9527-45A4-797B-94F9A3CE7373"
		},
		{
			"etask.entity": "sc019073",
			"id": "9686E2F9-5E8D-BA78-A956-80E2569DC241"
		},
		{
			"etask.entity": "sc019074",
			"id": "4F8796E5-66C3-4D33-18AB-2084601EB519"
		},
		{
			"etask.entity": "sc019075",
			"id": "AF490701-5D71-9509-B987-0B032C4D1DFE"
		},
		{
			"etask.entity": "sc019076",
			"id": "3251E513-1226-88DC-D668-FBDD16168B10"
		},
		{
			"etask.entity": "sc019077",
			"id": "EC5CF0D3-74B1-8419-7014-6A9A50DD91D0"
		},
		{
			"etask.entity": "sc019078",
			"id": "D21E4EBC-E551-AE7D-689C-E7DC64A5E5A9"
		},
		{
			"etask.entity": "sc019079",
			"id": "9C72EA52-5924-6273-BA25-1DE95233FA05"
		},
		{
			"etask.entity": "sc019080",
			"id": "AEBEDED9-D491-E180-329F-73A0FFDAE292"
		},
		{
			"etask.entity": "sc019081",
			"id": "D8C270A1-FA99-1FC6-804A-038BE4723522"
		},
		{
			"etask.entity": "sc019082",
			"id": "EE938D11-D561-F917-5891-7D367318A764"
		},
		{
			"etask.entity": "sc019083",
			"id": "1C76AF7C-8ED2-A340-5E4C-7FCCD3B08017"
		},
		{
			"etask.entity": "sc019084",
			"id": "B9F42338-A614-EF20-68DD-0084C29BA462"
		},
		{
			"etask.entity": "sc019085",
			"id": "A9C9F7BB-DFB2-B5C0-7DBE-26F924940392"
		},
		{
			"etask.entity": "sc019086",
			"id": "215E05DE-6DE3-6F94-7D76-5E039A80ACF5"
		},
		{
			"etask.entity": "sc019087",
			"id": "6363BF07-FE2D-AB7D-883B-1B877BB40878"
		},
		{
			"etask.entity": "sc019088",
			"id": "435C26C1-7738-6944-FF83-D60122535B80"
		},
		{
			"etask.entity": "sc019089",
			"id": "E1C6F39A-F3CE-8205-AD02-5C3AF4A20AEB"
		},
		{
			"etask.entity": "sc019090",
			"id": "1604553D-5F9F-292D-C59D-6A34389C7E80"
		},
		{
			"etask.entity": "sc019091",
			"id": "FF0EB01E-7C4D-13BD-AD6A-B155A43E976D"
		},
		{
			"etask.entity": "sc019092",
			"id": "DB8A7A4D-E3F5-76DE-C6C1-47DFA41D487E"
		},
		{
			"etask.entity": "sc019093",
			"id": "A3058D2C-0EA2-C5A1-F8D4-4CD268BA6B7F"
		},
		{
			"etask.entity": "sc019094",
			"id": "D94E8C7D-A9FA-0B40-1E72-B2CF5856703E"
		},
		{
			"etask.entity": "sc019095",
			"id": "5B666BF0-CB07-0D14-D495-1BBFEDFBA986"
		},
		{
			"etask.entity": "sc019096",
			"id": "C22C87B6-C507-277F-687C-0CE8A176ECDF"
		},
		{
			"etask.entity": "sc019097",
			"id": "BFD2F85A-66D2-7FCD-C3CC-9681EBE729E7"
		},
		{
			"etask.entity": "sc019098",
			"id": "32F2F1BA-2F69-74F7-3D81-A60C0093C1C1"
		},
		{
			"etask.entity": "sc019099",
			"id": "1B6FE721-D7A8-380D-5C4F-35E92F97841F"
		},
		{
			"etask.entity": "sc019100",
			"id": "A6E8CDCF-86B0-FD56-8AB2-A8C0D75F62E3"
		},
		{
			"etask.entity": "sc019101",
			"id": "C5788437-3B54-6D33-A311-60AE83187185"
		},
		{
			"etask.entity": "sc019102",
			"id": "DAC24DA0-AC6A-C0ED-54DE-C9BD7D7C4472"
		},
		{
			"etask.entity": "sc019103",
			"id": "D3A95C43-BE4F-6427-E9D0-C8EF6E4DDEEC"
		},
		{
			"etask.entity": "sc019104",
			"id": "57AD8CBF-D020-A145-1CD4-6EEB5FCDACBA"
		},
		{
			"etask.entity": "sc019105",
			"id": "72136D7B-BFD1-8C1B-0855-485F84FFBECC"
		},
		{
			"etask.entity": "sc019106",
			"id": "836AC4F5-3E76-EC97-D35E-BB3E1F4ACB06"
		},
		{
			"etask.entity": "sc019107",
			"id": "47122718-1A49-F42C-7045-B4127C5C3E4E"
		},
		{
			"etask.entity": "sc019108",
			"id": "179F58AE-7B19-73F0-8CB0-B4CF046D3063"
		},
		{
			"etask.entity": "sc019109",
			"id": "812E3E37-F23B-3C33-593E-71E52F3E59A1"
		},
		{
			"etask.entity": "sc019110",
			"id": "7CF81D70-3E52-22CA-1BC5-FDBB4C7A9B62"
		},
		{
			"etask.entity": "sc019111",
			"id": "01AD19A4-5192-FF7B-AE9D-AC7232D87A43"
		},
		{
			"etask.entity": "sc019112",
			"id": "1A842200-4E6E-B2A6-BEA6-0BC06F5EAAD4"
		},
		{
			"etask.entity": "sc019113",
			"id": "1D16EB15-1F44-898E-985E-8A664821D276"
		},
		{
			"etask.entity": "sc019114",
			"id": "1A952571-BF15-A985-8121-A68FDC5F976B"
		},
		{
			"etask.entity": "sc019115",
			"id": "24379B58-84F7-2021-6875-2B4895F7CF60"
		},
		{
			"etask.entity": "sc019116",
			"id": "E09BDC59-451B-61F3-A75D-274719B5371E"
		},
		{
			"etask.entity": "sc019117",
			"id": "986DE607-1375-CFD1-3A10-A01870C929B6"
		},
		{
			"etask.entity": "sc019118",
			"id": "FDF77AF2-F1EF-A04E-E834-2C207F5286DA"
		},
		{
			"etask.entity": "sc019119",
			"id": "AA77B517-5313-19C3-C363-FD4B6E83BE92"
		},
		{
			"etask.entity": "sc019120",
			"id": "8D70C03A-AAA5-3579-4986-03218BD5EEE7"
		},
		{
			"etask.entity": "sc019121",
			"id": "A9B10753-CAB8-9C01-2507-7AAE30A876AA"
		},
		{
			"etask.entity": "sc019122",
			"id": "85604B5E-6520-D91C-CD55-FFE8602A8DBA"
		},
		{
			"etask.entity": "sc019123",
			"id": "5EF7EB0B-5DDC-E30B-B3D5-0525D48C90EF"
		},
		{
			"etask.entity": "sc019124",
			"id": "A87D987A-9151-D897-EA35-7E1328B18463"
		},
		{
			"etask.entity": "sc019125",
			"id": "8F430BAA-BB7A-72F7-44F4-3A1B55ACACBA"
		},
		{
			"etask.entity": "sc019126",
			"id": "2A3B74BC-CEA0-1A5E-244F-38D2CBB3119D"
		},
		{
			"etask.entity": "sc019127",
			"id": "E01A612A-D96D-1C28-A0C5-F02B09F1E1CB"
		},
		{
			"etask.entity": "sc019128",
			"id": "0D4C6103-CF2E-AE38-E2F9-DAE9F9855BC6"
		},
		{
			"etask.entity": "sc019129",
			"id": "C75D4212-F223-F938-82A0-FD59824C1D23"
		},
		{
			"etask.entity": "sc019130",
			"id": "5511E206-95D7-087B-333B-FEB97CD2758B"
		},
		{
			"etask.entity": "sc019131",
			"id": "38F34E54-F721-E60C-4607-46606D0253BD"
		},
		{
			"etask.entity": "sc019132",
			"id": "DB86F5BD-CB04-A130-9BCD-134DFD0DB933"
		},
		{
			"etask.entity": "sc019133",
			"id": "B2040DF5-4FA1-B36C-7508-749CBF0F1C3A"
		},
		{
			"etask.entity": "sc019134",
			"id": "727AABEA-9B5D-9217-8B05-F43F5892BA1A"
		},
		{
			"etask.entity": "sc019135",
			"id": "1E14B85F-13D2-BFE2-6444-90F32E22106E"
		},
		{
			"etask.entity": "sc019136",
			"id": "A026E965-B71B-19E1-4502-63C4AA138AEE"
		},
		{
			"etask.entity": "sc019137",
			"id": "D3D42600-96BC-DEBB-815B-FBBCA4F96811"
		},
		{
			"etask.entity": "sc019138",
			"id": "925F8FA6-50A1-2821-1744-F9CBECC57904"
		},
		{
			"etask.entity": "sc019139",
			"id": "B3C8EAA6-F512-AB78-75B7-432E16A95F6E"
		},
		{
			"etask.entity": "sc019140",
			"id": "3391F435-FFE6-C0A9-7DCD-FA54EE5DB72C"
		},
		{
			"etask.entity": "sc019141",
			"id": "9DB7EB3D-8058-B1E4-6DDA-CE6A56CE20E1"
		},
		{
			"etask.entity": "sc019142",
			"id": "95D75DDD-5996-7929-09C1-B4DBA0481BBE"
		},
		{
			"etask.entity": "sc019143",
			"id": "5F007414-15A4-5525-45F5-31951211AF83"
		},
		{
			"etask.entity": "sc019144",
			"id": "6E994BB9-6212-B8BF-02F0-2527F83B44EE"
		},
		{
			"etask.entity": "sc019145",
			"id": "D68BB7B7-C0A0-3E10-4BF8-6D257E65AE03"
		},
		{
			"etask.entity": "sc019146",
			"id": "0A5FAB9B-7F5D-EE75-6177-66EC25642673"
		},
		{
			"etask.entity": "sc019147",
			"id": "6D8DCFEC-8C7F-DBC6-0B37-D024A50352B0"
		},
		{
			"etask.entity": "sc019148",
			"id": "1585812F-CD18-719A-B242-18158D9C7504"
		},
		{
			"etask.entity": "sc019149",
			"id": "654F19A5-497D-8382-74D7-5912CE296ED6"
		},
		{
			"etask.entity": "sc019150",
			"id": "ACDC4DE0-6E19-25D1-1EC1-1F383F470AB7"
		},
		{
			"etask.entity": "sc019151",
			"id": "589885F2-C054-D4C6-74AD-3CEE695AA289"
		},
		{
			"etask.entity": "sc019152",
			"id": "2B75E97E-3D0A-1F69-5D89-3BFCD97BFE87"
		},
		{
			"etask.entity": "sc019153",
			"id": "D57B0881-A9D3-D659-C0C2-AB7284D58828"
		},
		{
			"etask.entity": "sc019154",
			"id": "8BB2F35E-79B8-AAE1-6EFD-02D4B090BF3A"
		},
		{
			"etask.entity": "sc019155",
			"id": "56431F7E-82D4-5C9D-B91E-8F6D055553D6"
		},
		{
			"etask.entity": "sc019156",
			"id": "C9551D99-3188-6147-9E4D-CC5502696D34"
		},
		{
			"etask.entity": "sc019157",
			"id": "E5E823EB-6A50-1874-9750-3E69550824D0"
		},
		{
			"etask.entity": "sc019158",
			"id": "C70A362C-56C6-61A6-184A-E2E553AD6516"
		},
		{
			"etask.entity": "sc019159",
			"id": "9CDD2DCB-F98C-0B17-FF49-BA6A65489BAB"
		},
		{
			"etask.entity": "sc019160",
			"id": "3916FBC8-EDE6-8773-F552-D697E048C197"
		},
		{
			"etask.entity": "sc019161",
			"id": "491A72ED-5E4D-FFE8-0ADF-34C7DCB2A65A"
		},
		{
			"etask.entity": "sc019162",
			"id": "75FEC311-70F3-0373-B7D2-B839DD72D7AF"
		},
		{
			"etask.entity": "sc019163",
			"id": "F0112842-C18A-4F84-5352-F4D52619E0DC"
		},
		{
			"etask.entity": "sc019164",
			"id": "ECCCA3BE-B73D-4C9C-EEA5-EC15B8C55DE7"
		},
		{
			"etask.entity": "sc019165",
			"id": "FD6D0A8D-2AA4-59A9-7668-403522DED985"
		},
		{
			"etask.entity": "sc019166",
			"id": "474D9C1B-4143-FD4D-0C6E-BE7804803A1D"
		},
		{
			"etask.entity": "sc019167",
			"id": "6AA672AA-652A-C34F-0A62-9600EFFF878C"
		},
		{
			"etask.entity": "sc019168",
			"id": "C7ADAF61-33C4-561C-A4BC-3937AB8AEBE6"
		},
		{
			"etask.entity": "sc019169",
			"id": "B6ED43BE-0973-75D1-2D8C-C6B83724FAAB"
		},
		{
			"etask.entity": "sc019170",
			"id": "38AD45AC-0197-1782-7E1F-FC6C131B3328"
		},
		{
			"etask.entity": "sc019171",
			"id": "AD520F60-B482-5396-C49E-B1D545E4F43D"
		},
		{
			"etask.entity": "sc019172",
			"id": "C6AD8BCB-0374-FA0A-7E3C-76555B306C56"
		},
		{
			"etask.entity": "sc019173",
			"id": "11233F89-E73A-48E4-EC4F-BF82267B9A7D"
		},
		{
			"etask.entity": "sc019174",
			"id": "5C45F258-8519-E33A-2831-DA096161455B"
		},
		{
			"etask.entity": "sc019175",
			"id": "F3093974-6B08-A5B0-B74B-AA90DE819564"
		},
		{
			"etask.entity": "sc019176",
			"id": "92025DB6-5480-2559-C483-F4F3131E97AB"
		},
		{
			"etask.entity": "sc019177",
			"id": "D57FD1E5-298D-9C18-CC05-61EA5E2E7E93"
		},
		{
			"etask.entity": "sc019178",
			"id": "919D6CD0-C155-D9D2-24D7-BEC0A1367FE6"
		},
		{
			"etask.entity": "sc019179",
			"id": "7D77D643-EC70-925E-2D6B-E650B66CA4EC"
		},
		{
			"etask.entity": "sc019180",
			"id": "81EECDF8-5F3D-35AF-DA7D-09AB3C14B9B2"
		},
		{
			"etask.entity": "sc019181",
			"id": "6CEB5F9B-5759-8C33-1CB6-FCB28C081040"
		},
		{
			"etask.entity": "sc019182",
			"id": "BEA32541-BE10-49B7-9C4C-6F4EF19B01BE"
		},
		{
			"etask.entity": "sc019183",
			"id": "05A4D586-A9D9-9CDA-FB13-AD47D8535FCE"
		},
		{
			"etask.entity": "sc019184",
			"id": "C2E1F7A6-8114-08D2-091E-BB9DE2B179F3"
		},
		{
			"etask.entity": "sc019185",
			"id": "A6172A1C-3F60-FEB8-CB16-FCBDD7C36A84"
		},
		{
			"etask.entity": "sc019186",
			"id": "5B02B8A8-6FAA-7C51-1CE1-682E569CA27B"
		},
		{
			"etask.entity": "sc019187",
			"id": "B8D2E223-28A5-87D1-93CA-E601369A00D2"
		},
		{
			"etask.entity": "sc019188",
			"id": "95F9F386-BDCE-2F2B-E2B5-2351BA11AB5C"
		},
		{
			"etask.entity": "sc019189",
			"id": "6C3CFB70-0430-C065-52A5-EF48E3D0072A"
		},
		{
			"etask.entity": "sc019190",
			"id": "67FFAA44-AC20-4BB9-7415-1C7119675AA7"
		},
		{
			"etask.entity": "sc019191",
			"id": "C5E74DF8-327E-98E7-469B-90222DB4DE2F"
		},
		{
			"etask.entity": "sc019192",
			"id": "716DA4A0-23E4-9399-8F60-786EC9D29FB5"
		},
		{
			"etask.entity": "sc019193",
			"id": "D359E604-2D43-A6FA-3AE8-2692623A0F04"
		},
		{
			"etask.entity": "sc019194",
			"id": "6304F3DD-FB30-BAE8-61D9-388CABF385AE"
		},
		{
			"etask.entity": "sc019195",
			"id": "807DBFF8-3D6B-ECE1-9A37-6836D19D62D6"
		},
		{
			"etask.entity": "sc019196",
			"id": "3FCE9C03-9DBB-17E4-02C2-43059DFE1D28"
		},
		{
			"etask.entity": "sc019197",
			"id": "9241BF2E-7106-2151-C194-AA14537ABF9A"
		},
		{
			"etask.entity": "sc019198",
			"id": "EA1ABAED-3D58-C9E7-4C60-3D6C642E78EA"
		},
		{
			"etask.entity": "sc019199",
			"id": "C3007C81-7425-46E3-68A9-58CE252B56E0"
		},
		{
			"etask.entity": "sc019200",
			"id": "DEB743E7-1CED-717C-5831-0BD3A5DFE582"
		},
		{
			"etask.entity": "sc019201",
			"id": "5FDCB695-611B-DFD0-1720-1FA4D84FD167"
		},
		{
			"etask.entity": "sc019202",
			"id": "89D0DC5A-F889-B9EB-B869-D90AB084ABB3"
		},
		{
			"etask.entity": "sc019203",
			"id": "3F59FA2A-95A8-C4DF-31D4-3661D39D6F13"
		},
		{
			"etask.entity": "sc019204",
			"id": "C94F9B70-45B5-FCA5-9103-EFCAF267D5E0"
		},
		{
			"etask.entity": "sc019205",
			"id": "F7A07181-1769-A657-08FA-F5CA61BF6BD3"
		},
		{
			"etask.entity": "sc019206",
			"id": "6AD3A659-AFDA-109D-F3A6-7B78E2FE940F"
		},
		{
			"etask.entity": "sc019207",
			"id": "97BDE9DE-40CE-80DD-581B-E5D45563A7B1"
		},
		{
			"etask.entity": "sc019208",
			"id": "3764AFD0-8ADD-9D98-F57C-EBD3359CC258"
		},
		{
			"etask.entity": "sc019209",
			"id": "AA1956B0-4BB5-6C1F-3BBB-1030E5974FE3"
		},
		{
			"etask.entity": "sc019210",
			"id": "E17F9A6B-E660-9B1F-07A9-873C2E3C40B1"
		},
		{
			"etask.entity": "sc019211",
			"id": "CB8EB036-FA36-3633-A462-0DA7B2B83AD3"
		},
		{
			"etask.entity": "sc019212",
			"id": "0DCFC116-B171-6370-6681-8DF94C4B304E"
		},
		{
			"etask.entity": "sc019213",
			"id": "2C0B9F06-0029-7CF7-D311-27693BF69FCB"
		},
		{
			"etask.entity": "sc019214",
			"id": "B59CDE7F-0992-8E1E-EFB5-AE7517246FA2"
		},
		{
			"etask.entity": "sc019215",
			"id": "DBEABC9B-4640-A5A7-8BDF-808D6C5094C6"
		},
		{
			"etask.entity": "sc019216",
			"id": "AC3B20EF-76D3-6061-BF66-DFCF36FFAEE9"
		},
		{
			"etask.entity": "sc019217",
			"id": "6F067978-F0FC-68B7-BA7F-9FED8559ABE4"
		},
		{
			"etask.entity": "sc019218",
			"id": "33798CDE-9EDA-D3B9-12C9-B794559E4660"
		},
		{
			"etask.entity": "sc019219",
			"id": "A6D2B69D-6047-4FC4-6AC1-DCB112F5D76C"
		},
		{
			"etask.entity": "sc019220",
			"id": "6BB96FF9-1126-982A-3DD2-28158A4256F4"
		},
		{
			"etask.entity": "sc019221",
			"id": "B90C1582-25A0-7012-0F0F-BDDCEB594088"
		},
		{
			"etask.entity": "sc019222",
			"id": "BD33066D-9E2A-5F14-EED7-3553800B6F32"
		},
		{
			"etask.entity": "sc019223",
			"id": "E8AAA0F0-53F7-C483-0713-09B02D76B411"
		},
		{
			"etask.entity": "sc019224",
			"id": "095015CD-2D60-EAAB-1B83-F18D31E8BD25"
		},
		{
			"etask.entity": "sc019225",
			"id": "6EDA5199-7E84-4DA4-A357-BE33D02FBD74"
		},
		{
			"etask.entity": "sc019226",
			"id": "D3777FFC-FA1B-C879-486C-87BE7EE790B9"
		},
		{
			"etask.entity": "sc019227",
			"id": "8489D01A-11D9-BC72-50D6-8AEE8E158058"
		},
		{
			"etask.entity": "sc019228",
			"id": "A5698684-50C7-7471-131B-BC17AF5FB4DD"
		},
		{
			"etask.entity": "sc019229",
			"id": "1B80BBB2-A182-195D-D933-42E5067F99E8"
		},
		{
			"etask.entity": "sc019230",
			"id": "94DE06DE-B2F5-5850-3863-E2CEC1F854F1"
		},
		{
			"etask.entity": "sc019231",
			"id": "81457468-7722-197C-C122-215140327943"
		},
		{
			"etask.entity": "sc019232",
			"id": "B09A654E-4B04-A5A1-7402-BC57CAA2FF48"
		},
		{
			"etask.entity": "sc019233",
			"id": "06E4B3DE-4C73-2735-C2C0-30CB4275B4EB"
		},
		{
			"etask.entity": "sc019234",
			"id": "47461A9D-6937-EFCF-D594-FC0D62F571C5"
		},
		{
			"etask.entity": "sc019235",
			"id": "476CCF10-3972-4F60-DBDB-342F853E3D93"
		},
		{
			"etask.entity": "sc019236",
			"id": "056A7ADF-A5B5-92FA-E2AB-DEE50DE042F6"
		},
		{
			"etask.entity": "sc019237",
			"id": "D6D1C3E3-4D44-6490-C21F-845152806648"
		},
		{
			"etask.entity": "sc019238",
			"id": "E6213841-7821-BAD9-5284-6102A30380ED"
		},
		{
			"etask.entity": "sc019239",
			"id": "1424989B-47F1-A79E-935F-0F83AEFBFCE2"
		},
		{
			"etask.entity": "sc019240",
			"id": "A98AD2BE-B1A0-7E3A-1C40-3011DAA4FCD2"
		},
		{
			"etask.entity": "sc019241",
			"id": "3233D7B8-6F21-1177-E529-0A09C3F46C49"
		},
		{
			"etask.entity": "sc019242",
			"id": "FABCF403-0974-74C6-D31F-2A6A09869233"
		},
		{
			"etask.entity": "sc019243",
			"id": "EEDCAA92-373A-C3E3-29FE-ABA131AC87D8"
		},
		{
			"etask.entity": "sc019244",
			"id": "ECE7ED1F-5BEB-A54C-6033-F9D6E285040A"
		},
		{
			"etask.entity": "sc019245",
			"id": "37CA1474-36F2-F4D5-3CDE-B0D653DFDD9A"
		},
		{
			"etask.entity": "sc019246",
			"id": "2A2404DD-DBB2-1886-BEBB-2CB256B25FE5"
		},
		{
			"etask.entity": "sc019247",
			"id": "2DDAB8C9-866E-0C99-0830-E40400EA4673"
		},
		{
			"etask.entity": "sc019248",
			"id": "F6DAB0C9-FCEF-B571-480C-749D32077FB1"
		},
		{
			"etask.entity": "sc019249",
			"id": "C71062B5-0777-861C-5300-059EF1383FA1"
		},
		{
			"etask.entity": "sc019250",
			"id": "B2616DEC-51F8-80DD-235E-3B206BCC3BD4"
		},
		{
			"etask.entity": "sc019251",
			"id": "5534A54D-C7A8-4F2A-CA32-179805F67A66"
		},
		{
			"etask.entity": "sc019252",
			"id": "F7B66357-7003-5FF1-7101-05905BEA1F88"
		},
		{
			"etask.entity": "sc019253",
			"id": "018D3E68-738C-7C49-59E6-8D089A1D0647"
		},
		{
			"etask.entity": "sc019254",
			"id": "1E1ADA4C-5628-3BD5-F318-6230472CFFE9"
		},
		{
			"etask.entity": "sc019255",
			"id": "65A6D446-1AAC-D172-7366-2F56B9BB67F0"
		},
		{
			"etask.entity": "sc019256",
			"id": "C00A0979-76DE-2451-3211-CFB22340BE55"
		},
		{
			"etask.entity": "sc019257",
			"id": "E13FB660-2F45-384D-F949-F5783CACBB75"
		},
		{
			"etask.entity": "sc019258",
			"id": "E2852948-DC46-2CA6-A75B-290C5C47F0C1"
		},
		{
			"etask.entity": "sc019259",
			"id": "2EAF1C4E-8B5B-E132-0727-E6B85EBFFB9C"
		},
		{
			"etask.entity": "sc019260",
			"id": "CA1B0803-CBE7-C7B7-C820-0F643CD79CE9"
		},
		{
			"etask.entity": "sc019261",
			"id": "C1B0E75A-F803-1598-FAE4-02704F6871F3"
		},
		{
			"etask.entity": "sc019262",
			"id": "35A36A0D-0682-11CF-A690-A41C27A2FC2C"
		},
		{
			"etask.entity": "sc019263",
			"id": "CEB7BCA5-2023-8FCC-47DF-B41426A06C94"
		},
		{
			"etask.entity": "sc019264",
			"id": "2F26EAC0-F59D-9094-D402-9237D98F1B62"
		},
		{
			"etask.entity": "sc019265",
			"id": "FFEA7862-872D-3294-2DF8-91D3F9D32D56"
		},
		{
			"etask.entity": "sc019266",
			"id": "C06538C4-169C-7FF7-6BE7-44FEDD24F812"
		},
		{
			"etask.entity": "sc019267",
			"id": "72551901-589E-C22E-05D9-5574E7AD5999"
		},
		{
			"etask.entity": "sc019268",
			"id": "8A0F6563-651E-B983-B2CC-4D11B82F6454"
		},
		{
			"etask.entity": "sc019269",
			"id": "3FD1503C-D8F7-4467-6720-518E95C1C0F1"
		},
		{
			"etask.entity": "sc019270",
			"id": "275ACB42-795C-134E-6D3F-3F86480E28A3"
		},
		{
			"etask.entity": "sc019271",
			"id": "DF107FC9-B203-1C3A-B7FA-EE237E5F7CB6"
		},
		{
			"etask.entity": "sc019272",
			"id": "210C76FA-1865-515B-4992-706B6CA892E8"
		},
		{
			"etask.entity": "sc019273",
			"id": "2F22BAF4-E351-29C4-EE6D-5A962611C920"
		},
		{
			"etask.entity": "sc019274",
			"id": "B08F3E22-30D5-E03A-D50A-8E68D06FB336"
		},
		{
			"etask.entity": "sc019275",
			"id": "089FFDFA-D636-B3B3-D89B-725F5DDD3241"
		},
		{
			"etask.entity": "sc019276",
			"id": "C787417A-B047-9C3E-8D1D-3A1414AC846C"
		},
		{
			"etask.entity": "sc019277",
			"id": "9F7027E6-2F0F-A149-CA13-1C87AC0F36DE"
		},
		{
			"etask.entity": "sc019278",
			"id": "5495EC1B-7FAB-65E9-422F-D79EA25581F4"
		},
		{
			"etask.entity": "sc019279",
			"id": "7E0397D2-3848-55F6-B86F-E5A151FFA4F7"
		},
		{
			"etask.entity": "sc019280",
			"id": "3902012B-D5E6-0477-9BF8-24E5D8706914"
		},
		{
			"etask.entity": "sc019281",
			"id": "AF556D0F-BA07-A656-7F03-BFFE2E7859B0"
		},
		{
			"etask.entity": "sc019282",
			"id": "7174F41C-D43D-31E0-6918-6BABB2E515AA"
		},
		{
			"etask.entity": "sc019283",
			"id": "7B73BCA4-5CAB-3858-E5A4-EEBD6A0DC6F3"
		},
		{
			"etask.entity": "sc019284",
			"id": "D54D2323-7580-CB51-9CDD-590247994AB4"
		},
		{
			"etask.entity": "sc019285",
			"id": "331816C6-160F-063B-02DF-80432D8617A6"
		},
		{
			"etask.entity": "sc019286",
			"id": "8246B6D1-D44B-91F1-EDDF-AE34BB40A0CE"
		},
		{
			"etask.entity": "sc019287",
			"id": "9932B251-62C8-E32B-144B-3D5DA0FEAADA"
		},
		{
			"etask.entity": "sc019288",
			"id": "2BAED243-87F8-CA9C-AC1E-ECBE02D426A0"
		},
		{
			"etask.entity": "sc019289",
			"id": "6B8EB00A-3892-154D-26E8-E3D81B648E31"
		},
		{
			"etask.entity": "sc019290",
			"id": "EE839DC0-DF20-332F-11C5-7E90B156C552"
		},
		{
			"etask.entity": "sc019291",
			"id": "CC2A82DE-9A90-1B96-6776-19078F30DDF7"
		},
		{
			"etask.entity": "sc019292",
			"id": "EDA59F21-ACC8-3169-6F9E-FFB8069CC2C0"
		},
		{
			"etask.entity": "sc019293",
			"id": "2250AEA1-113C-72E0-420B-3075720CDE17"
		},
		{
			"etask.entity": "sc019294",
			"id": "C971EAC3-68C5-2E3C-56E3-7D2594EB00F7"
		},
		{
			"etask.entity": "sc019295",
			"id": "382F4413-D1A5-D0F5-F1CF-F526B3F9FA9A"
		},
		{
			"etask.entity": "sc019296",
			"id": "2852FFFB-FC3E-A638-CED8-6777BDD8CD83"
		},
		{
			"etask.entity": "sc019297",
			"id": "19DC1D8A-1CCE-6725-ABE1-5269F2F31A51"
		},
		{
			"etask.entity": "sc019298",
			"id": "7D5FFFFF-2E9A-F1EC-55D5-1206CEC4D561"
		},
		{
			"etask.entity": "sc019299",
			"id": "E0C36E51-1F75-6392-4451-934EF88F99AC"
		},
		{
			"etask.entity": "sc019300",
			"id": "BFD82197-73E7-499C-19E0-73542C660A22"
		},
		{
			"etask.entity": "sc019301",
			"id": "6D53FFC1-FC49-2C1F-7956-59DF8F5FE48E"
		},
		{
			"etask.entity": "sc019302",
			"id": "D6C8ED06-EF81-10A9-ADB5-8D442E332F8A"
		},
		{
			"etask.entity": "sc019303",
			"id": "8CB9429E-4D0C-CFE5-7539-64E492207F3A"
		},
		{
			"etask.entity": "sc019304",
			"id": "07D58F62-50D2-F4EC-C792-42AE38953618"
		},
		{
			"etask.entity": "sc019305",
			"id": "38A96463-5312-A5D4-69B1-15DAEAD9A719"
		},
		{
			"etask.entity": "sc019306",
			"id": "E1A4A738-D548-C9E5-F2F0-57BED5299A66"
		},
		{
			"etask.entity": "sc019307",
			"id": "2C1218DF-744F-B537-B4AF-AF0905867CBE"
		},
		{
			"etask.entity": "sc019308",
			"id": "D8AAB067-14C4-E798-A61F-6B5F22B83960"
		},
		{
			"etask.entity": "sc019309",
			"id": "9BF580F2-E648-3B13-B0CF-7CF975FE228C"
		},
		{
			"etask.entity": "sc019310",
			"id": "5CBD2B17-ADEF-444D-F3F0-8A14E7D392D1"
		},
		{
			"etask.entity": "sc019311",
			"id": "AC07CAB3-E496-6457-B68A-3F2C19A0AF5C"
		},
		{
			"etask.entity": "sc019312",
			"id": "15A97E3E-D0E1-DEB7-62E8-B3ABC308E28D"
		},
		{
			"etask.entity": "sc019313",
			"id": "F0B662E7-FA5E-EEC7-7B19-3E3DBA2B8F02"
		},
		{
			"etask.entity": "sc019314",
			"id": "FAF5E9DD-2485-C57B-3E5D-49564DA3E611"
		},
		{
			"etask.entity": "sc019315",
			"id": "FEF7C565-3161-2E01-B67F-CFE00F4F2EBD"
		},
		{
			"etask.entity": "sc019316",
			"id": "368BA5BD-B86A-65E1-D60B-4BED4D8821C2"
		},
		{
			"etask.entity": "sc019317",
			"id": "8E4A7860-991D-742E-C02E-8BE2A6FF6D0F"
		},
		{
			"etask.entity": "sc019318",
			"id": "A9EA6B17-D7AC-6E47-179B-690977EF16D4"
		},
		{
			"etask.entity": "sc019319",
			"id": "4FD3B9F3-6B73-146C-3839-38612B70B02F"
		},
		{
			"etask.entity": "sc019320",
			"id": "6A5FAAB1-8FEE-0150-41B8-EB36F4562638"
		},
		{
			"etask.entity": "sc019321",
			"id": "BEAAEE5F-5E66-7416-AD85-05356D8B7DE1"
		},
		{
			"etask.entity": "sc019322",
			"id": "E074BF53-2CFF-D883-9BAE-547631F58B64"
		},
		{
			"etask.entity": "sc019323",
			"id": "35765506-36D2-0483-2981-E27E7C0ED519"
		},
		{
			"etask.entity": "sc019324",
			"id": "4839A4E3-3420-1069-AB1C-10971DF210CF"
		},
		{
			"etask.entity": "sc019325",
			"id": "22DE995E-FA92-D1DE-48C7-4D3F62A7EB08"
		},
		{
			"etask.entity": "sc019326",
			"id": "4D887020-FA0C-F4CD-C60E-F58F7CF41C0D"
		},
		{
			"etask.entity": "sc019327",
			"id": "8F1E0579-ADEB-C239-4455-39DBD98BF640"
		},
		{
			"etask.entity": "sc019328",
			"id": "EF288334-28C2-A566-5338-65F9F3E7A3C0"
		},
		{
			"etask.entity": "sc019329",
			"id": "7E526A4C-ABF0-D448-3E52-9A7898380D09"
		},
		{
			"etask.entity": "sc019330",
			"id": "DD521B71-E377-A16F-CE47-2F032194AB81"
		},
		{
			"etask.entity": "sc019331",
			"id": "FF2FFFE7-6E42-5279-95D8-10455A1D01EA"
		},
		{
			"etask.entity": "sc019332",
			"id": "1D8FB780-060C-272F-C03B-8D15F0A9C649"
		},
		{
			"etask.entity": "sc019333",
			"id": "203082A8-6F32-2096-CAD1-9F0A71A169EB"
		},
		{
			"etask.entity": "sc019334",
			"id": "6510E6F9-9D67-7B2F-2EAF-0C84AB7870FD"
		},
		{
			"etask.entity": "sc019335",
			"id": "4FBD3CCE-85D3-5A85-27AB-15C3CC68944C"
		},
		{
			"etask.entity": "sc019336",
			"id": "9DC9532C-C75B-3452-5EE0-95B5A99C315C"
		},
		{
			"etask.entity": "sc019337",
			"id": "C33DC9CD-7800-61FE-C018-89904AC53224"
		},
		{
			"etask.entity": "sc019338",
			"id": "2358AC97-1A8C-8B76-2E01-75941E94AB43"
		},
		{
			"etask.entity": "sc019339",
			"id": "0297406F-9A88-9845-1EF2-EB52D66D0A56"
		},
		{
			"etask.entity": "sc019340",
			"id": "E64029A9-3D86-7783-B812-F07E717F8D1D"
		},
		{
			"etask.entity": "sc019341",
			"id": "F642795D-AC97-1E4B-6C84-A8F6C4669D0B"
		},
		{
			"etask.entity": "sc019342",
			"id": "6C77872D-9869-D0BA-CE3C-0CB00F141118"
		},
		{
			"etask.entity": "sc019343",
			"id": "F7349D82-41DE-CFE9-49D6-623A3C92635C"
		},
		{
			"etask.entity": "sc019344",
			"id": "C76FADB4-0127-D4C4-D110-5E54DC350C22"
		},
		{
			"etask.entity": "sc019345",
			"id": "DED54CC4-A7BF-10AB-C806-6BBF9461CDBA"
		},
		{
			"etask.entity": "sc019346",
			"id": "72055604-158F-9D25-4459-11F91095D8CD"
		},
		{
			"etask.entity": "sc019347",
			"id": "6C78CC53-8F8F-AB5E-2C72-1661B6DBAA49"
		},
		{
			"etask.entity": "sc019348",
			"id": "CA402B80-633B-8C4B-6379-5232CEAAA2ED"
		},
		{
			"etask.entity": "sc019349",
			"id": "70F4330C-0E7C-875F-89A9-4B032B62CE3B"
		},
		{
			"etask.entity": "sc019350",
			"id": "57CC567E-40A0-4980-B529-D7024738A7A9"
		},
		{
			"etask.entity": "sc019351",
			"id": "93C3212A-54D2-5310-5B98-E7CDDC7CA95B"
		},
		{
			"etask.entity": "sc019352",
			"id": "0F225EBB-28A6-DA36-E2B4-77A40E1D77A4"
		},
		{
			"etask.entity": "sc019353",
			"id": "AB93ADEC-D456-E07A-2F55-79F058A16E02"
		},
		{
			"etask.entity": "sc019354",
			"id": "5A01BA6B-F3EA-307C-F5D0-918BA536DA65"
		},
		{
			"etask.entity": "sc019355",
			"id": "1FEB4B6F-DED0-CDE3-943F-3032D901036C"
		},
		{
			"etask.entity": "sc019356",
			"id": "EA7FEEC2-3D54-641E-4DB6-1E520F451B63"
		},
		{
			"etask.entity": "sc019357",
			"id": "A3C8FF09-A7B8-A035-37C4-B9E120F404ED"
		},
		{
			"etask.entity": "sc019358",
			"id": "975ECDFA-E47C-41E5-8107-9D4615832B24"
		},
		{
			"etask.entity": "sc019359",
			"id": "62358830-49FE-30BB-D2D5-63553D0B3E72"
		},
		{
			"etask.entity": "sc019360",
			"id": "DEC2CEEE-DA0E-6AC8-A5CA-52C309E588B6"
		},
		{
			"etask.entity": "sc019361",
			"id": "127888FE-10DD-A6C8-5F38-35D03D77AB3C"
		},
		{
			"etask.entity": "sc019362",
			"id": "790C62C1-37D4-594B-9C59-9800C81B6BAF"
		},
		{
			"etask.entity": "sc019363",
			"id": "BC3A5474-81DE-E59D-8A18-C64547C2BAA1"
		},
		{
			"etask.entity": "sc019364",
			"id": "F06FC585-43CF-5604-0E8C-26B18403A88B"
		},
		{
			"etask.entity": "sc019365",
			"id": "98BD4346-FCA4-CB7C-8A96-27AD31604958"
		},
		{
			"etask.entity": "sc019366",
			"id": "92CA913D-6A6A-C84F-865C-D701539DE9D9"
		},
		{
			"etask.entity": "sc019367",
			"id": "36D3FB07-59DE-66D1-526B-359AEEBE2605"
		},
		{
			"etask.entity": "sc019368",
			"id": "62C6BA99-152D-8166-03AC-5EDE9381C000"
		},
		{
			"etask.entity": "sc019369",
			"id": "5CC2F804-E745-39F1-2F6D-15856D76F5D2"
		},
		{
			"etask.entity": "sc019370",
			"id": "EAEC2D88-44C4-455C-E4B6-4AF35378E152"
		},
		{
			"etask.entity": "sc019371",
			"id": "AAA3E094-3E20-684C-EFF3-067361E5A1B6"
		},
		{
			"etask.entity": "sc019372",
			"id": "11447542-DCDB-EC19-F0C2-F4BA72F7CEBB"
		},
		{
			"etask.entity": "sc019373",
			"id": "99A9F868-5BA2-135A-4A0D-9E77D20EC4ED"
		},
		{
			"etask.entity": "sc019374",
			"id": "03EB3260-5623-3935-8CD5-E14A3566A3DC"
		},
		{
			"etask.entity": "sc019375",
			"id": "FBBDB223-2FA3-0F83-0420-A9BBE3488F0F"
		},
		{
			"etask.entity": "sc019376",
			"id": "2BD3079D-E1A5-301C-1D0F-EDBE0AFE046D"
		},
		{
			"etask.entity": "sc019377",
			"id": "C172F2E4-A727-A5F0-DEDE-E19DD0A225A9"
		},
		{
			"etask.entity": "sc019378",
			"id": "9A61A3B8-D24F-793A-AA05-CF45FF4062DB"
		},
		{
			"etask.entity": "sc019379",
			"id": "162D243C-6565-5E99-A717-243644CC7508"
		},
		{
			"etask.entity": "sc019380",
			"id": "6F625FD6-495D-4F3E-E7CB-0084998F3B44"
		},
		{
			"etask.entity": "sc019381",
			"id": "5FBB64D1-06A2-F2DC-3A59-95DE563FD866"
		},
		{
			"etask.entity": "sc019382",
			"id": "E58EE787-0B9E-8D52-4587-6FE2B025F720"
		},
		{
			"etask.entity": "sc019383",
			"id": "82C5E4CD-D91C-1E17-A87F-6D3309FFB577"
		},
		{
			"etask.entity": "sc019384",
			"id": "E4C9BDB1-887A-06B6-7AD1-0F8517F4E0AC"
		},
		{
			"etask.entity": "sc019385",
			"id": "58FB4E0A-4FE4-2ED8-D075-313D45690965"
		},
		{
			"etask.entity": "sc019386",
			"id": "9F11AD33-1B2D-9E45-7D8B-7172582B7C7C"
		},
		{
			"etask.entity": "sc019387",
			"id": "C00BE36D-B291-FE58-F901-13965C3AE4F4"
		},
		{
			"etask.entity": "sc019388",
			"id": "896F844A-10C0-BEE5-B08B-641B3126F8D7"
		},
		{
			"etask.entity": "sc019389",
			"id": "89384E06-1D33-9F89-4ECC-0016C67D342E"
		},
		{
			"etask.entity": "sc019390",
			"id": "6F965847-0B61-34D6-C05A-62AD7DCCC6D2"
		},
		{
			"etask.entity": "sc019391",
			"id": "8CB04042-362F-CBD5-978F-85A473F95B3C"
		},
		{
			"etask.entity": "sc019392",
			"id": "D682C924-BA99-2C2D-9D96-4D0D832918D0"
		},
		{
			"etask.entity": "sc019393",
			"id": "E2912D28-10A5-E368-A4AB-87E8E428AD21"
		},
		{
			"etask.entity": "sc019394",
			"id": "07C4390F-FDB9-A12E-BECF-A876E60DAAF3"
		},
		{
			"etask.entity": "sc019395",
			"id": "844BA627-052C-46EE-C663-AEF8CC88ED00"
		},
		{
			"etask.entity": "sc019396",
			"id": "D96A9C19-695C-43F1-546C-4BA04B885EFE"
		},
		{
			"etask.entity": "sc019397",
			"id": "19193F32-C9F5-9679-C6F9-F02E9A25D188"
		},
		{
			"etask.entity": "sc019398",
			"id": "82D0C6FF-809E-AB64-632B-25969C11B04A"
		},
		{
			"etask.entity": "sc019399",
			"id": "3393D738-D793-379B-DBDA-C6CAD3F3B547"
		},
		{
			"etask.entity": "sc019400",
			"id": "9D77D148-717E-8092-202E-BE11E098ED55"
		},
		{
			"etask.entity": "sc019401",
			"id": "800F948C-AA67-1A88-B6EE-A356CB643AE0"
		},
		{
			"etask.entity": "sc019402",
			"id": "AF0A95D8-696B-DBE5-1A68-358BE878AA40"
		},
		{
			"etask.entity": "sc019403",
			"id": "B774380B-0844-9ED2-6727-AA07AF60D955"
		},
		{
			"etask.entity": "sc019404",
			"id": "4A48B126-27D0-8C30-F0F2-1ABA18E7DCCE"
		},
		{
			"etask.entity": "sc019405",
			"id": "E900B3B9-1694-4593-7FDE-8B49D6FD953B"
		},
		{
			"etask.entity": "sc019406",
			"id": "29691DC6-4AD9-07BE-F762-91D4C6A13D9E"
		},
		{
			"etask.entity": "sc019407",
			"id": "1CA290D0-45FA-8B94-E975-CF11403A7ECE"
		},
		{
			"etask.entity": "sc019408",
			"id": "5A0EBEF7-9C70-52A9-F8F0-61AD5C675DC1"
		},
		{
			"etask.entity": "sc019409",
			"id": "75FA2C10-E9D8-9D6E-0365-9F7ABF6086D7"
		},
		{
			"etask.entity": "sc019410",
			"id": "A12F0873-985B-4723-28CC-0587C65A5FD1"
		},
		{
			"etask.entity": "sc019411",
			"id": "95D6168A-9297-E5B6-CC0F-BAA2FFD38106"
		},
		{
			"etask.entity": "sc019412",
			"id": "8A24BF56-CACE-F223-D7FA-45E8D927BCF6"
		},
		{
			"etask.entity": "sc019413",
			"id": "97A58048-DB03-D087-59B9-9104BF2B93BD"
		},
		{
			"etask.entity": "sc019414",
			"id": "9E326972-5213-573E-D8DC-6A4E9A5CAF68"
		},
		{
			"etask.entity": "sc019415",
			"id": "3CB9C6A4-B000-CEF5-3610-C815850A8E0C"
		},
		{
			"etask.entity": "sc019416",
			"id": "FDB46E4D-4DD2-1D0A-0DD2-5923EB895B1D"
		},
		{
			"etask.entity": "sc019417",
			"id": "038E0F59-2FD1-1B33-711B-0D333ECFC4B0"
		},
		{
			"etask.entity": "sc019418",
			"id": "E41307E9-8587-B889-CC8D-AA6F874697A7"
		},
		{
			"etask.entity": "sc019419",
			"id": "37C1D50D-6A0F-A343-86A1-B71143D9AD33"
		},
		{
			"etask.entity": "sc019420",
			"id": "BC07B9C3-8D78-E1EC-4CB8-76EF1CF19BD8"
		},
		{
			"etask.entity": "sc019421",
			"id": "3E5EC96D-2C78-C7E8-0ABC-68E6535C45A4"
		},
		{
			"etask.entity": "sc019422",
			"id": "0DDA5AE2-D049-EAEF-A919-E7BBD319A65F"
		},
		{
			"etask.entity": "sc019423",
			"id": "C9FB127A-7141-1D3A-8D8C-CB2ABA8C8A27"
		},
		{
			"etask.entity": "sc019424",
			"id": "175B5DBF-53B3-8641-5523-4766B14711AD"
		},
		{
			"etask.entity": "sc019425",
			"id": "033C493A-322A-3BEB-DBA3-E9F275A94047"
		},
		{
			"etask.entity": "sc019426",
			"id": "73F37CA9-9340-5D16-29C4-BAF42A0BC929"
		},
		{
			"etask.entity": "sc019427",
			"id": "0C339FAA-9820-5A89-932F-C440300D87EE"
		},
		{
			"etask.entity": "sc019428",
			"id": "357A213D-CFB4-C9A8-2FF4-45023DED1861"
		},
		{
			"etask.entity": "sc019429",
			"id": "8103A2A2-4EA8-4692-8BD3-5E3B676A0062"
		},
		{
			"etask.entity": "sc019430",
			"id": "813FFDC2-8EE6-8A01-C538-E564AEFF8980"
		},
		{
			"etask.entity": "sc019431",
			"id": "1BF6E3DD-4775-6F9A-DF45-73EACCC6D167"
		},
		{
			"etask.entity": "sc019432",
			"id": "EB5B50F7-9A23-262C-EEF5-00BD42189B09"
		},
		{
			"etask.entity": "sc019433",
			"id": "0F629CFC-E847-8998-142A-E6618894D787"
		},
		{
			"etask.entity": "sc019434",
			"id": "50B8E069-FAD4-51A7-22ED-FB3A6FAD0E5E"
		},
		{
			"etask.entity": "sc019435",
			"id": "E9F42B8D-44BF-842B-0BD5-A8690E03FA80"
		},
		{
			"etask.entity": "sc019436",
			"id": "920EBD50-895E-74A9-3AC1-5C3B7DBB16E1"
		},
		{
			"etask.entity": "sc019437",
			"id": "B558847C-3D39-64AC-7F09-D7571EE5F175"
		},
		{
			"etask.entity": "sc019438",
			"id": "5D5D2BC7-9EE9-33AD-D66A-12906A6D64C1"
		},
		{
			"etask.entity": "sc019439",
			"id": "009C76DF-5EFC-89AA-6890-E933F9DAAB91"
		},
		{
			"etask.entity": "sc019440",
			"id": "15DED410-6C0D-B634-21AA-6693B0E93C31"
		},
		{
			"etask.entity": "sc019441",
			"id": "A7130A9B-ADF6-2817-33A4-61C234E6AB6E"
		},
		{
			"etask.entity": "sc019442",
			"id": "F1499C66-5C2D-4C72-6AA7-274F96A1D645"
		},
		{
			"etask.entity": "sc019443",
			"id": "7571A939-6C5A-C3AD-ECE0-C98D242306A8"
		},
		{
			"etask.entity": "sc019444",
			"id": "22D6ED2B-4531-670B-89D5-9396F2BF5910"
		},
		{
			"etask.entity": "sc019445",
			"id": "9C886D11-4263-B395-D4C7-860C632F33CE"
		},
		{
			"etask.entity": "sc019446",
			"id": "582E8A35-1FA2-1BDF-AE87-CA4592CD0682"
		},
		{
			"etask.entity": "sc019447",
			"id": "D5FC4596-4DDC-25E1-F751-4F89A4C73607"
		},
		{
			"etask.entity": "sc019448",
			"id": "DF067ACA-CB56-74F4-680E-B0FD008CD731"
		},
		{
			"etask.entity": "sc019449",
			"id": "B30A63B6-AD96-7528-A9DF-C7F4D9E0256C"
		},
		{
			"etask.entity": "sc019450",
			"id": "4E329357-2A4F-66ED-D6EB-23B73B5366B2"
		},
		{
			"etask.entity": "sc019451",
			"id": "18F5A3CE-00CF-AA83-3551-F5DAB1704C07"
		},
		{
			"etask.entity": "sc019452",
			"id": "FBACB890-3326-51AA-D282-964EF7403FEB"
		},
		{
			"etask.entity": "sc019453",
			"id": "0E56C448-B208-CF53-F680-03C25A8ECE35"
		},
		{
			"etask.entity": "sc019454",
			"id": "AB1AA666-F63A-488E-2BC1-E3D4EC4EB8FD"
		},
		{
			"etask.entity": "sc019455",
			"id": "6414B03A-07A4-12EC-3B0C-EC31939A4531"
		},
		{
			"etask.entity": "sc019456",
			"id": "F532A056-98FB-A17F-904C-FDC793A9F062"
		},
		{
			"etask.entity": "sc019457",
			"id": "625F96C6-CA10-D317-C5F3-56DFD0CF45DF"
		},
		{
			"etask.entity": "sc019458",
			"id": "DDE07373-2F59-3318-8F10-4586FAFFCEAE"
		},
		{
			"etask.entity": "sc019459",
			"id": "A4153797-255B-7DA2-2F2C-F89D58B7F5B6"
		},
		{
			"etask.entity": "sc019460",
			"id": "46617AA0-54B7-81BE-38EE-486D539333AF"
		},
		{
			"etask.entity": "sc019461",
			"id": "3DBEFCDE-2644-D468-488F-2045A9332F6A"
		},
		{
			"etask.entity": "sc019462",
			"id": "51D19897-F3E6-3CC6-0B9B-1FBEEF319A21"
		},
		{
			"etask.entity": "sc019463",
			"id": "AF87F101-1F55-2255-9CBB-6084B94169C2"
		},
		{
			"etask.entity": "sc019464",
			"id": "A0E0B9D4-3BB6-57B8-83D3-DF9CE16F684A"
		},
		{
			"etask.entity": "sc019465",
			"id": "51B8CA10-0659-7A9B-B2FF-619B6E8C3FD2"
		},
		{
			"etask.entity": "sc019466",
			"id": "01149C7A-6F35-87D8-1177-FE950326F0A8"
		},
		{
			"etask.entity": "sc019467",
			"id": "655E8ECB-43A4-4C75-8530-8FE4043FC66B"
		},
		{
			"etask.entity": "sc019468",
			"id": "2F982114-0253-EF6B-17F1-8EB92A893B1C"
		},
		{
			"etask.entity": "sc019469",
			"id": "B8E3C055-0DD5-9396-B65F-45F1BE6509E3"
		},
		{
			"etask.entity": "sc019470",
			"id": "44DB075E-3E3D-287A-4145-C0FCD70AEE74"
		},
		{
			"etask.entity": "sc019471",
			"id": "85D453D0-C375-A097-95FF-63FA2D03CA07"
		},
		{
			"etask.entity": "sc019472",
			"id": "365B252C-0429-8F78-7384-EB25A928FECA"
		},
		{
			"etask.entity": "sc019473",
			"id": "095B17BE-5A01-D7FC-B8A0-C9613F1262ED"
		},
		{
			"etask.entity": "sc019474",
			"id": "199740CD-37BE-A3EC-BB05-44AB24F5253F"
		},
		{
			"etask.entity": "sc019475",
			"id": "5ACF6663-0393-917A-7C8C-00E6C1A13091"
		},
		{
			"etask.entity": "sc019476",
			"id": "264BA269-D6FC-9154-2384-C20EA1DB4D3A"
		},
		{
			"etask.entity": "sc019477",
			"id": "C9B95C39-9E7A-432D-7956-BC6C4C639BEB"
		},
		{
			"etask.entity": "sc019478",
			"id": "FE002F94-4BD5-9DE5-7E29-E105A556EF3F"
		},
		{
			"etask.entity": "sc019479",
			"id": "6FD58AC2-EC19-8100-1366-26D4E0A9DE7B"
		},
		{
			"etask.entity": "sc019480",
			"id": "57BD2168-C58C-CA52-9AD9-B0E31331A5F4"
		},
		{
			"etask.entity": "sc019481",
			"id": "89A4A87A-9881-DA39-3219-E6D7E2074354"
		},
		{
			"etask.entity": "sc019482",
			"id": "86E4F5FA-C966-5909-E809-CF3AB2E9DD6F"
		},
		{
			"etask.entity": "sc019483",
			"id": "DAD77DC6-2023-20DB-6AF8-2C3B4DF9BE4D"
		},
		{
			"etask.entity": "sc019484",
			"id": "D12261CC-9FA4-1F2F-39FA-DC9870346DAC"
		},
		{
			"etask.entity": "sc019485",
			"id": "F9E36E18-B2A5-DE9C-72DA-BA4D662CF8DC"
		},
		{
			"etask.entity": "sc019486",
			"id": "05BFED95-3971-3928-D2CA-17F134A382FC"
		},
		{
			"etask.entity": "sc019487",
			"id": "C607D612-5512-0A34-D7DD-DB2BB44ECB73"
		},
		{
			"etask.entity": "sc019488",
			"id": "3301BFA2-5D40-0630-6EA9-0451DB90C2C2"
		},
		{
			"etask.entity": "sc019489",
			"id": "41F204BA-D067-E0CB-FAAE-3C953C3C1B5E"
		},
		{
			"etask.entity": "sc019490",
			"id": "832A3A12-2B83-8413-0CAE-B49C389E4373"
		},
		{
			"etask.entity": "sc019491",
			"id": "00652D10-F9AD-CB74-941A-B1BD3B256977"
		},
		{
			"etask.entity": "sc019492",
			"id": "34FEA0EF-50B9-19D8-5A83-00969FEC74C1"
		},
		{
			"etask.entity": "sc019493",
			"id": "62B50198-5270-9AFA-4182-F38D92F28E6F"
		},
		{
			"etask.entity": "sc019494",
			"id": "A634F929-47DB-5DD5-20D7-F8AB03E5188D"
		},
		{
			"etask.entity": "sc019495",
			"id": "35D08B85-2338-CF90-643D-56E9847ED483"
		},
		{
			"etask.entity": "sc019496",
			"id": "8132A524-8E68-241A-F89F-7A4B8CD6FA5A"
		},
		{
			"etask.entity": "sc019497",
			"id": "E432CDB9-9717-E51A-A625-97E5615E02B8"
		},
		{
			"etask.entity": "sc019498",
			"id": "204A9BAE-7F9B-C519-9076-1F2E51044399"
		},
		{
			"etask.entity": "sc019499",
			"id": "C9F4C807-8206-A3A4-0E67-84F8AD07534F"
		},
		{
			"etask.entity": "sc019500",
			"id": "37882CBC-7639-63D8-325C-8286332EA45E"
		},
		{
			"etask.entity": "sc019501",
			"id": "112C6F00-DA34-3C68-5A3F-84B1E9F47C68"
		},
		{
			"etask.entity": "sc019502",
			"id": "24E2ADF9-1E48-F51E-3352-6840EBCF92ED"
		},
		{
			"etask.entity": "sc019503",
			"id": "5A55729D-3222-5698-D99F-B82EADA502EC"
		},
		{
			"etask.entity": "sc019504",
			"id": "AD566367-5352-6121-0402-0B51B1DD4F01"
		},
		{
			"etask.entity": "sc019505",
			"id": "5D287B74-2347-2F47-7993-99246B1F999F"
		},
		{
			"etask.entity": "sc019506",
			"id": "0ECAC994-4334-924D-EC51-C0684D24F889"
		},
		{
			"etask.entity": "sc019507",
			"id": "6EA4B800-F46B-2371-B046-E54DFAB055A8"
		},
		{
			"etask.entity": "sc019508",
			"id": "A9ED0230-63F5-666F-611F-2077FA01DEA5"
		},
		{
			"etask.entity": "sc019509",
			"id": "55E37E9A-F893-73B0-0AD1-AAD4B32D3B7F"
		},
		{
			"etask.entity": "sc019510",
			"id": "B88AC5E3-BDAB-4C61-C5C1-F34963BE22C8"
		},
		{
			"etask.entity": "sc019511",
			"id": "1D5320F0-5EC0-B76B-04A2-DDCDC04FEB3D"
		},
		{
			"etask.entity": "sc019512",
			"id": "9ECCDBD1-B6C4-FB65-869E-90FE48C3071D"
		},
		{
			"etask.entity": "sc019513",
			"id": "5445FFC3-C1BC-76A3-3E72-90F7906A1C9A"
		},
		{
			"etask.entity": "sc019514",
			"id": "EB65E380-D2B3-DDC1-4C72-4BBC36E50EC9"
		},
		{
			"etask.entity": "sc019515",
			"id": "3D865071-0D06-026C-96BB-147523EBF6C4"
		},
		{
			"etask.entity": "sc019516",
			"id": "C8450B41-97AC-1307-CF33-25FF163FE629"
		},
		{
			"etask.entity": "sc019517",
			"id": "0B392979-30D9-04A2-E826-5B1914E4FF7B"
		},
		{
			"etask.entity": "sc019518",
			"id": "D7342094-9AD8-B9A2-2B2A-25004DE2C34C"
		},
		{
			"etask.entity": "sc019519",
			"id": "CAD2B108-DCB3-041B-FA3B-D348B0FD0CB5"
		},
		{
			"etask.entity": "sc019520",
			"id": "D0817D87-B725-C7E7-71C9-4B11A01CA929"
		},
		{
			"etask.entity": "sc019521",
			"id": "A38CF66B-2321-5C89-335A-7E7A6DA4B04E"
		},
		{
			"etask.entity": "sc019522",
			"id": "FD68925E-DFF1-9AA6-D291-7288619BEA72"
		},
		{
			"etask.entity": "sc019523",
			"id": "062CB1FB-F423-9206-1127-DFE882A88015"
		},
		{
			"etask.entity": "sc019524",
			"id": "864E25B2-43B1-6E66-5041-34CC9E5A46D0"
		},
		{
			"etask.entity": "sc019525",
			"id": "7ABE717D-1A47-70E1-7AA6-B7B2AA202EEA"
		},
		{
			"etask.entity": "sc019526",
			"id": "33582077-2BAA-286E-F03B-A360DE6FCEDE"
		},
		{
			"etask.entity": "sc019527",
			"id": "5C08ABC7-3F7C-1458-3D29-E74F036E3836"
		},
		{
			"etask.entity": "sc019528",
			"id": "5563669A-EEC7-8465-7F2A-4FE04D4894A7"
		},
		{
			"etask.entity": "sc019529",
			"id": "2E4FE9A2-4B78-48F7-DEC6-B8594BB82622"
		},
		{
			"etask.entity": "sc019530",
			"id": "98520FF4-6D79-0409-205F-C4741CA3BE67"
		},
		{
			"etask.entity": "sc019531",
			"id": "1B72C7BD-F1BF-4566-5669-4083BA83A0BE"
		},
		{
			"etask.entity": "sc019532",
			"id": "89DA6F88-3652-85F3-7F9C-957F4778098C"
		},
		{
			"etask.entity": "sc019533",
			"id": "4AF2B9B3-EC27-C8B9-9113-E73D0AE1CEFA"
		},
		{
			"etask.entity": "sc019534",
			"id": "E4AA590B-2F5E-86E0-F016-36919F12A339"
		},
		{
			"etask.entity": "sc019535",
			"id": "AC6E4F82-1965-1126-AB5C-4A50272093FD"
		},
		{
			"etask.entity": "sc019536",
			"id": "AB317E40-5E17-77B8-F6DA-C0358852456F"
		},
		{
			"etask.entity": "sc019537",
			"id": "598D7A0A-D1EA-F7C0-F646-904571204D50"
		},
		{
			"etask.entity": "sc019538",
			"id": "CB78128D-36CE-D99A-2CEB-EDF52C6B1A30"
		},
		{
			"etask.entity": "sc019539",
			"id": "A57E721C-D221-2BBC-C8C6-0EA11ADE69B3"
		},
		{
			"etask.entity": "sc019540",
			"id": "04398774-7D45-D6BB-5FC5-93486B65F753"
		},
		{
			"etask.entity": "sc019541",
			"id": "8D032DA4-3242-1EBC-6CA4-37DC93B4379C"
		},
		{
			"etask.entity": "sc019542",
			"id": "7B99882D-DF44-1BE4-A996-776651C7931D"
		},
		{
			"etask.entity": "sc019543",
			"id": "D4022648-C74B-3893-6E80-F6BCD3DB608A"
		},
		{
			"etask.entity": "sc019544",
			"id": "B403627C-0BD2-C175-1EE3-8ED72BAA74D0"
		},
		{
			"etask.entity": "sc019545",
			"id": "61DE2C8B-A57C-BBDC-124D-A2E853B58F80"
		},
		{
			"etask.entity": "sc019546",
			"id": "AA3E45C6-003A-DAF9-07C5-D000D11C402F"
		},
		{
			"etask.entity": "sc019547",
			"id": "80158547-C2BE-4F2E-544A-B2F6D81C3429"
		},
		{
			"etask.entity": "sc019548",
			"id": "74293B31-B54F-9901-9248-24D6DE726FC5"
		},
		{
			"etask.entity": "sc019549",
			"id": "EEFADB28-EE8A-8120-F9C1-8B516BBBCFF2"
		},
		{
			"etask.entity": "sc019550",
			"id": "F9E94272-51FD-CC20-9F2A-0CF3C7FCB7BE"
		},
		{
			"etask.entity": "sc019551",
			"id": "4CDE03D7-48A8-06C6-8C8E-5DA794FC6DDC"
		},
		{
			"etask.entity": "sc019552",
			"id": "6F7DE71A-128D-2195-491D-FDC432A59794"
		},
		{
			"etask.entity": "sc019553",
			"id": "0A24F255-D160-DEF6-DF5C-55633D5376FF"
		},
		{
			"etask.entity": "sc019554",
			"id": "6137DA84-CBB7-8DDC-7DD6-6CFD28669492"
		},
		{
			"etask.entity": "sc019555",
			"id": "704E867E-CF97-B1EE-DCDC-F5CDECD4E5B6"
		},
		{
			"etask.entity": "sc019556",
			"id": "E631C7AE-32F7-5512-F58B-2973ECC11558"
		},
		{
			"etask.entity": "sc019557",
			"id": "024B359C-0D56-BBA3-AAC8-E119F6346C26"
		},
		{
			"etask.entity": "sc019558",
			"id": "7EE1D1AA-E8E6-0CCB-BDB8-E2D777D95309"
		},
		{
			"etask.entity": "sc019559",
			"id": "EBEB787A-836A-4867-F97B-FA9C212295C7"
		},
		{
			"etask.entity": "sc019560",
			"id": "9A48D422-33BC-507E-A4E6-DC767085243F"
		},
		{
			"etask.entity": "sc019561",
			"id": "28BCB378-2808-D607-DF69-E16579CFB370"
		},
		{
			"etask.entity": "sc019562",
			"id": "952BBB42-FD17-951B-8205-3B8CEEB226D3"
		},
		{
			"etask.entity": "sc019563",
			"id": "C6BDAA2D-5807-1C84-48C7-314B4AC098A4"
		},
		{
			"etask.entity": "sc019564",
			"id": "65D80C0E-7890-6932-DCBF-D038FF0227C0"
		},
		{
			"etask.entity": "sc019565",
			"id": "A4B32436-9469-94FE-BC93-08608366528E"
		},
		{
			"etask.entity": "sc019566",
			"id": "D8F13227-55E7-18F5-740D-E3D415EFE231"
		},
		{
			"etask.entity": "sc019567",
			"id": "1253CCCF-5981-7872-91F7-64FC16DC898B"
		},
		{
			"etask.entity": "sc019568",
			"id": "AB6EB21C-513E-C544-58D6-5CE6ACA44BE0"
		},
		{
			"etask.entity": "sc019569",
			"id": "2788302F-F384-F7D6-75DF-A8EB65837E25"
		},
		{
			"etask.entity": "sc019570",
			"id": "E8B947A3-8FA4-FE2F-EAC7-71CA7CB1BE40"
		},
		{
			"etask.entity": "sc019571",
			"id": "EC08A651-E6D8-D4FA-01A2-084FA707222E"
		},
		{
			"etask.entity": "sc019572",
			"id": "6C5E3675-CB53-BEE6-AB58-4A766333584F"
		},
		{
			"etask.entity": "sc019573",
			"id": "6FC3680D-9646-41ED-3EFA-BDA10D141D53"
		},
		{
			"etask.entity": "sc019574",
			"id": "3D6A5883-E839-C6EA-C8CF-794CE2A1111A"
		},
		{
			"etask.entity": "sc019575",
			"id": "A755A7E7-DBE7-284D-1050-C2A4759A3BD6"
		},
		{
			"etask.entity": "sc019576",
			"id": "C7C725B9-B9DF-AC30-286C-E44642548D05"
		},
		{
			"etask.entity": "sc019577",
			"id": "3E913502-BB4A-B27A-FE57-C82350C5E3E1"
		},
		{
			"etask.entity": "sc019578",
			"id": "4F32D409-C70B-F267-57D0-F1DC4FE70150"
		},
		{
			"etask.entity": "sc019579",
			"id": "E9DCFDDF-3B01-98A5-7D33-E5C1A3DF9282"
		},
		{
			"etask.entity": "sc019580",
			"id": "4958397E-422A-8CA8-D973-BAE5948E3E5B"
		},
		{
			"etask.entity": "sc019581",
			"id": "C064A1DB-41AC-3D5F-D6CD-130109C75766"
		},
		{
			"etask.entity": "sc019582",
			"id": "B781112C-A76D-AA7C-E0B6-EA56DA23635F"
		},
		{
			"etask.entity": "sc019583",
			"id": "7294B794-BDB9-C5F5-CABD-7EEEFD2C9367"
		},
		{
			"etask.entity": "sc019584",
			"id": "F51ED68B-2ECF-54F9-BB9F-97A60C4FB62C"
		},
		{
			"etask.entity": "sc019585",
			"id": "9CE12FD5-3A5A-D8CC-6EE5-43F9A33E42A2"
		},
		{
			"etask.entity": "sc019586",
			"id": "59CEF375-3A45-7143-995A-FCEDFD74DCF5"
		},
		{
			"etask.entity": "sc019587",
			"id": "0D72E0A5-6022-DD6C-CD52-53024F4D3BEA"
		},
		{
			"etask.entity": "sc019588",
			"id": "58554AF8-B2BF-EE83-CF47-3310B7B5BFE8"
		},
		{
			"etask.entity": "sc019589",
			"id": "22A38756-B01A-0544-B97C-D7F678BDEE4B"
		},
		{
			"etask.entity": "sc019590",
			"id": "7FA2A5AF-E917-13AA-D8C6-7FC231E8BD0F"
		},
		{
			"etask.entity": "sc019591",
			"id": "143F0CA4-C73F-D2A5-0F89-A91659CDAB1D"
		},
		{
			"etask.entity": "sc019592",
			"id": "8FBF4C9F-F010-9BBB-B2F6-3AE1DC89EEEF"
		},
		{
			"etask.entity": "sc019593",
			"id": "E8614561-EDB1-65F2-951F-346626EB391C"
		},
		{
			"etask.entity": "sc019594",
			"id": "0C994187-3645-A413-BF0B-7A6569448E1C"
		},
		{
			"etask.entity": "sc019595",
			"id": "775EF04E-965D-E1DC-9998-5BF6FDA31AA7"
		},
		{
			"etask.entity": "sc019596",
			"id": "6732A3F0-3765-5860-3921-3E85E371E387"
		},
		{
			"etask.entity": "sc019597",
			"id": "880F5043-BCB8-5BF7-DF88-B4B946E08EC5"
		},
		{
			"etask.entity": "sc019598",
			"id": "C77091AC-D6FC-C0EC-11FA-8F94C43FEA75"
		},
		{
			"etask.entity": "sc019599",
			"id": "9E76D15E-B3CA-C8B0-1A3A-B2411388BEC7"
		},
		{
			"etask.entity": "sc019600",
			"id": "3E79C3AE-B4C1-30B0-7D0A-A66D8576C429"
		},
		{
			"etask.entity": "sc019601",
			"id": "165A61C8-5984-7164-F2D6-CCEC9705714F"
		},
		{
			"etask.entity": "sc019602",
			"id": "60C5C7B6-FB73-892C-29C6-680971FB7AE2"
		},
		{
			"etask.entity": "sc019603",
			"id": "F7255A5E-3567-E26D-28C8-A11E98D297C0"
		},
		{
			"etask.entity": "sc019604",
			"id": "C8EAFD04-6C9D-813E-9AD7-EA8C8F2F828B"
		},
		{
			"etask.entity": "sc019605",
			"id": "201AEED2-4D0F-5EA5-DC09-AA9B82E4BEE7"
		},
		{
			"etask.entity": "sc019606",
			"id": "86398A1B-4B5C-C55D-91B8-F839837FEB7C"
		},
		{
			"etask.entity": "sc019607",
			"id": "B0F5EB2C-A867-88A5-5702-BA48D64427D0"
		},
		{
			"etask.entity": "sc019608",
			"id": "AC9684AB-8D36-BC0E-6743-62F55DE78643"
		},
		{
			"etask.entity": "sc019609",
			"id": "8D70B7A3-2821-F3FC-B70B-5E52BE49BF50"
		},
		{
			"etask.entity": "sc019610",
			"id": "A0AEC36A-42A1-AB6A-D149-ABCB549AAE86"
		},
		{
			"etask.entity": "sc019611",
			"id": "C0586A3D-11A0-5747-A54E-EBECA92A2FFC"
		},
		{
			"etask.entity": "sc019612",
			"id": "B27F59FD-244D-C3E2-2D70-4BEFDEB86B92"
		},
		{
			"etask.entity": "sc019613",
			"id": "2FBAD011-776F-69BD-68AE-B8B4534F0B26"
		},
		{
			"etask.entity": "sc019614",
			"id": "5E18A495-5517-9370-AA95-4F9F108255B2"
		},
		{
			"etask.entity": "sc019615",
			"id": "6C6A4263-F179-1E77-91C6-6A7D21A625FD"
		},
		{
			"etask.entity": "sc019616",
			"id": "416B6D94-4594-C0B0-1291-FAD43F467ACD"
		},
		{
			"etask.entity": "sc019617",
			"id": "197DAA07-61F6-E886-AD76-29D4FF8F2C7D"
		},
		{
			"etask.entity": "sc019618",
			"id": "3D9FE232-3246-040F-6D06-08890F2E0121"
		},
		{
			"etask.entity": "sc019619",
			"id": "7FD03E50-1E28-141F-A545-E17A21DDD3D6"
		},
		{
			"etask.entity": "sc019620",
			"id": "0CC718EB-5CB4-AD79-E61C-A23716FF3992"
		},
		{
			"etask.entity": "sc019621",
			"id": "E4F11BAE-0B92-0E70-FED2-05A87A2EE266"
		},
		{
			"etask.entity": "sc019622",
			"id": "E4C46C63-597B-A048-42B3-02D2FD5880D2"
		},
		{
			"etask.entity": "sc019623",
			"id": "9CA9E03F-9068-E73E-4BF1-990D0C4C1001"
		},
		{
			"etask.entity": "sc019624",
			"id": "615FC520-C976-7C40-E136-7CE754385F41"
		},
		{
			"etask.entity": "sc019625",
			"id": "26C1F2AE-8295-4943-1ED0-43EE28E69E5E"
		},
		{
			"etask.entity": "sc019626",
			"id": "510017FE-FFA0-F81A-9046-BAC1078030B3"
		},
		{
			"etask.entity": "sc019627",
			"id": "F6E43AFA-374A-B9A2-D477-6B66CE5625C7"
		},
		{
			"etask.entity": "sc019628",
			"id": "9A70F971-80AA-A0C5-C548-828145981360"
		},
		{
			"etask.entity": "sc019629",
			"id": "832A41B9-AAF5-8C3E-F6E4-D763768B415F"
		},
		{
			"etask.entity": "sc019630",
			"id": "BF5C44A5-A0EA-A66E-40E5-B354CECC265D"
		},
		{
			"etask.entity": "sc019631",
			"id": "0FC9C96F-8A6D-0756-4D34-0A44B6A9A65D"
		},
		{
			"etask.entity": "sc019632",
			"id": "A3161DF3-C6C4-E1C2-E468-2B13F38E4207"
		},
		{
			"etask.entity": "sc019633",
			"id": "204D84E0-6528-FE5B-ABC9-E20DECB5778F"
		},
		{
			"etask.entity": "sc019634",
			"id": "FA7FD7DD-0712-724A-A2D6-25F802D19861"
		},
		{
			"etask.entity": "sc019635",
			"id": "4BB75D05-BE74-B6A4-0676-E0F5E439657F"
		},
		{
			"etask.entity": "sc019636",
			"id": "D3009C4E-4660-5809-DF15-AADF546DFE7F"
		},
		{
			"etask.entity": "sc019637",
			"id": "51BC6466-AD19-0F66-4CF4-DAA738BDE554"
		},
		{
			"etask.entity": "sc019638",
			"id": "C17F902C-8758-F92D-F74C-6C242A7D3EE5"
		},
		{
			"etask.entity": "sc019639",
			"id": "50A69C61-D69A-C167-EDD9-9CB083B63AD7"
		},
		{
			"etask.entity": "sc019640",
			"id": "933198B4-BD85-3284-F9F1-06CC831889CB"
		},
		{
			"etask.entity": "sc019641",
			"id": "03B137FD-AA2B-A8DD-8C0E-ACB1DC73F6F2"
		},
		{
			"etask.entity": "sc019642",
			"id": "947BDBC0-112E-ECFF-65B1-67DE7262D7D8"
		},
		{
			"etask.entity": "sc019643",
			"id": "811A6E07-E96F-E6FC-6054-D62A3C61A9CF"
		},
		{
			"etask.entity": "sc019644",
			"id": "8757ED49-8997-A78C-81EF-6D71994BAA15"
		},
		{
			"etask.entity": "sc019645",
			"id": "5D05F31B-550A-5B4F-EC4A-D8CCB0CC969B"
		},
		{
			"etask.entity": "sc019646",
			"id": "F450CA64-7C84-F71A-F44F-4A1FEFB95787"
		},
		{
			"etask.entity": "sc019647",
			"id": "72CD479C-B5BE-60C7-8E78-FFEF593DDF2F"
		},
		{
			"etask.entity": "sc019648",
			"id": "B344D76A-5B91-834D-B9C3-DBA5034508E6"
		},
		{
			"etask.entity": "sc019649",
			"id": "45DF79A8-0137-B59F-C9D6-311FB46BB06E"
		},
		{
			"etask.entity": "sc019650",
			"id": "D18F07A5-E942-655E-B62C-C5DB7519CB68"
		},
		{
			"etask.entity": "sc019651",
			"id": "ECBCE8F3-A3CB-1BE1-86A9-5D39D2236F32"
		},
		{
			"etask.entity": "sc019652",
			"id": "A705DF37-7001-DB1B-F499-088E5B40C171"
		},
		{
			"etask.entity": "sc019653",
			"id": "61913227-AFD9-6710-686C-AB65506044E1"
		},
		{
			"etask.entity": "sc019654",
			"id": "747E5E01-4898-02E8-83E7-93E1E0675BA0"
		},
		{
			"etask.entity": "sc019655",
			"id": "21A94F6E-D402-ED38-0DC0-8DC49D8A0E92"
		},
		{
			"etask.entity": "sc019656",
			"id": "404E32F9-40A0-3B84-C009-C283940DC96E"
		},
		{
			"etask.entity": "sc019657",
			"id": "6DE5967B-E03F-EE4C-A95E-34300B4FA9AB"
		},
		{
			"etask.entity": "sc019658",
			"id": "E573DB9D-D91D-A2EA-84CE-7DD849CA97C1"
		},
		{
			"etask.entity": "sc019659",
			"id": "A8F3C555-9C2A-DB8D-2D7E-D8DAE86C01B5"
		},
		{
			"etask.entity": "sc019660",
			"id": "3CF93859-F363-5D5D-2B7F-A4B3B7BF0617"
		},
		{
			"etask.entity": "sc019661",
			"id": "465AA267-B54B-FC85-A5CB-B79A5DF0D01D"
		},
		{
			"etask.entity": "sc019662",
			"id": "79FE9BF5-13D0-4E53-9EF3-54F9DB4BCECD"
		},
		{
			"etask.entity": "sc019663",
			"id": "A79A93A2-9EF4-4AAC-6AEB-FCFE87C12876"
		},
		{
			"etask.entity": "sc019664",
			"id": "1F8E42F7-A31C-5E7F-57EA-18F218DD4AD0"
		},
		{
			"etask.entity": "sc019665",
			"id": "9C382FD7-FE6D-8E9D-E178-C1F9EF92D1E5"
		},
		{
			"etask.entity": "sc019666",
			"id": "05F6EEA5-6768-1A16-424C-907B10FE8F9B"
		},
		{
			"etask.entity": "sc019667",
			"id": "0F2BACC3-1AAA-3B9F-4FE2-59D2CBF2D46D"
		},
		{
			"etask.entity": "sc019668",
			"id": "FEFA4B26-D9BB-FB69-EBDB-5FAA542F009E"
		},
		{
			"etask.entity": "sc019669",
			"id": "B2E8194F-AA49-D178-364A-86351DE8165C"
		},
		{
			"etask.entity": "sc019670",
			"id": "536BDD46-D18C-AE9A-466C-18F3635348EB"
		},
		{
			"etask.entity": "sc019671",
			"id": "7A6943ED-AB9B-5193-4DEE-33C15F0FB6FE"
		},
		{
			"etask.entity": "sc019672",
			"id": "3EB1D6C9-F5E8-49EF-6648-E001DB6D4138"
		},
		{
			"etask.entity": "sc019673",
			"id": "0758D0A8-1B75-F092-D2B2-7D01D4D56FDB"
		},
		{
			"etask.entity": "sc019674",
			"id": "40900B28-BD4D-7112-8A02-7570D11586F0"
		},
		{
			"etask.entity": "sc019675",
			"id": "CBFDF365-9C8D-5546-04D3-4839A5C13075"
		},
		{
			"etask.entity": "sc019676",
			"id": "4240170E-FBE7-BEF5-BB83-15BD6287EE64"
		},
		{
			"etask.entity": "sc019677",
			"id": "EF6480E2-21C7-BEF6-8ECC-15DD8169F89C"
		},
		{
			"etask.entity": "sc019678",
			"id": "F8BC9B32-282E-D491-4372-D9613127FD4D"
		},
		{
			"etask.entity": "sc019679",
			"id": "593B7473-86C8-F9AF-7FE9-3BCFC6454ECD"
		},
		{
			"etask.entity": "sc019680",
			"id": "B5A40704-2809-50AC-E2E2-C3C33EC505DF"
		},
		{
			"etask.entity": "sc019681",
			"id": "79917F7C-B520-EAFA-4097-BF893685EE83"
		},
		{
			"etask.entity": "sc019682",
			"id": "07FD86F6-389F-0877-E287-C03091450C93"
		},
		{
			"etask.entity": "sc019683",
			"id": "1ABABC63-6AE6-D452-6D2E-E83DC5D1E53D"
		},
		{
			"etask.entity": "sc019684",
			"id": "48821382-9B61-F053-2FB1-DDC285637B51"
		},
		{
			"etask.entity": "sc019685",
			"id": "612B7243-D4E7-ED46-533F-E1774ADD225C"
		},
		{
			"etask.entity": "sc019686",
			"id": "4370A96D-9204-01AA-2E70-2004B14B12E5"
		},
		{
			"etask.entity": "sc019687",
			"id": "9FF7A0FA-015B-80E4-47B9-AB8B85184785"
		},
		{
			"etask.entity": "sc019688",
			"id": "65688FF7-C0B5-06D4-9EB4-B7CD5605892B"
		},
		{
			"etask.entity": "sc019689",
			"id": "44C053F9-8DA3-ABA2-53E6-A2D0507B485D"
		},
		{
			"etask.entity": "sc019690",
			"id": "FF59F74D-E59F-60A4-7975-E4BFE5E957D4"
		},
		{
			"etask.entity": "sc019691",
			"id": "58AE68DF-48FA-8260-C4DC-16B59F1490C9"
		},
		{
			"etask.entity": "sc019692",
			"id": "DA7A5EC5-7EBA-F09C-0514-E52F655725C4"
		},
		{
			"etask.entity": "sc019693",
			"id": "5B8EF171-C8E0-E22C-2D1E-C67AEA224073"
		},
		{
			"etask.entity": "sc019694",
			"id": "8B6D2C6F-325B-5ADF-961D-063C334D8BEA"
		},
		{
			"etask.entity": "sc019695",
			"id": "EDF8DC2F-C8EE-7932-7269-1D6D1C522F26"
		},
		{
			"etask.entity": "sc019696",
			"id": "3EC2711D-F0FD-FDE8-3E8E-7A4B2350DBC6"
		},
		{
			"etask.entity": "sc019697",
			"id": "9E73F915-A679-CD85-ADE1-955F2DE636FC"
		},
		{
			"etask.entity": "sc019698",
			"id": "973F793B-F604-CA72-9FEF-C76F2B205281"
		},
		{
			"etask.entity": "sc019699",
			"id": "8FCF7540-8436-E606-9D6F-8C5714D897A8"
		},
		{
			"etask.entity": "sc019700",
			"id": "2172EE84-D474-13DF-DA86-52D143D414D2"
		},
		{
			"etask.entity": "sc019701",
			"id": "D86E2E28-4535-3194-3F7F-562343CC35B1"
		},
		{
			"etask.entity": "sc019702",
			"id": "776A6F58-81CC-2FDA-792B-E43DC0479480"
		},
		{
			"etask.entity": "sc019703",
			"id": "32607381-D5D0-09A9-1C4E-4B6980A103B5"
		},
		{
			"etask.entity": "sc019704",
			"id": "DC1435AB-365F-2DE4-B562-9AD19DC7D1C0"
		},
		{
			"etask.entity": "sc019705",
			"id": "CC9124D7-3EB7-B764-C8E3-3D254578CCBA"
		},
		{
			"etask.entity": "sc019706",
			"id": "5B70A77E-1516-2670-D088-DD5E725FA8BA"
		},
		{
			"etask.entity": "sc019707",
			"id": "38AD6FE3-84DD-D2F2-1A1E-112745694382"
		},
		{
			"etask.entity": "sc019708",
			"id": "29A65539-5C11-94C7-3465-9E421F18070D"
		},
		{
			"etask.entity": "sc019709",
			"id": "68DA347F-1372-D403-D136-AC6EDFD89340"
		},
		{
			"etask.entity": "sc019710",
			"id": "C5A8D2EC-C494-8646-4DF8-6C0C3DD84226"
		},
		{
			"etask.entity": "sc019711",
			"id": "BB9C91D7-D9C8-0584-8ABD-81C9958422D0"
		},
		{
			"etask.entity": "sc019712",
			"id": "4BCE0E57-5228-AD4B-5D4B-B0B471E0F352"
		},
		{
			"etask.entity": "sc019713",
			"id": "FB9FD1A8-AEF0-86B7-279B-52BE0CF37A24"
		},
		{
			"etask.entity": "sc019714",
			"id": "0FF636DF-4EAA-090D-1728-426A40F41F45"
		},
		{
			"etask.entity": "sc019715",
			"id": "145D4075-87C9-7F9E-4245-38BEB313B802"
		},
		{
			"etask.entity": "sc019716",
			"id": "84EEEFF9-958E-CFDD-B0F1-0B1C12162F8C"
		},
		{
			"etask.entity": "sc019717",
			"id": "FE3072C0-F040-C52C-62BB-31E637132C61"
		},
		{
			"etask.entity": "sc019718",
			"id": "5D1119CC-CEB2-72B7-7566-C54A93349478"
		},
		{
			"etask.entity": "sc019719",
			"id": "6FB8739D-E3CF-DC1E-7A09-46CB1F4BAFC3"
		},
		{
			"etask.entity": "sc019720",
			"id": "E8E5A6A2-5B1F-BC9A-94FC-DFD0EB99E588"
		},
		{
			"etask.entity": "sc019721",
			"id": "AD08A9E5-73DC-ED36-E4F6-DCCAB055C0C9"
		},
		{
			"etask.entity": "sc019722",
			"id": "7D9FC154-8110-367F-78A7-46B45E2034D9"
		},
		{
			"etask.entity": "sc019723",
			"id": "E12D0CAF-B866-C737-2DF8-3AE22EF16644"
		},
		{
			"etask.entity": "sc019724",
			"id": "EA505318-90E9-CC7A-CF2A-A596211C8832"
		},
		{
			"etask.entity": "sc019725",
			"id": "08F804A7-38A2-021A-C56F-750BE1D153DC"
		},
		{
			"etask.entity": "sc019726",
			"id": "7541526E-85D2-D449-6A2D-EAD4EE27B05B"
		},
		{
			"etask.entity": "sc019727",
			"id": "88604D40-9EC3-F2D7-245D-CAE59421437C"
		},
		{
			"etask.entity": "sc019728",
			"id": "997ABBAD-A1D9-96C4-5FF1-9D79A72F00D2"
		},
		{
			"etask.entity": "sc019729",
			"id": "0C97F6D6-F925-2DF6-9240-5A4EDB672291"
		},
		{
			"etask.entity": "sc019730",
			"id": "15491850-BB77-9B23-9658-99EB61FE42BE"
		},
		{
			"etask.entity": "sc019731",
			"id": "69C2E3A1-C1B6-65B4-64B5-775E57F8788F"
		},
		{
			"etask.entity": "sc019732",
			"id": "5B247991-BE13-6AD6-B429-814BD39B4201"
		},
		{
			"etask.entity": "sc019733",
			"id": "6FBCAF6D-35B5-1B84-3747-A5F724B9D151"
		},
		{
			"etask.entity": "sc019734",
			"id": "15AD93E3-AC5B-332A-CE9D-A1A98908A002"
		},
		{
			"etask.entity": "sc019735",
			"id": "DCE4AC9A-725E-470A-6548-0140BC81F0BE"
		},
		{
			"etask.entity": "sc019736",
			"id": "C6457BB3-644A-BF3D-47E8-AD3F930E01A9"
		},
		{
			"etask.entity": "sc019737",
			"id": "27BD7A47-D4BA-6D4C-182F-04C7F9E67629"
		},
		{
			"etask.entity": "sc019738",
			"id": "353BBAD8-FAD2-A266-86CD-737D8A8729B2"
		},
		{
			"etask.entity": "sc019739",
			"id": "E8A79179-0E76-385C-7840-4A0ED8021A19"
		},
		{
			"etask.entity": "sc019740",
			"id": "E921B5A7-C81E-B3B9-1B79-37714FA608A3"
		},
		{
			"etask.entity": "sc019741",
			"id": "69AAD03A-B930-1AE0-37FA-6B768BF8FC8E"
		},
		{
			"etask.entity": "sc019742",
			"id": "01161B37-EB99-55A6-C723-FF2B02E66256"
		},
		{
			"etask.entity": "sc019743",
			"id": "43288B90-2362-86A7-07E6-92AE65EC2CBD"
		},
		{
			"etask.entity": "sc019744",
			"id": "61547EA2-899E-4CFA-2759-C7AB5D1530FD"
		},
		{
			"etask.entity": "sc019745",
			"id": "2F799080-C83F-9A24-BA92-D9E6458A4AC9"
		},
		{
			"etask.entity": "sc019746",
			"id": "61437791-74E3-CF27-79ED-372C6C62443D"
		},
		{
			"etask.entity": "sc019747",
			"id": "021487D8-3954-6912-BAD4-E7AFBA97E1A0"
		},
		{
			"etask.entity": "sc019748",
			"id": "0C876B28-83CE-7830-4A3B-D185A437003E"
		},
		{
			"etask.entity": "sc019749",
			"id": "D6A912F4-7051-0DE0-8620-9ECFB2D2B58B"
		},
		{
			"etask.entity": "sc019750",
			"id": "3A64F119-DAD2-CD06-9581-9444417FDF84"
		},
		{
			"etask.entity": "sc019751",
			"id": "833B7A19-C797-9CDE-498D-B7FF18CF36AC"
		},
		{
			"etask.entity": "sc019752",
			"id": "2B5623FA-0565-E9B0-DAC6-AFF51F0F2B43"
		},
		{
			"etask.entity": "sc019753",
			"id": "4942A308-7B6B-38BB-5CAB-2782FD4CF720"
		},
		{
			"etask.entity": "sc019754",
			"id": "2410AD1D-E274-D8A6-409E-19D7B3BC2DF8"
		},
		{
			"etask.entity": "sc019755",
			"id": "049B02EC-70DF-EA65-F6C1-B1442C36674B"
		},
		{
			"etask.entity": "sc019756",
			"id": "07DA36CA-070F-5812-9F06-9CF505785DBF"
		},
		{
			"etask.entity": "sc019757",
			"id": "FF1F23A8-26B5-D05C-AF38-3D461C862E1F"
		},
		{
			"etask.entity": "sc019758",
			"id": "FAA2412C-0CE5-6240-571D-8FE97EF6AD02"
		},
		{
			"etask.entity": "sc019759",
			"id": "94C56B02-0D4A-50BF-5589-36DAEB3CD447"
		},
		{
			"etask.entity": "sc019760",
			"id": "BF1E2190-28E5-CDEB-FAAA-717F488E0E5A"
		},
		{
			"etask.entity": "sc019761",
			"id": "9EF4A195-04A0-B450-2C85-A84EDCD4138C"
		},
		{
			"etask.entity": "sc019762",
			"id": "AB4354EB-8AA5-1E2E-8C46-55D0A3593302"
		},
		{
			"etask.entity": "sc019763",
			"id": "99D1F6F7-0F4B-2334-C98A-80CF4DC2065C"
		},
		{
			"etask.entity": "sc019764",
			"id": "8C42DB63-0E69-2D19-8D7E-F187C264331B"
		},
		{
			"etask.entity": "sc019765",
			"id": "756E7AFF-3F42-3397-F80B-97969D719602"
		},
		{
			"etask.entity": "sc019766",
			"id": "3506F678-ED53-6839-4809-CE22C17AA747"
		},
		{
			"etask.entity": "sc019767",
			"id": "B311210C-BC6F-5C96-461E-3A7FE91B9F70"
		},
		{
			"etask.entity": "sc019768",
			"id": "2ADF6D39-62D9-2CEE-4CB6-236C1D72E0E2"
		},
		{
			"etask.entity": "sc019769",
			"id": "61039963-87BF-5180-3B50-602539C98A6D"
		},
		{
			"etask.entity": "sc019770",
			"id": "DDFA7D41-4DFE-EB6D-6AB8-3C96AD8C8EBB"
		},
		{
			"etask.entity": "sc019771",
			"id": "7D02C2F6-59A7-BB43-7119-6EE757F5D684"
		},
		{
			"etask.entity": "sc019772",
			"id": "83A5ED93-583A-220C-2116-4FF4D9A98302"
		},
		{
			"etask.entity": "sc019773",
			"id": "608B3835-911E-8708-C910-87462E9E505F"
		},
		{
			"etask.entity": "sc019774",
			"id": "4B7B9F56-1A27-B016-975F-950C49D2DCD8"
		},
		{
			"etask.entity": "sc019775",
			"id": "C279A77D-0D69-98CE-D3F4-ADCD6F5D9061"
		},
		{
			"etask.entity": "sc019776",
			"id": "A6C793DD-A55C-AFA5-0CAD-7CDEFEB2C2FA"
		},
		{
			"etask.entity": "sc019777",
			"id": "60877522-E9A0-5A24-72C1-4088C465F787"
		},
		{
			"etask.entity": "sc019778",
			"id": "79A86963-2CAA-EE70-9EE7-C6A2622D790E"
		},
		{
			"etask.entity": "sc019779",
			"id": "F4AD17D1-D8C7-9B53-7255-07B188DBCEC2"
		},
		{
			"etask.entity": "sc019780",
			"id": "D6AC0473-5874-714A-E06D-F488B4BBF72F"
		},
		{
			"etask.entity": "sc019781",
			"id": "3E9D6541-8FDF-BC85-8A3C-4D442576E9DC"
		},
		{
			"etask.entity": "sc019782",
			"id": "68CEA023-740A-F3A0-72F0-62C356DEAE85"
		},
		{
			"etask.entity": "sc019783",
			"id": "6E95E365-34BA-19EC-0A27-CD60AD6B5EF7"
		},
		{
			"etask.entity": "sc019784",
			"id": "C45FBDA9-A496-088D-C003-1944416EF39D"
		},
		{
			"etask.entity": "sc019785",
			"id": "43B576EB-E4C3-4907-8E4F-BF333BD81DF0"
		},
		{
			"etask.entity": "sc019786",
			"id": "D5DA8528-46D1-72AF-A4E1-C314B759C76D"
		},
		{
			"etask.entity": "sc019787",
			"id": "E0FAD857-27DC-2E1E-04EF-B352740AD1ED"
		},
		{
			"etask.entity": "sc019788",
			"id": "3126C862-29FB-64E8-944D-E327B45E29E1"
		},
		{
			"etask.entity": "sc019789",
			"id": "E4ACA3D5-9A9C-1CE4-3933-25B82834EE71"
		},
		{
			"etask.entity": "sc019790",
			"id": "910F193E-438E-B51E-3B86-82768101E581"
		},
		{
			"etask.entity": "sc019791",
			"id": "F5E30D43-6737-2D53-0CBD-3E4D89B16E56"
		},
		{
			"etask.entity": "sc019792",
			"id": "740201DF-86F2-88F8-6401-9B698C3A80F2"
		},
		{
			"etask.entity": "sc019793",
			"id": "4E0E1514-ABD4-A57D-37EE-0C44DCFE28D9"
		},
		{
			"etask.entity": "sc019794",
			"id": "4980076D-3174-97A7-2123-46211B3476C8"
		},
		{
			"etask.entity": "sc019795",
			"id": "B1E24396-AD5E-E1F8-62F4-A9B073B1137F"
		},
		{
			"etask.entity": "sc019796",
			"id": "C02F42DF-216D-3C77-123D-2F541BF25C7B"
		},
		{
			"etask.entity": "sc019797",
			"id": "B69CF8C7-B89A-736C-4744-039010767D31"
		},
		{
			"etask.entity": "sc019798",
			"id": "13325D3F-D187-BCB0-76E1-068ADB714488"
		},
		{
			"etask.entity": "sc019799",
			"id": "F7FE73BD-229A-3E1E-1A67-67E437CFC36C"
		},
		{
			"etask.entity": "sc019800",
			"id": "584173E7-489F-D7A2-BF51-24C5DE540D93"
		},
		{
			"etask.entity": "sc019801",
			"id": "AE3F8B5A-A42B-58AA-659C-E04DFDC3D110"
		},
		{
			"etask.entity": "sc019802",
			"id": "E5FA900A-C59A-C8E2-1880-D2D5B2CB5722"
		},
		{
			"etask.entity": "sc019803",
			"id": "F006316F-00B3-3135-FDE0-4DB1D796304F"
		},
		{
			"etask.entity": "sc019804",
			"id": "16FE6992-9920-3913-91CE-3AA0D8CCCCD5"
		},
		{
			"etask.entity": "sc019805",
			"id": "C8B70B1A-CD17-2AB6-6416-C32F20BACBB6"
		},
		{
			"etask.entity": "sc019806",
			"id": "CA08F0E5-DB03-03BD-3B46-402EC2A656F5"
		},
		{
			"etask.entity": "sc019807",
			"id": "A90E723F-54FF-7554-46A2-A074BB247F84"
		},
		{
			"etask.entity": "sc019808",
			"id": "46DBA8BA-2842-0ADA-F971-F84321A9CE58"
		},
		{
			"etask.entity": "sc019809",
			"id": "63C74255-6225-B59C-A5F1-7587BA89792F"
		},
		{
			"etask.entity": "sc019810",
			"id": "BFEF385E-12BD-14C8-4377-1617A1E9E1A1"
		},
		{
			"etask.entity": "sc019811",
			"id": "E5173DC4-2EF3-242B-033D-21573DFADE28"
		},
		{
			"etask.entity": "sc019812",
			"id": "1CFE7B1E-B3E6-4463-CCA3-D84FF3459C32"
		},
		{
			"etask.entity": "sc019813",
			"id": "5637480C-C8E3-D35E-5F7D-AEFFB81A1196"
		},
		{
			"etask.entity": "sc019814",
			"id": "EB6A5B7A-4720-DA59-E4C1-F9252441E1EB"
		},
		{
			"etask.entity": "sc019815",
			"id": "9517B795-EFDE-EF7C-DF86-C8CE9690A01A"
		},
		{
			"etask.entity": "sc019816",
			"id": "5835F4A4-C113-47D8-D310-6883C60DB32B"
		},
		{
			"etask.entity": "sc019817",
			"id": "7E264A0A-C49E-CD9B-EB9A-F341C24DE7A8"
		},
		{
			"etask.entity": "sc019818",
			"id": "33041689-C59C-5A78-CA4D-AECD67E9FF34"
		},
		{
			"etask.entity": "sc019819",
			"id": "57A0D46C-092E-1604-6B15-62E881A804E8"
		},
		{
			"etask.entity": "sc019820",
			"id": "0E1E8BD5-D35C-1147-61F4-7F70B6536C69"
		},
		{
			"etask.entity": "sc019821",
			"id": "88BB36E4-2351-0959-3EC3-1C4C0909D038"
		},
		{
			"etask.entity": "sc019822",
			"id": "E30AF500-8EEA-7C7C-AB8C-2C74044BB0BD"
		},
		{
			"etask.entity": "sc019823",
			"id": "70FB7A44-AE41-5E9A-5B24-DE4BED11C3AB"
		},
		{
			"etask.entity": "sc019824",
			"id": "3DBB1E4B-CB17-F28D-1EE4-08C07F2C7A14"
		},
		{
			"etask.entity": "sc019825",
			"id": "9EBAEC52-AE7B-4841-B214-C5CCFCCE4B55"
		},
		{
			"etask.entity": "sc019826",
			"id": "766D8630-F1BD-8564-53BA-49EC73A12B2B"
		},
		{
			"etask.entity": "sc019827",
			"id": "A258C29B-741F-D595-8646-54129206DC21"
		},
		{
			"etask.entity": "sc019828",
			"id": "7E6C5C18-70F6-7F3A-8343-4FCFAB0702C6"
		},
		{
			"etask.entity": "sc019829",
			"id": "B4CD2B88-A2B6-81D3-1145-CE39F1AC404A"
		},
		{
			"etask.entity": "sc019830",
			"id": "26E769E1-6382-A707-E858-2C2697BB9C73"
		},
		{
			"etask.entity": "sc019831",
			"id": "CC559F9D-C1F0-5F14-90E8-A15B6F96B6E4"
		},
		{
			"etask.entity": "sc019832",
			"id": "0CD51D75-61C2-F3DB-11E3-E2619A57A661"
		},
		{
			"etask.entity": "sc019833",
			"id": "FFD5DE92-E38A-751F-2E8A-DE527F3921E7"
		},
		{
			"etask.entity": "sc019834",
			"id": "8B8ED6AB-57E1-FB71-4801-C69B21B4ABF1"
		},
		{
			"etask.entity": "sc019835",
			"id": "3BB2E0BF-9F1E-7808-A0E9-64DB978DE582"
		},
		{
			"etask.entity": "sc019836",
			"id": "BA57ABA0-0BA9-8ECB-2B50-957363242236"
		},
		{
			"etask.entity": "sc019837",
			"id": "00FA46CE-22C4-C9AF-3391-89338CD89B8C"
		},
		{
			"etask.entity": "sc019838",
			"id": "AA8D039D-040F-E847-7A0B-65A1293A4445"
		},
		{
			"etask.entity": "sc019839",
			"id": "DF854B9D-5CEF-17D0-806B-30094DA43D77"
		},
		{
			"etask.entity": "sc019840",
			"id": "802F78F6-30E9-9168-3866-B8D7FDF4E66D"
		},
		{
			"etask.entity": "sc019841",
			"id": "702AF58A-31CE-45D6-8314-DD80D93826B6"
		},
		{
			"etask.entity": "sc019842",
			"id": "F31E418D-4472-DD07-824A-1864AF6EB368"
		},
		{
			"etask.entity": "sc019843",
			"id": "DDAD12D5-4A8D-D578-67AE-FAFEBD66A57F"
		},
		{
			"etask.entity": "sc019844",
			"id": "2ADC8DD0-FB23-F00D-6A2F-1DB975674252"
		},
		{
			"etask.entity": "sc019845",
			"id": "F9592D51-FC3C-1B32-31EA-277E7D42E9FC"
		},
		{
			"etask.entity": "sc019846",
			"id": "8C8A74D4-BA67-AB36-0D3D-BD5E2A8010FD"
		},
		{
			"etask.entity": "sc019847",
			"id": "AF40690C-FF3E-96BE-EE23-9B3624055425"
		},
		{
			"etask.entity": "sc019848",
			"id": "9E13B5EC-D1E5-27C6-ABBD-A844C85F4EBB"
		},
		{
			"etask.entity": "sc019849",
			"id": "8E0364C3-13D0-1FED-667F-3695F629426E"
		},
		{
			"etask.entity": "sc019850",
			"id": "93D9BCF6-BC9D-EF3E-4F1D-7D3BB2195374"
		},
		{
			"etask.entity": "sc019851",
			"id": "323E5B68-1214-9887-0668-3787D0B6E3C5"
		},
		{
			"etask.entity": "sc019852",
			"id": "2AC9F648-9480-72DD-8CCC-60B0D9399FA5"
		},
		{
			"etask.entity": "sc019853",
			"id": "F9382A87-7921-A073-B869-E661744E4644"
		},
		{
			"etask.entity": "sc019854",
			"id": "2B426FF1-558C-291C-55B5-9651DCF59508"
		},
		{
			"etask.entity": "sc019855",
			"id": "1E86D5FD-20E8-89C7-4F98-DF7582B87EAE"
		},
		{
			"etask.entity": "sc019856",
			"id": "4AE7C440-8372-8829-B29D-57A4A0EAEA26"
		},
		{
			"etask.entity": "sc019857",
			"id": "88E4A54D-0762-C02A-F541-20969C6FC1D4"
		},
		{
			"etask.entity": "sc019858",
			"id": "781FF810-01EA-53E3-6DCB-ECE265B34338"
		},
		{
			"etask.entity": "sc019859",
			"id": "F30E3D64-7EA6-076D-F48A-F7E26EA51236"
		},
		{
			"etask.entity": "sc019860",
			"id": "2E9C69F6-69A4-3D61-99A3-DB307AE184E0"
		},
		{
			"etask.entity": "sc019861",
			"id": "D7CC3F15-F257-55B1-1A45-F5B93D6B299C"
		},
		{
			"etask.entity": "sc019862",
			"id": "E9FAA5B7-0B42-4BA0-041E-21CBD0615105"
		},
		{
			"etask.entity": "sc019863",
			"id": "F9EDC0CA-D1A9-2C33-7E2F-263DD5C45964"
		},
		{
			"etask.entity": "sc019864",
			"id": "50534FB1-E170-0EC2-836A-4D023190C503"
		},
		{
			"etask.entity": "sc019865",
			"id": "CFE3CC52-E4AB-A23B-5796-7EB7B5DB2235"
		},
		{
			"etask.entity": "sc019866",
			"id": "3E6E67DA-DA45-ACE2-3C88-D299A684A8BA"
		},
		{
			"etask.entity": "sc019867",
			"id": "D89724EC-A80A-6294-04C1-C3FDF45F6073"
		},
		{
			"etask.entity": "sc019868",
			"id": "71CBBFE2-523C-E6ED-2BCB-B753FD9AB86A"
		},
		{
			"etask.entity": "sc019869",
			"id": "ACCE4D64-9D3A-DD81-79CD-D0350A38CAB4"
		},
		{
			"etask.entity": "sc019870",
			"id": "3DA6A56E-0A7C-0E5C-796B-7AE8E1AFB296"
		},
		{
			"etask.entity": "sc019871",
			"id": "17CCC8E8-4A43-5D51-E659-8A5B0E4A98B6"
		},
		{
			"etask.entity": "sc019872",
			"id": "694F64C5-4BAF-DD41-32E9-1215D129DCC1"
		},
		{
			"etask.entity": "sc019873",
			"id": "53657282-A542-8F9E-0124-B306DE9DC966"
		},
		{
			"etask.entity": "sc019874",
			"id": "A8A2B2FB-580D-E9AF-C15B-F9D4BA447F82"
		},
		{
			"etask.entity": "sc019875",
			"id": "CA0A2A8D-2BB0-C9CE-905A-9DE0B400FBB0"
		},
		{
			"etask.entity": "sc019876",
			"id": "5E949D9C-1D87-B18B-8A52-60A5E4BB9D42"
		},
		{
			"etask.entity": "sc019877",
			"id": "8D1E366F-A371-44FA-7F82-44B085E981F2"
		},
		{
			"etask.entity": "sc019878",
			"id": "96F38238-9ACE-8731-65F3-52EC354BF32A"
		},
		{
			"etask.entity": "sc019879",
			"id": "494A3971-6848-1F45-98C4-95C9B921C33B"
		},
		{
			"etask.entity": "sc019880",
			"id": "97BE53A8-322B-2E9A-D35F-75BA0B33E1DA"
		},
		{
			"etask.entity": "sc019881",
			"id": "46CAEF55-8716-E233-49AB-8B0D650EF409"
		},
		{
			"etask.entity": "sc019882",
			"id": "0517E351-D0E7-EED9-8EF6-A1DC9F1AA002"
		},
		{
			"etask.entity": "sc019883",
			"id": "AF91D8A9-115E-8A35-36A2-C218B92DF505"
		},
		{
			"etask.entity": "sc019884",
			"id": "BB99190F-E411-7337-D6B5-12BC35AA3568"
		},
		{
			"etask.entity": "sc019885",
			"id": "8FC9127D-1CB6-9BEA-9B20-3AA43A5F4FB6"
		},
		{
			"etask.entity": "sc019886",
			"id": "25CF06A3-6B5C-2B55-FE96-C4EE2042640C"
		},
		{
			"etask.entity": "sc019887",
			"id": "C46317FC-11EE-98B1-99B8-4843F1090719"
		},
		{
			"etask.entity": "sc019888",
			"id": "D97EE6A3-9D61-56FB-9408-0EA9A1C888A6"
		},
		{
			"etask.entity": "sc019889",
			"id": "5CD332A8-DBFF-7E78-217A-C13CC03FCC5D"
		},
		{
			"etask.entity": "sc019890",
			"id": "A784E8E4-FD97-0BB3-3A04-E70B3DB52F22"
		},
		{
			"etask.entity": "sc019891",
			"id": "6D5B75AA-0C93-AD64-E93A-1553706DBE69"
		},
		{
			"etask.entity": "sc019892",
			"id": "6ED43D53-4B1D-C8EE-FA11-33E511ED717F"
		},
		{
			"etask.entity": "sc019893",
			"id": "78B0AD6C-4E92-3E19-BED4-8A8E4B9096D8"
		},
		{
			"etask.entity": "sc019894",
			"id": "D7A2198C-4B02-36F4-E0B1-C0B466514DC7"
		},
		{
			"etask.entity": "sc019895",
			"id": "0A0A57E3-5AC9-6D6F-6CEE-F3784DC3A62A"
		},
		{
			"etask.entity": "sc019896",
			"id": "A43AF9AB-7762-76FB-922B-E3AE81BB4AF4"
		},
		{
			"etask.entity": "sc019897",
			"id": "8BC588B2-F8FC-67BA-C94B-AC544CDD24E4"
		},
		{
			"etask.entity": "sc019898",
			"id": "1FC01277-51FD-9FF7-4E1B-8561CAC4E980"
		},
		{
			"etask.entity": "sc019899",
			"id": "B79EF97D-EE57-7AA7-B52E-6F7240C036D2"
		},
		{
			"etask.entity": "sc019900",
			"id": "A82E310B-4101-63B6-7EFD-38E5273BE3A6"
		},
		{
			"etask.entity": "sc019901",
			"id": "6BA7533F-D09F-9DAE-CB34-31CA0817AD3E"
		},
		{
			"etask.entity": "sc019902",
			"id": "837DEFA7-C141-36B8-DC8A-B5BF16FE435A"
		},
		{
			"etask.entity": "sc019903",
			"id": "9FEDD2F6-EC7F-42BA-70FD-7C2DE9856CA7"
		},
		{
			"etask.entity": "sc019904",
			"id": "8D9503FA-8A9D-A9B7-8396-E2DF7CF3FA60"
		},
		{
			"etask.entity": "sc019905",
			"id": "A308D0EE-6564-A50A-3A69-F595B1F27B57"
		},
		{
			"etask.entity": "sc019906",
			"id": "8C2D5097-20BB-5E1B-942B-7176EA5C5093"
		},
		{
			"etask.entity": "sc019907",
			"id": "2AC54F63-0A8F-FA1F-4666-8CE2D01FDE6E"
		},
		{
			"etask.entity": "sc019908",
			"id": "730B5BCC-FB07-CD43-E3EC-CA208701FFF9"
		},
		{
			"etask.entity": "sc019909",
			"id": "BFF24637-0BC0-17C2-F4A0-7CD0189138D0"
		},
		{
			"etask.entity": "sc019910",
			"id": "3C5AADFB-E46F-90B1-BE1F-8DFF4F0E8BE6"
		},
		{
			"etask.entity": "sc019911",
			"id": "9AC65B4C-009F-1556-D9B4-DF5AB9BDA3DF"
		},
		{
			"etask.entity": "sc019912",
			"id": "AC0F03C2-3125-10AC-13B9-39B5E1AB7F46"
		},
		{
			"etask.entity": "sc019913",
			"id": "C6ADB76C-4639-CABF-7976-37FB9D1BBDE5"
		},
		{
			"etask.entity": "sc019914",
			"id": "6B02F18B-C1B3-4FD0-6F6A-4AB9C6B95BC5"
		},
		{
			"etask.entity": "sc019915",
			"id": "3645FD1E-F1DF-1EB2-CBB8-FF11219A0C99"
		},
		{
			"etask.entity": "sc019916",
			"id": "27D48D1E-5A9A-4325-4577-94611BA8E8FE"
		},
		{
			"etask.entity": "sc019917",
			"id": "6CCB80BF-1FAC-669B-E48F-51528C35F100"
		},
		{
			"etask.entity": "sc019918",
			"id": "3C200108-B0AB-2D1B-D19F-B11E45C82901"
		},
		{
			"etask.entity": "sc019919",
			"id": "5B01A52C-7585-68C9-C41D-B24BE0131178"
		},
		{
			"etask.entity": "sc019920",
			"id": "8F67E890-6BD7-F367-C7AC-C63876537AFF"
		},
		{
			"etask.entity": "sc019921",
			"id": "A53686BE-F14A-D8A7-B153-3D8276B4F49E"
		},
		{
			"etask.entity": "sc019922",
			"id": "44DACAFE-F0AC-BB93-D0E5-2D09BEFAF141"
		},
		{
			"etask.entity": "sc019923",
			"id": "C1496C3B-75AF-E13B-8114-7E8E3FDBB081"
		},
		{
			"etask.entity": "sc019924",
			"id": "32760F8A-73F2-661F-26C1-B061B53E269D"
		},
		{
			"etask.entity": "sc019925",
			"id": "FE82311A-0BFE-874D-DA12-D2B86D23BA1F"
		},
		{
			"etask.entity": "sc019926",
			"id": "DC627742-33A3-C423-5E6D-C537783EC93B"
		},
		{
			"etask.entity": "sc019927",
			"id": "1E9879A5-4572-A3E3-7661-09F36C3EC677"
		},
		{
			"etask.entity": "sc019928",
			"id": "0E223235-D00D-53E8-3AF9-DB7403465328"
		},
		{
			"etask.entity": "sc019929",
			"id": "13DB2C67-968A-914C-04D8-668C703FD5BD"
		},
		{
			"etask.entity": "sc019930",
			"id": "F1F7D0F7-27BE-2D93-4961-054E2C7AA033"
		},
		{
			"etask.entity": "sc019931",
			"id": "381C64AB-C182-4FC4-18F8-0B2722609AA3"
		},
		{
			"etask.entity": "sc019932",
			"id": "EA05B70C-D1EF-E07C-315A-E5777A4A7542"
		},
		{
			"etask.entity": "sc019933",
			"id": "9FFE0D7A-CE98-403B-EAFE-7DE438BD7EAD"
		},
		{
			"etask.entity": "sc019934",
			"id": "567FE678-DE10-0FB9-8B51-4B598816F962"
		},
		{
			"etask.entity": "sc019935",
			"id": "8ABD4914-5687-51D2-57B6-7FD042463CB6"
		},
		{
			"etask.entity": "sc019936",
			"id": "D4A0899F-22E0-7ED1-ABDA-B2339327960D"
		},
		{
			"etask.entity": "sc019937",
			"id": "92271C9B-D4F1-7D9E-3F9B-F9A9A795DF78"
		},
		{
			"etask.entity": "sc019938",
			"id": "B6E62179-94B9-2495-1735-A1CF04849FC4"
		},
		{
			"etask.entity": "sc019939",
			"id": "0FFF0738-2102-E92F-519F-57B57D8BCA60"
		},
		{
			"etask.entity": "sc019940",
			"id": "8D1C74DE-2677-847F-49E5-A0A68A317C54"
		},
		{
			"etask.entity": "sc019941",
			"id": "854664C6-DBDC-4B34-40B1-AF6ADEB87437"
		},
		{
			"etask.entity": "sc019942",
			"id": "67CCCD96-264A-1CCC-A560-490A8776C077"
		},
		{
			"etask.entity": "sc019943",
			"id": "32317536-133B-14D7-077F-3E14A06E4608"
		},
		{
			"etask.entity": "sc019944",
			"id": "C888D1E9-235A-AAA5-9F8C-64CA24CC4588"
		},
		{
			"etask.entity": "sc019945",
			"id": "AC545417-8BC1-30B3-10F0-C1503B28A11A"
		},
		{
			"etask.entity": "sc019946",
			"id": "8F02162A-17EC-40AB-34D8-EBDEC2BD067F"
		},
		{
			"etask.entity": "sc019947",
			"id": "4AE559FE-3ED9-EABB-FD51-2F56C837D3D3"
		},
		{
			"etask.entity": "sc019948",
			"id": "79E62BFF-6BF0-434D-93C8-467C9A16B145"
		},
		{
			"etask.entity": "sc019949",
			"id": "81D98795-8BC0-28FC-D594-C811A27D9C91"
		},
		{
			"etask.entity": "sc019950",
			"id": "DA994959-549A-839E-3340-789EF5C1535C"
		},
		{
			"etask.entity": "sc019951",
			"id": "ADF50645-D61A-B6DE-881B-183F805501DE"
		},
		{
			"etask.entity": "sc019952",
			"id": "B2E05AE6-DC51-0886-9EB5-EF49A86D437C"
		},
		{
			"etask.entity": "sc019953",
			"id": "F0B3A893-670F-B442-BD31-16041DFF5E9A"
		},
		{
			"etask.entity": "sc019954",
			"id": "291824A4-506A-1D2B-6DF3-3F844D7616DD"
		},
		{
			"etask.entity": "sc019955",
			"id": "827155FC-60D9-39F6-6EEB-514DF6D0AD04"
		},
		{
			"etask.entity": "sc019956",
			"id": "9F091B2D-0290-BB29-B545-4854A9F41315"
		},
		{
			"etask.entity": "sc019957",
			"id": "4E2DD29C-3C5E-F53C-433B-206409F3E6B4"
		},
		{
			"etask.entity": "sc019958",
			"id": "20C87479-9A87-DD43-1A3A-BD9821143081"
		}
	]
}
```
## /cgtw7.0/etask/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[id_array][] | 6BC17195-9A1D-54E6-F76A-44D87C923BB1 | Array | 是 | ID列表
data[sign_array][] | etask.entity | Array | 是 | 字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[order_sign_array] | - | Array | 否 | 顺序的字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"etask.entity": "Layout",
			"id": "6BC17195-9A1D-54E6-F76A-44D87C923BB1"
		}
	]
}
```
## /cgtw7.0/etask/get_dir
```text
用目录标识列表获取对应的目录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_dir | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[id_array][] | C750174B-15BF-1FB5-0829-000B12D0A484 | Array | 是 | ID列表
data[sign_array][] | proj_entity | Array | 是 | 目录标识列表
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "C750174B-15BF-1FB5-0829-000B12D0A484",
			"proj_entity": "Z:/xiaoying_etask"
		}
	]
}
```
## /cgtw7.0/etask/get_field_and_dir
```text
用目录标识列表和字段标识列表获取对应的目录和字段列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_field_and_dir | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[id_array][] | BE7EF686-0565-1460-01D1-7C7441697A79 | Array | 是 | ID列表
data[folder_sign_array][] | proj_entity | Array | 是 | 字段标识列表
data[os] | win | String | 是 | 系统平台
data[field_sign_array][] | etask.entity | Array | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"etask.entity": "Layout",
			"id": "BE7EF686-0565-1460-01D1-7C7441697A79",
			"proj_entity": "Z:/xiaoying_etask"
		}
	]
}
```
## /cgtw7.0/etask/get_makedirs
```text
获取创建目录的列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_makedirs | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[id_array][] | 6BC17195-9A1D-54E6-F76A-44D87C923BB1 | Array | 是 | ID列表
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/check",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/work",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/approve",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/review/review_file",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/review/review_same",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/review",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/file_ver/file_ver_1",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/folder_ver",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/same_ver/same_ver",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/upgrade_ver/upgrade_fiile",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/upgrade_ver/upgrade_follow",
		"Z:/xiaoying_etask/ep002/seq001/sc001/lay/follow_ver/follow_ver",
		"Z:/xiaoying_etask/ep002/seq001/sc001/ani/check",
		"Z:/xiaoying_etask/ep002/seq001/sc001/ani/work",
		"Z:/xiaoying_etask/sc001/source"
	]
}
```
## /cgtw7.0/etask/get_submit_filebox_sign
```text
获取提交流程的文件框标识列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_submit_filebox_sign | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[id] | 6BC17195-9A1D-54E6-F76A-44D87C923BB1 | String | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"review"
	]
}
```
## /cgtw7.0/etask/get_sign_filebox
```text
根据文件框标识获取文件框设置信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_sign_filebox | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[id] | 6BC17195-9A1D-54E6-F76A-44D87C923BB1 | String | 是 | ID列表
data[filebox_sign] | review | String | 是 | 文件框标识
data[id_array] | - | Array | 否 | ID列表
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"ref_task_id_list": [],
		"ref_pipeline_id": "",
		"#id": "6DC342A2-55E2-A740-ABE2-9C57A443F483",
		"path": "Z:/xiaoying_etask/ep002/seq001/sc001/lay/review/review_file",
		"server": "Z:/",
		"server_id": "D2BF754E-CDD6-8AAA-F28C-3E9D59A55AF9",
		"pipeline_id": "71AF8214-1DFF-86A7-A6D1-BD05FD521122",
		"title": "review_file",
		"sign": "review",
		"color": "#FEC20E",
		"rule": [
			"sc001_{ver}.*",
			"sc001_{ver}"
		],
		"rule_view": [
			"sc001_{ver}.*",
			"sc001_{ver}"
		],
		"show_type": "Files and Folders",
		"is_drag_in": "Y",
		"is_ref": "",
		"ref_id": "",
		"is_approve_version": "",
		"is_upload_online": "Y",
		"online_upload_group": "all",
		"convert_type": [],
		"is_version": "Y",
		"version_type": "file",
		"version_length": "3",
		"is_upgrade_version": "N",
		"is_follow": "N",
		"follow_sign": "",
		"submit_type": "review",
		"drag_in": [
			{
				"plugin_id": "check_rule"
			},
			{
				"plugin_id": "msg_to",
				"account_id": "B8B95A85-36E8-B6FB-DB78-301A358C77F3",
				"is_input_note": "Y"
			}
		],
		"is_move_old_to_history": "N",
		"is_move_same_to_history": "N",
		"is_in_history_add_version": "N",
		"is_in_history_add_datetime": "N",
		"is_cover_disable": "N",
		"is_msg_to_first_qc": "N",
		"show_group_id": "all",
		"max_version": "003",
		"max_version_id": "C200B9AD-01E8-39D1-6203-662DFA8392C5",
		"version_list": [
			"001",
			"002",
			"003"
		],
		"version_id_list": {
			"0E17E772-9ADD-44E0-5338-7CC136215F2A": "001",
			"7F251B2D-F374-3A1A-CA50-3DDA097157DD": "002",
			"C200B9AD-01E8-39D1-6203-662DFA8392C5": "003"
		},
		"last_max_version": "003",
		"last_max_version_id": "C200B9AD-01E8-39D1-6203-662DFA8392C5",
		"last_link_id": "6BC17195-9A1D-54E6-F76A-44D87C923BB1",
		"follow_version": "",
		"follow_title": "",
		"is_submit": "Y",
		"reviewer_account_id": ""
	}
}
```
## /cgtw7.0/etask/get_filebox
```text
获取文件框设置信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_filebox | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[id] | 6BC17195-9A1D-54E6-F76A-44D87C923BB1 | String | 是 | ID列表
data[filebox_id] | 6DC342A2-55E2-A740-ABE2-9C57A443F483 | String | 是 | 文件框Id
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"ref_task_id_list": [],
		"ref_pipeline_id": "",
		"#id": "6DC342A2-55E2-A740-ABE2-9C57A443F483",
		"path": "Z:/xiaoying_etask/ep002/seq001/sc001/lay/review/review_file",
		"server": "Z:/",
		"server_id": "D2BF754E-CDD6-8AAA-F28C-3E9D59A55AF9",
		"pipeline_id": "71AF8214-1DFF-86A7-A6D1-BD05FD521122",
		"title": "review_file",
		"sign": "review",
		"color": "#FEC20E",
		"rule": [
			"sc001_{ver}.*",
			"sc001_{ver}"
		],
		"rule_view": [
			"sc001_{ver}.*",
			"sc001_{ver}"
		],
		"show_type": "Files and Folders",
		"is_drag_in": "Y",
		"is_ref": "",
		"ref_id": "",
		"is_approve_version": "",
		"is_upload_online": "Y",
		"online_upload_group": "all",
		"convert_type": [],
		"is_version": "Y",
		"version_type": "file",
		"version_length": "3",
		"is_upgrade_version": "N",
		"is_follow": "N",
		"follow_sign": "",
		"submit_type": "review",
		"drag_in": [
			{
				"plugin_id": "check_rule"
			},
			{
				"plugin_id": "msg_to",
				"account_id": "B8B95A85-36E8-B6FB-DB78-301A358C77F3",
				"is_input_note": "Y"
			}
		],
		"is_move_old_to_history": "N",
		"is_move_same_to_history": "N",
		"is_in_history_add_version": "N",
		"is_in_history_add_datetime": "N",
		"is_cover_disable": "N",
		"is_msg_to_first_qc": "N",
		"show_group_id": "all",
		"max_version": "003",
		"max_version_id": "C200B9AD-01E8-39D1-6203-662DFA8392C5",
		"version_list": [
			"001",
			"002",
			"003"
		],
		"version_id_list": {
			"0E17E772-9ADD-44E0-5338-7CC136215F2A": "001",
			"7F251B2D-F374-3A1A-CA50-3DDA097157DD": "002",
			"C200B9AD-01E8-39D1-6203-662DFA8392C5": "003"
		},
		"last_max_version": "003",
		"last_max_version_id": "C200B9AD-01E8-39D1-6203-662DFA8392C5",
		"last_link_id": "6BC17195-9A1D-54E6-F76A-44D87C923BB1",
		"follow_version": "",
		"follow_title": "",
		"is_submit": "Y",
		"reviewer_account_id": ""
	}
}
```
## /cgtw7.0/etask/get_review_file
```text
获取可预览最后版本文件,用于视频串播
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_review_file | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[link_id_array][] | 6BC17195-9A1D-54E6-F76A-44D87C923BB1 | Array | 是 | ID列表
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "6BC17195-9A1D-54E6-F76A-44D87C923BB1",
			"path": [
				"Z:/xiaoying_etask/ep002/seq001/sc001/lay/review/review_file/sc001_003.mov"
			],
			"file_path": [
				"Z:/xiaoying_etask/ep002/seq001/sc001/lay/review/review_file/sc001_003.mov"
			],
			"dir": "Z:/xiaoying_etask/ep002/seq001/sc001/lay/review/review_file"
		}
	]
}
```
## /cgtw7.0/etask/get_version_file
```text
获取文件框最后版本文件
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_version_file | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[link_id_array][] | 6BC17195-9A1D-54E6-F76A-44D87C923BB1 | Array | 是 | ID列表
data[os] | win | String | 是 | 系统平台
data[filebox_sign] | review | String | 是 | 文件框标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "6BC17195-9A1D-54E6-F76A-44D87C923BB1",
			"path": [
				"Z:/xiaoying_etask/ep002/seq001/sc001/lay/review/review_file/sc001_003.mov"
			],
			"file_path": [
				"Z:/xiaoying_etask/ep002/seq001/sc001/lay/review/review_file/sc001_003.mov"
			],
			"dir": "Z:/xiaoying_etask/ep002/seq001/sc001/lay/review/review_file"
		}
	]
}
```
## /cgtw7.0/etask/set
```text
更新记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[id_array][] | 6BC17195-9A1D-54E6-F76A-44D87C923BB1 | Array | 是 | ID列表
data[sign_data_array][etask.source_name] | sc001 | Array | 是 | 更新的数据(dict), 格式:{"字段标识" : "值", "字段标识" : "值" }
data[exec_event_filter] | - | Boolean | 否 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/etask/delete
```text
删除记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | delete | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[id_array][] | C750174B-15BF-1FB3-0829-000B12D0A484 | Array | 是 | ID列表
data[exec_event_filter] | - | Boolean | 否 | 执行事件过滤器
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/etask/create
```text
创建记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[type_sign] | eps | String | 是 | 任务类型标识
data[sign_data_array][etask.entity] | ep003 | Array | 是 | 更新的数据(dict), 格式:{"字段标识" : "值", "字段标识" : "值" }
data[sign_data_array][etask.link_etype] | eps | Array | 是 | -
data[sign_data_array][etask.link_id] | "" | Array | 是 | -
data[exec_event_filter] | false | Boolean | 否 | 执行事件过滤器
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "0579F7F2-2C5B-0412-FFFD-5F6F659A5D11"
}
```
## /cgtw7.0/etask/create_task
```text
创建记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[type_sign] | task | String | 是 | 任务类型标识
data[sign_data_array][etask.entity] | sss | Array | 是 | 更新的数据(dict), 格式:{"字段标识" : "值", "字段标识" : "值" }
data[sign_data_array][etask.link_etype] | task | Array | 是 | -
data[sign_data_array][etask.link_id] | 5B7688A3-881C-7408-338C-D8629625B6B8 | Array | 是 | -
data[exec_event_filter] | false | Boolean | 否 | 执行事件过滤器
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "6BA3CE67-59C4-550E-FF48-92AC0DDD49B1"
}
```
## /cgtw7.0/etask/count
```text
统计记录条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "3"
}
```
## /cgtw7.0/etask/distinct
```text
获取去重后的记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | distinct | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[distinct_sign] | etask.entity | String | 是 | 字段标识
data[order_sign_array] | - | Array | 否 | 顺序的字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"ep002",
		"ep003"
	]
}
```
## /cgtw7.0/etask/assign
```text
分配任务给制作人员
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | assign | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[assign_account_id] | {{account_id}} | String | 是 | -
data[start_date] | 2022-02-02 | String | 是 | 开始日期
data[end_date] | 2022-02-02 | String | 是 | 结束日期
data[task_id_array][] | 0579F7F2-2C5B-0412-FFFD-5F6F659A5D11 | Array | 是 | -
data[exec_event_filter] | - | Boolean | 否 | 执行事件过滤器
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/etask/update_flow
```text
修改某审核环节的状态
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | update_flow | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[task_id_array][] | 6BC17195-9A1D-54E6-F76A-44D87C923BB1 | Array | 是 | ID列表
data[field_sign] | etask.leader_status | String | 是 | 字段标识
data[dom_array][] | "" | String | 是 | 内容
data[status] | Approve | String | 是 | 状态
data[retake_pipeline_id_array] | - | Array | 否 | 返修阶段ID列表
data[tag] | - | String | 否 | 标签
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/etask/update_task_status
```text
修改任务状态列
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | update_task_status | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[dom_array][] | "" | Array | 是 | 内容
data[status] | Approve | String | 是 | 状态
data[task_id_array][] | 9C7686D1-60B4-13B0-B3E2-D26EF899B227 | Array | 是 | ID列表
data[retake_pipeline_id_array] | - | Array | 否 | 返修阶段ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/etask/group_count
```text
按字段标识进行分组统计条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | group_count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[sign_filter_array] | - | Array | 否 | 过滤语句列表
data[sign_array][] | etask.entity | Array | 是 | 字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"count": 1,
			"etask.entity": "sc008"
		}
	]
}
```
## /cgtw7.0/etask/send_msg
```text
给指定用户发送任务相关消息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | send_msg | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[account_id_array] | {{account_id}} | Array | 是 | 账号ID列表
data[task_id] | 0579F7F2-2C5B-0412-FFFD-5F6F659A5D11 | String | 是 | Id
data[content][] | "" | Array | 是 | 发送的内容
data[important] | - | Boolean | 否 | 是否强提醒
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/etask/get_sign_data
```text
获取标识数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask | String | 是 | 控制器
data[method] | get_sign_data | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[id_array][] | 9C7686D1-60B4-13B0-B3E2-D26EF899B227 | String | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"9C7686D1-60B4-13B0-B3E2-D26EF899B227": {
			"eps": "ep002",
			"seq": "seq001",
			"shot": "sc001",
			"task": "Animation"
		}
	}
}
```
## /cgtw7.0/etask_type
```text
简易版-分类
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/etask_type/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask_type | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"entity",
		"sign",
		"sort_id",
		"description",
		"create_by",
		"create_time",
		"last_update_time",
		"last_update_by"
	]
}
```
## /cgtw7.0/etask_type/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask_type | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[filter_array][0][] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"9F9A3D13-CD8D-FF2C-65BF-7BCC4F0AFB7C",
		"5587F8E2-BFE0-0EE6-FD83-D4430629771D",
		"37904CDF-FD4A-E215-EF65-2CA9D69D2ADC",
		"5559E825-70A1-2922-50D7-CBB9053DEA47",
		"CAAFB886-4A63-68EC-E919-BF90CD57159A",
		"5050133A-3995-7A31-2D04-EA2846CA925F"
	]
}
```
## /cgtw7.0/etask_type/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask_type | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[field_array][] | entity | Array | 是 | 字段标识列表
data[id_array][] | 9F9A3D13-CD8D-FF2C-65BF-7BCC4F0AFB7C | Array | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "Folder",
			"#id": "9F9A3D13-CD8D-FF2C-65BF-7BCC4F0AFB7C"
		}
	]
}
```
## /cgtw7.0/etask_type/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | etask_type | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_etask | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
data[field_array][] | entity | Array | 是 | 字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"9F9A3D13-CD8D-FF2C-65BF-7BCC4F0AFB7C",
		"5587F8E2-BFE0-0EE6-FD83-D4430629771D",
		"37904CDF-FD4A-E215-EF65-2CA9D69D2ADC",
		"5559E825-70A1-2922-50D7-CBB9053DEA47",
		"CAAFB886-4A63-68EC-E919-BF90CD57159A",
		"5050133A-3995-7A31-2D04-EA2846CA925F"
	]
}
```
## /cgtw7.0/note
```text
批注
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/note/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | note | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"module",
		"from_account_id",
		"dom_text",
		"to_account_id",
		"type",
		"tag",
		"version_id",
		"parent_id",
		"status",
		"module_type",
		"#id",
		"time",
		"#link_id",
		"create_time",
		"last_update_time",
		"create_by",
		"last_update_by",
		"version",
		"link_entity",
		"filename",
		"ee",
		"bb",
		"artist"
	]
}
```
## /cgtw7.0/note/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | note | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"CBA88AF7-5B29-2735-6C3B-0B2E955A349B",
		"CBE183E2-0C8C-E2CE-4805-0E570AB279C3",
		"A529579A-1EA4-C97E-3354-C42BEC71B011",
		"B1E7DEA8-47DC-998F-E2C3-34A177BCBDED",
		"55439681-536F-C357-0936-86825661F7D9"
	]
}
```
## /cgtw7.0/note/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | note | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | Array | 否 | 限制条数,默认5000
data[field_array][] | entity | Array | 是 | 字段标识列表
data[order_field_array] | - | Array | 否 | 排序列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"create_by": "xiaoying",
			"#id": "CBA88AF7-5B29-2735-6C3B-0B2E955A349B"
		},
		{
			"create_by": "xiaoying",
			"#id": "CBE183E2-0C8C-E2CE-4805-0E570AB279C3"
		},
		{
			"create_by": "xiaoying",
			"#id": "A529579A-1EA4-C97E-3354-C42BEC71B011"
		},
		{
			"create_by": "xiaoying",
			"#id": "B1E7DEA8-47DC-998F-E2C3-34A177BCBDED"
		},
		{
			"create_by": "xiaoying",
			"#id": "55439681-536F-C357-0936-86825661F7D9"
		}
	]
}
```
## /cgtw7.0/note/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | note | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id_array][0] | CBA88AF7-5B29-2735-6C3B-0B2E955A349B | Array | 是 | ID列表
data[field_array][] | dom_text | Array | 是 | 字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[order_field_array] | - | Array | 否 | 排序列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"dom_text": "[]",
			"#id": "CBA88AF7-5B29-2735-6C3B-0B2E955A349B"
		}
	]
}
```
## /cgtw7.0/note/set
```text
修改记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | note | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[field_data_array][0[dom_text] | 11 | Array | 是 | 内容
data[id] | CBA88AF7-5B29-2735-6C3B-0B2E955A349B | String | 是 | ID
data[exec_event_filter] | - | Boolean | 否 | 执行事件过滤器
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/note/create
```text
创建记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | note | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[cc_account_id] | - | String | 否 | 抄送账号ID
data[exec_event_filter] | - | Boolean | 否 | 执行事件过滤器
data[field_data_array][module] | shot | Array | 是 | 模块
data[field_data_array][module_type] | info | Array | 是 | 模块类型
data[field_data_array][#link_id] | 49D58EF8-01D9-5A3D-6017-4DEB1BAC9405 | Array | 是 | 任务的ID列表, ','分割
data[field_data_array][from_account_id] | {{account_id}} | Array | 是 | 当前账号id
data[field_data_array][dom_text][0][type] | text | Array | 是 | 内容
data[field_data_array][version_id] | BB57E35F-69E6-7059-2BEC-908ABBDB5F52 | String | 否 | 用于创建到指定版本下
data[field_data_array][dom_text][0][content] | 11 | String | 是 | 插入的文本
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"module",
		"from_account_id",
		"dom_text",
		"to_account_id",
		"type",
		"tag",
		"version_id",
		"parent_id",
		"status",
		"module_type",
		"#id",
		"time",
		"#link_id",
		"create_time",
		"last_update_time",
		"create_by",
		"last_update_by",
		"version",
		"link_entity",
		"filename",
		"ee",
		"bb",
		"artist"
	]
}
```
## /cgtw7.0/note/delete
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | note | String | 是 | 控制器
data[method] | delete | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id_array][] | 33 | String | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"CBA88AF7-5B29-2735-6C3B-0B2E955A349B",
		"CBE183E2-0C8C-E2CE-4805-0E570AB279C3",
		"A529579A-1EA4-C97E-3354-C42BEC71B011",
		"B1E7DEA8-47DC-998F-E2C3-34A177BCBDED",
		"55439681-536F-C357-0936-86825661F7D9"
	]
}
```
## /cgtw7.0/filebox
```text
文件框数据
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/filebox/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | filebox | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"pipeline_id",
		"folder_id",
		"module",
		"module_type",
		"classify",
		"title",
		"sign",
		"create_by",
		"create_time",
		"last_update_by",
		"last_update_time"
	]
}
```
## /cgtw7.0/filebox/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | filebox | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | info | String | 是 | 模块类型
data[field_array][] | title | Array | 是 | 字段标识列表
data[pipeline_id_array][] | all | Array | 是 | 阶段ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"title": "Layout",
			"#id": "231C7651-0DA9-FC63-5018-A0B84B24AE9C",
			"is_extend": ""
		},
		{
			"title": "images",
			"#id": "C4E59450-25C9-4FC7-454A-70F6D82AA37F",
			"is_extend": ""
		},
		{
			"title": "approve",
			"#id": "78FB712E-6F28-E710-0200-244E6C5068CB",
			"is_extend": ""
		},
		{
			"title": "素材路径",
			"#id": "44857647-C6C3-A5FD-A645-62FCF6FE054E",
			"is_extend": ""
		},
		{
			"title": "folder",
			"#id": "9359E86F-68A7-E73E-FEF3-9ABC12C734FF",
			"is_extend": ""
		}
	]
}
```
## /cgtw7.0/filebox/check_all_pipeline_finish
```text
检查阶段是否完成
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | filebox | String | 是 | 控制器
data[method] | check_all_pipeline_finish | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[task_id] | B006E913-4B83-C465-D2A5-6A38D087F243 | String | 是 | 任务ID
data[pipeline_id_array][] | 3429200E-6801-4FD8-A742-8F2767674FB2 | String | 是 | 阶段ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "0",
	"type": "msg",
	"data": "阶段未完成: (Layout); \n[project_filebox::check_all_pipeline_finish]"
}
```
## /cgtw7.0/field
```text
字段数据
主界面-字段选择
项目设置-模块管理-模块-字段设置
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/field/type
```text
获取字段的所有类型
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | field | String | 是 | 控制器
data[method] | type | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"int",
		"decimal",
		"lineedit",
		"textedit",
		"checkbox",
		"list"
	]
}
```
## /cgtw7.0/field/get_filter
```text
获取字段列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | field | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[field_array][] | sign | Array | 是 | 字段标识列表
data[filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"sign": "shot.sc"
		},
		{
			"sign": "shot.last_update_time"
		},
		{
			"sign": "shot.last_update_by"
		},
		{
			"sign": "shot.create_time"
		},
		{
			"sign": "shot.create_by"
		},
		{
			"sign": "shot.id"
		},
		{
			"sign": "shot.shot_date_field"
		},
		{
			"sign": "shot.list"
		},
		{
			"sign": "shot.shot"
		},
		{
			"sign": "shot.entity"
		}
	]
}
```
## /cgtw7.0/field/count
```text
统计记录条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | field | String | 是 | 控制器
data[method] | count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "69"
}
```
## /cgtw7.0/field/create
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | field | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[chinese_name] | test_create | String | 是 | 中文名
data[english_name] | test_create | String | 是 | 英文名
data[sign] | test_create | String | 是 | 字段标识
data[type] | lineedit | String | 是 | 字段类型
data[field_name] | - | String | 否 | 字段名, 默认为"",为空时,默认和sign一样
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[module_type] | info | String | 是 | 模块类型
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/folder
```text
目录标识结构数据
项目设置-项目模板-目录&文件框
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/folder/get_sign
```text
获取目录结构标识数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | folder | String | 是 | 控制器
data[method] | get_sign | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"sign": "11",
			"path": "z:/11"
		},
		{
			"sign": "mod_check",
			"path": "a:/xiaoying/Asset/{asset_type.entity}/{asset.entity}/Mod/check"
		},
		{
			"sign": "mod_work",
			"path": "a:/xiaoying/Asset/{asset_type.entity}/{asset.entity}/Mod/work"
		},
		{
			"sign": "shot",
			"path": "a:/xiaoying/Shot"
		},
		{
			"sign": "lay_check",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/check"
		},
		{
			"sign": "lay_work",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/work"
		},
		{
			"sign": "lay_approve",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/approve"
		},
		{
			"sign": "same_ver",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/same_ver"
		},
		{
			"sign": "same_ver1",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/same_ver/same_ver1"
		},
		{
			"sign": "same_ver2",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/same_ver/same_ver2"
		},
		{
			"sign": "folder_ver",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/{ver}/folder_ver"
		},
		{
			"sign": "follow_ver",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/follow_ver"
		},
		{
			"sign": "follow_ver1",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/follow_ver/follow_ver1"
		},
		{
			"sign": "follow_ver2",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/follow_ver/follow_ver2"
		},
		{
			"sign": "file_ver1",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/file_version/file_ver1"
		},
		{
			"sign": "folder_ver1",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/folder_ver/{ver}/folder_ver1"
		},
		{
			"sign": "folder_ver2",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/folder_ver/{ver}/folder_ver2"
		},
		{
			"sign": "upgrade_file",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/upgrade_file"
		},
		{
			"sign": "source",
			"path": "a:/xiaoying/Shot/Source/{eps.entity}/{shot.entity}"
		},
		{
			"sign": "shot_task_check",
			"path": "a:/xiaoying/Shot/{task.entity}/{shot.entity}/lllcheck"
		},
		{
			"sign": "date",
			"path": "a:/xiaoying/{today_ymd}"
		},
		{
			"sign": "ref_1",
			"path": "a:/ref_1"
		},
		{
			"sign": "file_ver",
			"path": "a:/file_ver"
		}
	]
}
```
## /cgtw7.0/folder/get_path
```text
获取目录id获取路径
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | folder | String | 是 | 控制器
data[method] | get_path | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[os] | win | String | 是 | 系统平台
data[id] | - | String | 是 | ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"sign": "11",
			"path": "z:/11"
		},
		{
			"sign": "mod_check",
			"path": "a:/xiaoying/Asset/{asset_type.entity}/{asset.entity}/Mod/check"
		},
		{
			"sign": "mod_work",
			"path": "a:/xiaoying/Asset/{asset_type.entity}/{asset.entity}/Mod/work"
		},
		{
			"sign": "shot",
			"path": "a:/xiaoying/Shot"
		},
		{
			"sign": "lay_check",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/check"
		},
		{
			"sign": "lay_work",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/work"
		},
		{
			"sign": "lay_approve",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/approve"
		},
		{
			"sign": "same_ver",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/same_ver"
		},
		{
			"sign": "same_ver1",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/same_ver/same_ver1"
		},
		{
			"sign": "same_ver2",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/same_ver/same_ver2"
		},
		{
			"sign": "folder_ver",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/{ver}/folder_ver"
		},
		{
			"sign": "follow_ver",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/follow_ver"
		},
		{
			"sign": "follow_ver1",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/follow_ver/follow_ver1"
		},
		{
			"sign": "follow_ver2",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/follow_ver/follow_ver2"
		},
		{
			"sign": "file_ver1",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/file_version/file_ver1"
		},
		{
			"sign": "folder_ver1",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/folder_ver/{ver}/folder_ver1"
		},
		{
			"sign": "folder_ver2",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/folder_ver/{ver}/folder_ver2"
		},
		{
			"sign": "upgrade_file",
			"path": "a:/xiaoying/Shot/Layout/{eps.entity}/{shot.entity}/upgrade_file"
		},
		{
			"sign": "source",
			"path": "a:/xiaoying/Shot/Source/{eps.entity}/{shot.entity}"
		},
		{
			"sign": "shot_task_check",
			"path": "a:/xiaoying/Shot/{task.entity}/{shot.entity}/lllcheck"
		},
		{
			"sign": "date",
			"path": "a:/xiaoying/{today_ymd}"
		},
		{
			"sign": "ref_1",
			"path": "a:/ref_1"
		},
		{
			"sign": "file_ver",
			"path": "a:/file_ver"
		}
	]
}
```
## /cgtw7.0/plugin
```text
系统设置-插件管理
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/plugin/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | plugin | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"name",
		"type",
		"argv",
		"create_by",
		"create_time",
		"last_update_time",
		"last_update_by"
	]
}
```
## /cgtw7.0/plugin/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | plugin | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"67270827-7B82-7700-AF57-1B4BB56D71EB",
		"73B51C31-39B2-C98E-BD3F-44B3E13346C1"
	]
}
```
## /cgtw7.0/plugin/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | plugin | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[filter_array] | - | Array | 否 | 过滤语句列表
data[field_array][] | name | Array | 是 | 字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"name": "jump_link",
			"#id": "67270827-7B82-7700-AF57-1B4BB56D71EB"
		}
	]
}
```
## /cgtw7.0/plugin/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | plugin | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[id_array][0] | 67270827-7B82-7700-AF57-1B4BB56D71EB | Array | 是 | ID列表
data[field_array][] | type | Array | 是 | 字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"type": "menu",
			"#id": "67270827-7B82-7700-AF57-1B4BB56D71EB"
		}
	]
}
```
## /cgtw7.0/plugin/get_argvs
```text
获取指定插件所有的参数字典
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | plugin | String | 是 | 控制器
data[method] | get_argvs | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[id] | 67270827-7B82-7700-AF57-1B4BB56D71EB | String | 是 | 插件ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"type": "ee"
	}
}
```
## /cgtw7.0/plugin/set_argvs
```text
设置插件参数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | plugin | String | 是 | 控制器
data[method] | set_argvs | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[id] | 67270827-7B82-7700-AF57-1B4BB56D71EB | String | 是 | 插件ID
data[argv_data][type] | ee | Array | 是 | 更新参数 (dict), 格式{'key':'value'}
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/pipeline
```text
阶段数据
模块管理-项目模块-选择模块-阶段设置
项目设置-项目模板-模块&阶段
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/pipeline/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"entity",
		"module",
		"module_type",
		"description",
		"create_by",
		"create_time",
		"last_update_time",
		"last_update_by"
	]
}
```
## /cgtw7.0/pipeline/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"27337D30-72E2-2563-9AFB-9FA73D6A9784",
		"DCF9F3B2-6234-2ACB-0609-A8A854EA3EEE",
		"01EBA3C2-DAA3-8403-AC29-8038B6DD74C0",
		"17C4BD79-4BF0-B8E4-05B8-D00E3191B092",
		"93BB8422-8B31-49CC-B558-B8419DE2D50B",
		"65399223-CC65-9235-8A6F-C75C945ED16B",
		"217BCAE2-EECC-0FD1-19DB-5704B2FD0F3B",
		"3429200E-6801-4FD8-A742-8F2767674FB2",
		"01F99FCE-3407-E541-E14C-DE4BD9D17AB7",
		"EB7F1215-9C95-5F81-502D-BDCBB9A57987",
		"18AD4BB0-5C93-FDC8-790A-023435B9D507",
		"475A1477-22EE-BCCF-E49B-5BB76BD52E87",
		"B603D209-659A-358F-DB78-6A04B9D70C32",
		"1F046927-7C99-D3DC-3909-C797A736FB08"
	]
}
```
## /cgtw7.0/pipeline/get_filter
```text
获取记录列表

缩写:abridge
名称:entity
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
data[field_array][] | abridge | Array | 是 | 字段标识列表
data[field_array][] | entity | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "Design",
			"#id": "27337D30-72E2-2563-9AFB-9FA73D6A9784"
		},
		{
			"entity": "Mod",
			"#id": "DCF9F3B2-6234-2ACB-0609-A8A854EA3EEE"
		},
		{
			"entity": "Texture",
			"#id": "01EBA3C2-DAA3-8403-AC29-8038B6DD74C0"
		},
		{
			"entity": "Rig",
			"#id": "17C4BD79-4BF0-B8E4-05B8-D00E3191B092"
		},
		{
			"entity": "Face",
			"#id": "93BB8422-8B31-49CC-B558-B8419DE2D50B"
		},
		{
			"entity": "剧本",
			"#id": "65399223-CC65-9235-8A6F-C75C945ED16B"
		},
		{
			"entity": "分镜",
			"#id": "217BCAE2-EECC-0FD1-19DB-5704B2FD0F3B"
		},
		{
			"entity": "Layout",
			"#id": "3429200E-6801-4FD8-A742-8F2767674FB2"
		},
		{
			"entity": "Animation",
			"#id": "01F99FCE-3407-E541-E14C-DE4BD9D17AB7"
		},
		{
			"entity": "Lighting",
			"#id": "EB7F1215-9C95-5F81-502D-BDCBB9A57987"
		},
		{
			"entity": "VFX",
			"#id": "18AD4BB0-5C93-FDC8-790A-023435B9D507"
		},
		{
			"entity": "Comp",
			"#id": "475A1477-22EE-BCCF-E49B-5BB76BD52E87"
		}
	]
}
```
## /cgtw7.0/pipeline/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id_array][0] | 27337D30-72E2-2563-9AFB-9FA73D6A9784 | Array | 是 | 过滤语句列表
data[field_array][] | entity | Array | 是 | 字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "Design",
			"#id": "27337D30-72E2-2563-9AFB-9FA73D6A9784"
		}
	]
}
```
## /cgtw7.0/history
```text
查看方式:记录-右侧面板-历史记录
启用:项目设置-模块管理-选择模块-模块配置-历史记录
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/history/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | history | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"account_id",
		"link_entity",
		"#id",
		"create_by",
		"#link_id",
		"last_update_time",
		"last_update_by",
		"note_id",
		"file",
		"status",
		"time",
		"text",
		"module",
		"module_type",
		"status_type",
		"step",
		"create_time"
	]
}
```
## /cgtw7.0/history/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | history | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | Array | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"6060344B-E3C2-657C-1B8D-567AF29F921C",
		"996E088F-91D4-3D92-C01E-83DC079CB5BD",
		"994FF143-F082-5EF8-076A-B3763FE39BB6",
		"D9724FCB-D3DF-D245-55D6-CEDC6670092C",
		"8C6E56C6-7CEB-52FE-0472-986EB6ACB317"
	]
}
```
## /cgtw7.0/history/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | history | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id_array][] | 6060344B-E3C2-657C-1B8D-567AF29F921C | Array | 是 | ID列表
data[field_array][] | link_entity | Array | 是 | 字段列表
data[order_field_array][] | - | Array | 否 | 排序列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"link_entity": "ep001/sc001/Layout",
			"#id": "6060344B-E3C2-657C-1B8D-567AF29F921C"
		}
	]
}
```
## /cgtw7.0/history/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | history | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array] | - | String | 否 | 过滤语句列表
data[field_array][] | link_entity | Array | 是 | 字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[order_field_array] | - | Array | 否 | 顺序的字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"link_entity": "ep001/sc001/Layout",
			"#id": "6060344B-E3C2-657C-1B8D-567AF29F921C"
		},
		{
			"link_entity": "ep001/sc001/Animation",
			"#id": "996E088F-91D4-3D92-C01E-83DC079CB5BD"
		},
		{
			"link_entity": "ep001/sc002/Layout",
			"#id": "994FF143-F082-5EF8-076A-B3763FE39BB6"
		},
		{
			"link_entity": "ep001/sc002/Animation",
			"#id": "D9724FCB-D3DF-D245-55D6-CEDC6670092C"
		},
		{
			"link_entity": "ep001/sc003/Layout",
			"#id": "8C6E56C6-7CEB-52FE-0472-986EB6ACB317"
		}
	]
}
```
## /cgtw7.0/history/count
```text
统计记录条数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | history | String | 是 | 控制器
data[method] | count | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "49827"
}
```
## /cgtw7.0/link
```text
查看方式:记录-右侧面板-关联信息
启用:项目设置-模块管理-选择模块-模块配置-关联信息
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/link/link_entity
```text
关联模块记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | link | String | 是 | 控制器
data[method] | link_entity | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[id_array][] | 16D442F6-A17D-C445-2E6C-14C852053DD1 | Array | 是 | ID列表
data[link_module] | asset | String | 是 | link模块标识
data[link_id_array][] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | Array | 是 | 关联ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/link/link_entity_num
```text
添加关联模块的引用次数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | link | String | 是 | 控制器
data[method] | link_entity_num | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[id_array][] | 16D442F6-A17D-C445-2E6C-14C852053DD1 | Array | 是 | ID列表
data[link_module] | asset | String | 是 | link模块标识
data[link_data][849D6CD8-7D37-B37B-492A-91C3726A0717] | 2 | Array | 是 | 资产ID字典 (dict),如{asset_id: num}
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/link/unlink_entity
```text
取消关联模块的记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | link | String | 是 | 控制器
data[method] | unlink_entity | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[id_array][] | 16D442F6-A17D-C445-2E6C-14C852053DD1 | Array | 是 | ID列表
data[link_module] | asset | String | 是 | link模块标识
data[link_id_array][] | 849D6CD8-7D37-B37B-492A-91C3726A0717 | Array | 是 | 资产ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/link/get_entity
```text
获取关联模块的id和引用次数的字典
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | link | String | 是 | 控制器
data[method] | get_entity | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[id] | 16D442F6-A17D-C445-2E6C-14C852053DD1 | String | 是 | ID
data[link_module] | asset | String | 是 | link模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"849D6CD8-7D37-B37B-492A-91C3726A0717": "2"
	}
}
```
## /cgtw7.0/link/reset_link_num
```text
重置关联资产的引用次数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | link | String | 是 | 控制器
data[method] | reset_link_num | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[id_array][] | 16D442F6-A17D-C445-2E6C-14C852053DD1 | Array | 是 | 任务ID列表
data[link_module] | asset | String | 是 | link模块标识
data[link_data][849D6CD8-7D37-B37B-492A-91C3726A0717] | 3 | Array | 是 | 资产ID字典 (dict),如{asset_id: num}
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/link/get_more_link
```text
获取记录关联数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | link | String | 是 | 控制器
data[method] | get_more_link | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[id_array][] | 4B957344-0908-86A1-E235-A32E2FC7A1BD | String | 是 | ID
data[link_module] | asset | String | 是 | link模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"0ABB0965-9F79-E003-2E39-A7EB5904BB42": {
			"849D6CD8-7D37-B37B-492A-91C3726A0717": "1",
			"3ADACCAA-4652-03BE-D9AB-043FCE8CD735": "1",
			"B390809D-09F0-04AD-1BA3-F8E80939AA20": "1",
			"A58016E1-5E0D-3A2D-6C18-0EC1E6494B14": "1"
		}
	}
}
```
## /cgtw7.0/software
```text
应用中心-工具
系统设置-启动器管理
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/software/types
```text
获取软件类型
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | software | String | 是 | 控制器
data[method] | types | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"3dmax",
		"Blender",
		"hiero",
		"houdini",
		"maya",
		"nuke",
		"rv",
		"Unreal"
	]
}
```
## /cgtw7.0/software/get_path
```text
获取软件路径
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | software | String | 是 | 控制器
data[method] | get_path | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[name] | nuke13 | String | 是 | 软件名称
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "A:\\software\\nuke\\Nuke13.0v1/Nuke13.0.exe"
}
```
## /cgtw7.0/software/get_with_type
```text
根据类型获取软件信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | software | String | 是 | 控制器
data[method] | get_with_type | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[type] | nuke | String | 是 | 软件类型
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "C:/software/Nuke13.0v1/Nuke13.0.exe"
}
```
## /cgtw7.0/api_data
```text
项目自定义数据
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/api_data/get
```text
获取项目自定义数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | api_data | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[key] | aa | String | 是 | 键
data[is_user] | false | Boolean | 是 | 是否为个人 (bool)
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "123456"
}
```
## /cgtw7.0/api_data/set
```text
设置项目自定义数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | api_data | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[key] | aa | String | 是 | 键
data[value] | 123456 | String | 是 | 值
data[is_user] | - | Boolean | 是 | 是否为个人 (bool)
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/link_entity
```text
实体数据
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/link_entity/get_entity
```text
获取关联的实体名称
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | link_entity | String | 是 | 控制器
data[method] | get_entity | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[link_id] | 16D442F6-A17D-C445-2E6C-14C852053DD1 | String | 是 | 任务ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "ep001/sc002/Layout"
}
```
## /cgtw7.0/link_entity/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | link_entity | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[filter_entity] | ep001/sc001 | String | 是 | 查找的实体
data[is_mytask] | - | Boolean | 否 | 是否查找我的任务
data[limit] | 0 | String | 是 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"2ACDCC36-A3EA-0410-5BFC-24DCC8DFE746": "ep001/sc001/Animation",
		"31171194-E0A3-F0C5-FC51-B6F6EFCF7910": "ep001/sc001/Lighting",
		"5C1B6B4D-7320-9383-2E78-242A1584D453": "ep001/sc001/Comp",
		"4B957344-0908-86A1-E235-A32E2FC7A1BD": "ep001/sc001/Layout"
	}
}
```
## /cgtw7.0/link_entity/get_entity_array
```text
获取关联的实体名称
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | link_entity | String | 是 | 控制器
data[method] | get_entity_array | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[link_id_array][] | 16D442F6-A17D-C445-2E6C-14C852053DD1 | String | 是 | 任务ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"16D442F6-A17D-C445-2E6C-14C852053DD1": "test_rv/sc002/Layout"
	}
}
```
## /cgtw7.0/timelog
```text
应用中心-工时
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/timelog/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | timelog | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"#link_id",
		"module",
		"module_type",
		"use_time",
		"date",
		"text",
		"create_by",
		"create_time",
		"last_update_by",
		"last_update_time"
	]
}
```
## /cgtw7.0/timelog/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | timelog | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array][0][0] | link_id | Array | 否 | 过滤语句列表
data[limit] | 5 | String | 否 | 限制条数,默认5000
data[filter_array][0][1] | = | String | 是 | -
data[filter_array][0][2] | B006E913-4B83-C465-D2A5-6A38D087F243 | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"1C48D9B7-85B0-8C0C-A31C-5B5A6C382FA2",
		"08DFDA7B-E8E1-C7DF-AD42-B40E9E2B8976",
		"A5CD4874-FFC6-532E-CD83-AC03B00DF7B1",
		"2987EF32-033B-EB1C-C4F0-B22458A2A4AA",
		"222B3FE9-1E3F-65BC-6F30-9CDAFBB184C5"
	]
}
```
## /cgtw7.0/timelog/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | timelog | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id_array][] | FDF151CB-EE47-04B0-7E99-44BCE7A3FB56 | Array | 是 | ID列表
data[field_array][] | account_id | Array | 是 | 字段列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[order_field_array][] | id | Array | 否 | 排序列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"use_time": "05:05",
			"#id": "1C48D9B7-85B0-8C0C-A31C-5B5A6C382FA2"
		}
	]
}
```
## /cgtw7.0/timelog/create
```text
创建记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | timelog | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[link_id] | 16D442F6-A17D-C445-2E6C-14C852053DD1 | String | 是 | 任务ID
data[use_time] | 02:30 | String | 是 | 用时, 格式:时:分,例 02:30
data[date] | 2022-02-02 | String | 是 | 日期
data[text] | 11 | String | 是 | 内容
data[tag] | - | String | 否 | 标签
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "6052C991-795D-70FF-51A7-5D6AACB5433F"
}
```
## /cgtw7.0/timelog/set
```text
更新单条记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | timelog | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id] | 1C48D9B7-85B0-8C0C-A31C-5B5A6C382FA2 | String | 是 | ID
data[field_data_array][use_time] | 05:05 | Array | 是 | 更新的数据 (dict)
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/flow
```text
审核流程
查看/设置方式:项目设置-审核流程
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/flow/get_data
```text
获取审核流程记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | flow | String | 是 | 控制器
data[method] | get_data | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[pipeline_id_array][] | 3429200E-6801-4FD8-A742-8F2767674FB2 | Array | 是 | 阶段ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"flow_name": "Layout",
			"pipeline_id": "3429200E-6801-4FD8-A742-8F2767674FB2",
			"pipeline_name": "Layout"
		}
	]
}
```
## /cgtw7.0/flow/get_node
```text
获取审核节点数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | flow | String | 是 | 控制器
data[method] | get_node | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[flow_id] | 672A349D-A765-FBFB-CC5E-06C8A06B2B79 | String | 是 | 流程ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"field_sign": "task.leader_status",
			"qc_account_id": "B8B95A85-36E8-B6FB-DB78-301A358C77F3,F2E31BCA-63C9-55A2-3D24-5FF65CC5C20F,A98C9570-F63D-84A5-1620-3EA8CB13D87E",
			"status_list": [
				{
					"name": "Approve",
					"type": "approve"
				},
				{
					"name": "Retake",
					"type": "retake"
				},
				{
					"name": "Pause",
					"type": "pause"
				},
				{
					"name": "Revert",
					"type": "revert"
				}
			]
		},
		{
			"field_sign": "task.director_status",
			"qc_account_id": "73825608-A6F7-CBEC-C8F1-2C0825330EE9,C84FF25F-D83F-CC64-E992-5D41ED1DCDFE,EE93BE0D-6DC5-19EF-BE72-E5CECD8386D6",
			"status_list": [
				{
					"name": "Retake",
					"type": "retake"
				},
				{
					"name": "Approve",
					"type": "approve"
				}
			]
		},
		{
			"field_sign": "task.client_status",
			"qc_account_id": "912E47F0-7A27-6970-5DCA-E41EDB33BF72,76ae9e2f-7067-409a-9319-f538c68dcde4,0502AD9B-5A38-B9AB-7E39-00F7C0B9B3A0",
			"status_list": [
				{
					"name": "Approve",
					"type": "approve"
				},
				{
					"name": "Retake",
					"type": "retake"
				}
			]
		},
		{
			"field_sign": "task.file_status",
			"qc_account_id": "B8B95A85-36E8-B6FB-DB78-301A358C77F3",
			"status_list": [
				{
					"name": "Approve",
					"type": "approve"
				},
				{
					"name": "Retake",
					"type": "retake"
				}
			]
		}
	]
}
```
## /cgtw7.0/flow/get_field_sign_array
```text
根据阶段名称获取审核字段
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | flow | String | 是 | 控制器
data[method] | get_field_sign_array | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[pipeline_name_array][] | Layout | Array | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"task.file_status": "工程审核",
		"task.director_status": "导演审核",
		"task.client_status": "客户审核",
		"task.leader_status": "内部审核"
	}
}
```
## /cgtw7.0/server
```text
服务器设置
项目服务器设置(项目设置-文件盘符设置/项目设置-项目模板-项目-目录&文件框-选择服务器)
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/server/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | server | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"name",
		"win_path",
		"mac_path",
		"linux_path"
	]
}
```
## /cgtw7.0/server/get
```text
获取信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | server | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[field_array][] | name | Array | 是 | 字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"name": "(共享盘)文件服务器",
			"#id": "271E10CC-A6BA-F359-073F-FBC355198353"
		}
	]
}
```
## /cgtw7.0/server/get_path
```text
获取指定软件路径
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | server | String | 是 | 控制器
data[method] | get_path | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id] | 271E10CC-A6BA-F359-073F-FBC355198353 | String | 是 | ID
data[os] | win | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "a:/"
}
```
## /cgtw7.0/version
```text
版本数据
项目设置-模块管理-版本
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/version/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | version | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"create_time",
		"last_update_time",
		"#id",
		"create_by",
		"last_update_by",
		"description",
		"link_entity",
		"sign",
		"#link_id",
		"status",
		"entity",
		"module",
		"module_type",
		"aa",
		"ee"
	]
}
```
## /cgtw7.0/version/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | version | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"1DA5DBC2-728B-EE08-7038-52E8E8470F64",
		"9D20F162-E8FC-3758-119F-68ECFA86C2FA",
		"04110525-EDAC-409F-F5A6-C9A09E5F7C13",
		"62DD5CA0-0A58-3B42-DB81-FF4E9A59EACC",
		"181EBC79-D282-61D7-A605-E16A7E88BC3E"
	]
}
```
## /cgtw7.0/version/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | version | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[id_array][] | 1DA5DBC2-728B-EE08-7038-52E8E8470F64 | Array | 是 | ID列表
data[field_array][] | entity | Array | 是 | 字段列表
data[order_field_array][] | - | Array | 否 | 顺序的字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "001",
			"#id": "1DA5DBC2-728B-EE08-7038-52E8E8470F64"
		}
	]
}
```
## /cgtw7.0/version/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | version | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[field_array][] | entity | Array | 是 | 字段列表
data[order_field_array][] | - | Array | 否 | 顺序的字段标识列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "001",
			"#id": "9D20F162-E8FC-3758-119F-68ECFA86C2FA"
		},
		{
			"entity": "002",
			"#id": "04110525-EDAC-409F-F5A6-C9A09E5F7C13"
		},
		{
			"entity": "003",
			"#id": "62DD5CA0-0A58-3B42-DB81-FF4E9A59EACC"
		},
		{
			"entity": "009",
			"#id": "181EBC79-D282-61D7-A605-E16A7E88BC3E"
		},
		{
			"entity": "001",
			"#id": "1DA5DBC2-728B-EE08-7038-52E8E8470F64"
		}
	]
}
```
## /cgtw7.0/version/create
```text
创建记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | version | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[link_id] | 267FE899-F915-D76A-DC75-8F400D320DF9 | String | 是 | 任务ID
data[sign] | review | String | 是 | 文件框标识
data[field_data_array] | - | Array | 否 | 额外的数据 (dict), 格式:{key: value}
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "AD123CB4-743C-F37F-1CD3-28B79FE312DF"
}
```
## /cgtw7.0/version/delete
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | version | String | 是 | 控制器
data[method] | delete | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[id_array][] | AD123CB4-7431-F37F-1CD3-28B79FE312DF | Array | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/version/set
```text
修改字段
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | version | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id] | F71FF71C-CA6F-3ABA-A34E-5865D71FF937 | Array | 是 | ID列表
data[field_data_array][aa] | 11 | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/file
```text
提交记录表
项目设置-模块管理-提交记录
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/file/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | file | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"link_entity",
		"sys_last_update_by",
		"sys_local_full_path",
		"#module",
		"#module_type",
		"#server_id",
		"sys_create_by",
		"sys_create_time",
		"sys_last_update_time",
		"#version_id",
		"sys_modify_time",
		"#file_name",
		"#is_online",
		"sys_size",
		"#id",
		"#link_id"
	]
}
```
## /cgtw7.0/file/create
```text
创建记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | file | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型(info、task)
data[link_id] | 5F376C61-750F-6462-45FF-14EB31F781CB | String | 是 | 任务ID
data[version_id] | AD123CB4-743C-F37F-1CD3-28B79FE312DF | String | 是 | 版本ID
data[os] | win | String | 是 | 系统平台
data[file_data_array][0][path] | z:/project/shot/sc001.mp4 | Array | 是 | 文件路径
data[file_data_array][0][size] | 1000 | Array | 是 | 文件大小
data[file_data_array][0][modify_time] | 2022-02-02 02:02:02 | Array | 是 | 文件修改时间
data[meta_data_array] | - | String | 否 | 自定义的数据 (dict), 格式:{key: value}
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"path": "z:/project/shot/sc001.mp4",
			"online": "/project/shot/sc001.mp4",
			"id": "B91252E6-691C-2695-C875-5FEFCF17E9B4"
		}
	]
}
```
## /cgtw7.0/file/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | file | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"5D6633D4-8D3A-73CC-00F1-2120337206DE",
		"75012DBE-1F20-C019-4A21-2FE1541CCE5B",
		"EA670970-D65D-E0CE-E5CD-39622AF67A41",
		"6F1E2430-708E-EE4F-0C2B-520EECAFFAA2",
		"4FB68698-B1D8-A2EC-87D6-5F2D8043C34F"
	]
}
```
## /cgtw7.0/file/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | file | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[field_array][] | sys_size | Array | 是 | 字段标识列表
data[id_array][] | 5D6633D4-8D3A-73CC-00F1-2120337206DE | Array | 是 | ID列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[order_field_array] | - | Array | 否 | 排序列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"sys_size": "1043911",
			"#id": "5D6633D4-8D3A-73CC-00F1-2120337206DE"
		}
	]
}
```
## /cgtw7.0/file/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | file | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[field_array][] | sys_size | Array | 是 | 字段标识列表
data[id_array][] | 5D6633D4-8D3A-73CC-00F1-2120337206DE | Array | 是 | ID列表
data[filter_array] | - | Array | 否 | 过滤语句列表
data[order_field_array] | - | Array | 否 | 排序列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"sys_size": "774642",
			"#id": "EA670970-D65D-E0CE-E5CD-39622AF67A41"
		},
		{
			"sys_size": "34788959",
			"#id": "6F1E2430-708E-EE4F-0C2B-520EECAFFAA2"
		},
		{
			"sys_size": "1153",
			"#id": "4FB68698-B1D8-A2EC-87D6-5F2D8043C34F"
		},
		{
			"sys_size": "10032434",
			"#id": "B35E8DD4-D4A0-8D3D-BF89-79407C603B8F"
		},
		{
			"sys_size": "942668",
			"#id": "F019784C-3081-C1D9-3408-253730E968E6"
		}
	]
}
```
## /cgtw7.0/file/delete
```text
删除记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | file | String | 是 | 控制器
data[method] | delete | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id_array][] | 5D6623D4-8D3A-73CC-00F1-2120337206DE | Array | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/file/get_filebox_version_file
```text
获取版本文件框的提交文件数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | file | String | 是 | 控制器
data[method] | get_filebox_version_file | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[task_id] | {{task_asset_id}} | String | 是 | 任务ID
data[filebox_id] | {{task_asset_filebox_id}} | String | 是 | 文件框ID
data[os] | mac | String | 是 | 系统平台
data[is_all] | N | String | 是 | 是否所有 Y/N/L
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"/tmp/xiaoying/Asset/Chars/cat001/Design/file_ver/cat001_003.tga"
	]
}
```
## /cgtw7.0/file/get_info
```text
获取网盘文件信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | file | String | 是 | 控制器
data[method] | get_info | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[online_dir] | /xiaoying/Asset/Chars/cat001/Design/file_ver/ | String | 是 | 网盘目录
data[file_name_array][] | cat001_003.tga | Array | 是 | 文件名列表
data[folder_name_array][] | - | Array | 是 | 目录名列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"cat001_003.tga": {
			"time": "2020-04-27 13:09:34",
			"size": "388771"
		}
	}
}
```
## /cgtw7.0/file/get_version_file
```text
根据版本id获取版本文件
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | file | String | 是 | 控制器
data[method] | get_version_file | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[version_id_array][] | AD123CB4-743C-F37F-1CD3-28B79FE312DF | Array | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"path": "/project/shot/sc001.mp4",
			"size": "1000",
			"time": "2022-02-02 02:02:02",
			"id": "B91252E6-691C-2695-C875-5FEFCF17E9B4"
		}
	]
}
```
## /cgtw7.0/file/get_publish_json_data
```text
根据文件提交数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | file | String | 是 | 控制器
data[method] | get_publish_json_data | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id_array][] | B91252E6-691C-2695-C875-5FEFCF17E9B4 | Array | 是 | File ID列表
data[folder_id_array][] | - | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"sc001.mp4": {
			"time": "2022-02-02 02:02:02",
			"is_file": "Y",
			"size": "1000",
			"ver": "015"
		}
	}
}
```
## /cgtw7.0/msg_queue
```text
创建消息队列任务, 一般和任务处理脚本配合使用
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/msg_queue/create
```text
创建消息队列任务, 一般和任务处理脚本配合使用
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | msg_queue | String | 是 | 控制器
data[method] | add | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[app_key] | render1 | String | 是 | 程序标识
data[argv][task_name] | render | Array | 是 | 任务的数据(dict), 格式:{key: value}
data[timeout] | - | Integer | 否 | 超时时长, (int)单位为秒
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/msg_queue/get_task_data
```text
取队列列表中的数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | msg_queue | String | 是 | 控制器
data[method] | get_task_data | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[app_key] | render1 | String | 是 | 程序标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/log
```text
日志
获取项目日志时,参数db填项目数据库
获取系统日志时,参数db填public
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/log/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | log | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"#timecode",
		"type",
		"module",
		"module_type",
		"entity",
		"event",
		"user",
		"time"
	]
}
```
## /cgtw7.0/log/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | log | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("log_id", response.json.data[0]);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"7B5EB2B5-0407-9615-F4C7-551AA16A4AC6",
		"79DDE361-3F2F-65D5-E32D-AB4CC42D10F4",
		"16DE8858-E830-104E-E3B2-B86C4C19E380",
		"3931FCEA-EC5E-A8B0-5B24-7FA0C66CA682",
		"8F21AB8E-EF36-6BEE-F573-3A7B12547435",
		"8FC7EAFC-3577-A475-D59D-B1A1D8D67023",
		"1D647BB4-DF02-8619-2705-80ECF35859E5",
		"C12482BE-1FDC-1485-CE6C-19CD3A7DD012",
		"E7B3DF6E-CCCB-A898-84B4-5F8F468F8473",
		"80F6BF87-F735-8259-E719-AC47C19DE0AB",
		"07348913-242B-0D05-4D46-5CAF2B1B018C",
		"0BF52E5A-C37E-F1E9-8562-ABBD29762795",
		"760947B4-3C72-6E59-B663-B44883F5B24D",
		"AF0F379A-35DD-432F-AEF6-211814C49A8B",
		"FFCA1F81-A24F-180D-A396-A271B057D61F",
		"3ECB07F7-A657-747B-FA88-0BF632B30BE7",
		"2ED231EC-53BB-A4C3-6876-D25E3CACB8A2",
		"01947FE4-142A-182C-DA1F-D5530FF25DC8",
		"CA6D70FE-15CB-D457-5767-C1CFD9CE737C",
		"3EB644FD-33A5-BDC1-3765-FAD54C22B1AC",
		"5F8F7BA1-2884-9868-03AD-8A971C2E6568",
		"D408BFDE-56F4-D7C2-0FBC-207779F7E4EA",
		"25FF5C4B-C313-BBA2-4F6E-85792B95508C",
		"90D0F6CD-BB35-D707-9792-03A7820CFC7E",
		"D26900D7-993B-BDBA-17B6-76ED39473CA9",
		"CF9C8E95-5C94-C703-D8F1-5635E4941BCE",
		"99FB6B61-6923-CF7A-C9EC-2C73D5B9C271",
		"F45D2738-9A2A-665C-EF20-A99B4D05388C",
		"064706E7-DF5D-0DE5-1EAF-402DDDD309C8",
		"3B11203F-C323-1437-DFD7-26301C79DE00"
	]
}
```
## /cgtw7.0/log/get_filter
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | log | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[field_array][] | entity | Array | 是 | 字段标识列表
data[filter_array] | - | Array | 否 | 过滤语句列表
data[limit] | - | String | 否 | 限制条数,默认5000
data[order_field_array] | - | Array | 否 | 顺序的字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("log_id", response.json.data[0]);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "eps001/seq001/sc001",
			"#id": "7B5EB2B5-0407-9615-F4C7-551AA16A4AC6"
		},
		{
			"entity": "eps001/seq001/sc002",
			"#id": "79DDE361-3F2F-65D5-E32D-AB4CC42D10F4"
		},
		{
			"entity": "eps001/seq001/sc003",
			"#id": "16DE8858-E830-104E-E3B2-B86C4C19E380"
		},
		{
			"entity": "eps001/seq001/sc004",
			"#id": "3931FCEA-EC5E-A8B0-5B24-7FA0C66CA682"
		},
		{
			"entity": "eps001/seq001/sc005",
			"#id": "8F21AB8E-EF36-6BEE-F573-3A7B12547435"
		},
		{
			"entity": "eps001/seq001/sc006",
			"#id": "8FC7EAFC-3577-A475-D59D-B1A1D8D67023"
		},
		{
			"entity": "eps001/seq001/sc007",
			"#id": "1D647BB4-DF02-8619-2705-80ECF35859E5"
		},
		{
			"entity": "eps001/seq001/sc008",
			"#id": "C12482BE-1FDC-1485-CE6C-19CD3A7DD012"
		},
		{
			"entity": "eps001/seq001/sc009",
			"#id": "E7B3DF6E-CCCB-A898-84B4-5F8F468F8473"
		},
		{
			"entity": "eps001/seq001/sc010",
			"#id": "80F6BF87-F735-8259-E719-AC47C19DE0AB"
		},
		{
			"entity": "eps001/seq001/sc001/Layout",
			"#id": "07348913-242B-0D05-4D46-5CAF2B1B018C"
		},
		{
			"entity": "eps001/seq001/sc001/Animation",
			"#id": "0BF52E5A-C37E-F1E9-8562-ABBD29762795"
		},
		{
			"entity": "eps001/seq001/sc002/Layout",
			"#id": "760947B4-3C72-6E59-B663-B44883F5B24D"
		},
		{
			"entity": "eps001/seq001/sc002/Animation",
			"#id": "AF0F379A-35DD-432F-AEF6-211814C49A8B"
		},
		{
			"entity": "eps001/seq001/sc003/Layout",
			"#id": "FFCA1F81-A24F-180D-A396-A271B057D61F"
		},
		{
			"entity": "eps001/seq001/sc003/Animation",
			"#id": "3ECB07F7-A657-747B-FA88-0BF632B30BE7"
		},
		{
			"entity": "eps001/seq001/sc004/Layout",
			"#id": "2ED231EC-53BB-A4C3-6876-D25E3CACB8A2"
		},
		{
			"entity": "eps001/seq001/sc004/Animation",
			"#id": "01947FE4-142A-182C-DA1F-D5530FF25DC8"
		},
		{
			"entity": "eps001/seq001/sc005/Layout",
			"#id": "CA6D70FE-15CB-D457-5767-C1CFD9CE737C"
		},
		{
			"entity": "eps001/seq001/sc005/Animation",
			"#id": "3EB644FD-33A5-BDC1-3765-FAD54C22B1AC"
		},
		{
			"entity": "eps001/seq001/sc006/Layout",
			"#id": "5F8F7BA1-2884-9868-03AD-8A971C2E6568"
		},
		{
			"entity": "eps001/seq001/sc006/Animation",
			"#id": "D408BFDE-56F4-D7C2-0FBC-207779F7E4EA"
		},
		{
			"entity": "eps001/seq001/sc007/Layout",
			"#id": "25FF5C4B-C313-BBA2-4F6E-85792B95508C"
		},
		{
			"entity": "eps001/seq001/sc007/Animation",
			"#id": "90D0F6CD-BB35-D707-9792-03A7820CFC7E"
		},
		{
			"entity": "eps001/seq001/sc008/Layout",
			"#id": "D26900D7-993B-BDBA-17B6-76ED39473CA9"
		},
		{
			"entity": "eps001/seq001/sc008/Animation",
			"#id": "CF9C8E95-5C94-C703-D8F1-5635E4941BCE"
		},
		{
			"entity": "eps001/seq001/sc009/Layout",
			"#id": "99FB6B61-6923-CF7A-C9EC-2C73D5B9C271"
		},
		{
			"entity": "eps001/seq001/sc009/Animation",
			"#id": "F45D2738-9A2A-665C-EF20-A99B4D05388C"
		},
		{
			"entity": "eps001/seq001/sc010/Layout",
			"#id": "064706E7-DF5D-0DE5-1EAF-402DDDD309C8"
		},
		{
			"entity": "eps001/seq001/sc010/Animation",
			"#id": "3B11203F-C323-1437-DFD7-26301C79DE00"
		}
	]
}
```
## /cgtw7.0/log/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | log | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[field_array][] | entity | Array | 是 | 字段标识列表
data[id_array][] | {{log_id}} | Array | 是 | ID列表
data[order_field_array][] | - | Array | 否 | 排序列表
data[limit] | - | String | 否 | 限制条数,默认5000
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "eps001/seq001/sc001",
			"#id": "7B5EB2B5-0407-9615-F4C7-551AA16A4AC6"
		}
	]
}
```
## /cgtw7.0/todo_group
```text
待办事项分组
应用中心-代办事项
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/todo_group/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo_group | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"#account_id",
		"entity"
	]
}
```
## /cgtw7.0/todo_group/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo_group | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("todo_group_id", response.json.data[0]);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"DC4BF42B-9307-B6C8-9E65-EED1118925AC",
		"2A494185-FA17-B5DE-4715-1DA02CCE3C7D",
		"7FD2170E-F89D-A81B-5775-C5DA64BB3EAC",
		"2EEED53C-EE2C-93A9-5B4F-AFD72D96D2FA",
		"CF60B529-886E-76B8-C46C-BEE895A65B90"
	]
}
```
## /cgtw7.0/todo_group/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo_group | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[field_array][] | entity | Array | 是 | 字段标识列表
data[id_array][] | {{todo_group_id}} | Array | 是 | ID列表
data[order_field_array][] | entity | Array | 是 | 排序列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "11",
			"#id": "DC4BF42B-9307-B6C8-9E65-EED1118925AC"
		}
	]
}
```
## /cgtw7.0/todo_group/create
```text
创建记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo_group | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[entity] | test_create | String | 是 | 实体
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "0FA24776-ECDB-95AC-7F80-513B96EC68FF"
}
```
## /cgtw7.0/todo_group/set
```text
修改记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo_group | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[id] | {{todo_group_id}}} | String | 是 | ID
data[entity] | test_edit | String | 是 | 实体
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/todo_group/delete
```text
删除记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo_group | String | 是 | 控制器
data[method] | delete | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[id_array][] | 0FA24776-ECDB-95AC-7F80-513B96EC68FF | Array | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/todo
```text
待办事项
应用中心-代办shi x
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/todo/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"account_id",
		"todo_group_id",
		"text",
		"head_account_id",
		"attend_account_id",
		"start_date",
		"end_date",
		"status",
		"priority"
	]
}
```
## /cgtw7.0/todo/get_id
```text
获取记录id列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo | String | 是 | 控制器
data[method] | get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[filter_array] | - | Array | 否 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"BDC01AE9-FB8A-0674-6955-6F5034DC0FED",
		"731419E5-07D4-EF4F-8833-B93A07FD0513",
		"AD8C8111-5689-745C-48A7-9560F814C54B",
		"114597F3-CAA2-7B0E-BCC4-E5F9583BC023",
		"2C78C934-C832-F6D3-E1EF-E4F92214A26E",
	]
}
```
## /cgtw7.0/todo/create
```text
创建记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo | String | 是 | 控制器
data[method] | create | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[todo_group_id] | DC4BF42B-9307-B6C8-9E65-EED1118925AC | String | 是 | 分组ID
data[text] | review | String | 是 | 内容
data[status] | wait | String | 是 | 状态
data[start_date] | 2022-02-02 | String | 是 | 开始日期,format: 2021-07-11
data[end_date] | 2022-12-02 | String | 是 | 结束日期,format: 2021-07-11
data[head_account_id] | - | String | 是 | 负责人账号ID
data[attend_account_id] | - | String | 是 | 参与人账号ID,多人以逗号隔开
data[priority] | - | String | 否 | 优先级, P1到P4
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("todo_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "245BC7C1-F1D2-DD31-C11E-6D1AD0CE2B6E"
}
```
## /cgtw7.0/todo/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[field_array][] | text | Array | 是 | 字段标识列表
data[id_array][] | {{todo_id}} | Array | 是 | ID列表
data[order_field_array][] | - | Array | 否 | 排序列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"text": "11",
			"#id": "BDC01AE9-FB8A-0674-6955-6F5034DC0FED"
		}
	]
}
```
## /cgtw7.0/todo/set
```text
更新单条记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo | String | 是 | 控制器
data[method] | set | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[id] | {{todo_id}} | String | 是 | ID
data[field_data_array][text] | 11 | Array | 否 | 更新的数据
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/todo/delete
```text
删除记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | todo | String | 是 | 控制器
data[method] | delete | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[id_array][] | BDC01AE9-FB81-1674-6955-6F5034DC0FED | Array | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/pipeline_template
```text
阶段流程
设置/查看方式:项目设置-项目模板-进入项目-阶段流程
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/pipeline_template/fields
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline_template | String | 是 | 控制器
data[method] | fields | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"entity",
		"module",
		"create_by",
		"create_time",
		"last_update_by",
		"last_update_time"
	]
}
```
## /cgtw7.0/pipeline_template/get_next_and_previous_task
```text
获取任务的上游和下游任务ID
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline_template | String | 是 | 控制器
data[method] | get_next_and_previous_task | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[task_id] | B006E913-4B83-C465-D2A5-6A38D087F243 | String | 是 | 任务ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"previous": [],
		"next": [
			"2ACDCC36-A3EA-0410-5BFC-24DCC8DFE746"
		]
	}
}
```
## /cgtw7.0/pipeline_template/get_task_with_last_pipeline_id
```text
获取最后一个环节的任务ID
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline_template | String | 是 | 控制器
data[method] | get_task_with_last_pipeline_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[info_id] | 0ABB0965-9F79-E003-2E39-A7EB5904BB42 | String | 是 | 信息ID
data[db] | {{db}} | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"5C1B6B4D-7320-9383-2E78-242A1584D453"
	]
}
```
## /cgtw7.0/pipeline_template/get_next_pipeline_id
```text
获取任务的下个阶段ID
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline_template | String | 是 | 控制器
data[method] | get_next_pipeline_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[task_id] | B006E913-4B83-C465-D2A5-6A38D087F243 | String | 是 | 任务ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"01F99FCE-3407-E541-E14C-DE4BD9D17AB7"
	]
}
```
## /cgtw7.0/pipeline_template/get_next_all_task
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline_template | String | 是 | 控制器
data[method] | get_next_all_task | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[task_id] | 889CA9F5-5905-7BAE-8808-67A50B0BC11A | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"entity",
		"module",
		"create_by",
		"create_time",
		"last_update_by",
		"last_update_time"
	]
}
```
## /cgtw7.0/pipeline_template/get_all_next_and_previous_task
```text
获取所有字段标识
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline_template | String | 是 | 控制器
data[method] | get_all_next_and_previous_task | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[info_id] | 21872028-D021-20D7-54CD-0A65BCAAE670 | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"#id",
		"entity",
		"module",
		"create_by",
		"create_time",
		"last_update_by",
		"last_update_time"
	]
}
```
## /cgtw7.0/pipeline_template/get
```text
获取记录列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | pipeline_template | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
data[field_array][] | entity | Array | 是 | 字段标识列表
data[field_array][] | data | String | 是 | -
data[filter_array][0][0] | entity | String | 是 | 过滤语句列表
data[filter_array][0][1] | has | String | 是 | -
data[filter_array][0][2] | % | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "shot模板流程",
			"#id": "2CE992E5-2BB2-AFA3-B4B2-5AC7F471E501"
		},
		{
			"entity": "11",
			"#id": "F0D06F1D-1385-4953-817D-C588FE176A93"
		}
	]
}
```
## /cgtw7.0/relate
```text
相关任务
查看方式:任务-右侧面板-相关任务
设置路径:项目设置-模块管理-模块配置-启用模块组件(相关任务)
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/relate/link
```text
关联记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | relate | String | 是 | 控制器
data[method] | link | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[id_array][] | 267FE899-F915-D76A-DC75-8F400D320DF9 | Array | 是 | ID列表
data[link_id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | Array | 是 | 关联ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/relate/unlink
```text
取消关联记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | relate | String | 是 | 控制器
data[method] | unlink | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[id_array][] | 267FE899-F915-D76A-DC75-8F400D320DF9 | Array | 是 | ID列表
data[link_id_array][] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | Array | 是 | 关联ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/relate/get
```text
关联记录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | relate | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying_ml_module | String | 是 | 数据库
data[id_array][0] | DB9E804C-5B6A-C9A0-5C9B-820878AE0050 | Array | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/relate/get_from
```text
任务a关联任务b

通过任务b的id，获取关联了b的任务.
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | relate | String | 是 | 控制器
data[method] | get_from | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id_array][0] | DB9E804C-5B6A-C9A0-5C9B-820878AE0050 | Array | 是 | ID列表
data[id_array][1] | 39F15D59-66E9-4734-54F3-0DC5A1F1030A | String | 是 | ID列表
data[id_array][2] | 6C08CDF1-5B14-B17F-9488-1E9CE0F12E0B | String | 是 | -
data[id_array][3] | FCDB2F54-66D1-866B-E9FE-D3E7625DAD88 | String | 是 | -
data[id_array][4] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | String | 是 | -
data[id_array][5] | 70214928-0928-F42B-CF7D-3E01A68AFFAC | String | 是 | -
data[id_array][6] | 29A20CD5-79E6-476F-C6DE-F6408D4814CC | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/relate/get_from 副本
```text
任务a关联任务b

通过任务b的id，获取关联了b的任务.
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | relate | String | 是 | 控制器
data[method] | get_from | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id_array][0] | DB9E804C-5B6A-C9A0-5C9B-820878AE0050 | Array | 是 | ID列表
data[id_array][1] | 39F15D59-66E9-4734-54F3-0DC5A1F1030A | String | 是 | ID列表
data[id_array][2] | 6C08CDF1-5B14-B17F-9488-1E9CE0F12E0B | String | 是 | -
data[id_array][3] | FCDB2F54-66D1-866B-E9FE-D3E7625DAD88 | String | 是 | -
data[id_array][4] | EA6D6829-FD25-2D54-2BF1-65919A910C3E | String | 是 | -
data[id_array][5] | 70214928-0928-F42B-CF7D-3E01A68AFFAC | String | 是 | -
data[id_array][6] | 39A65B86-962F-E678-8D26-CEC3E8610B86 | String | 是 | -
data[id_array][7] | BCB5B13F-2027-8F4B-3AA5-0588E96BE5E3 | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/asset_lib
```text
资产库
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
apt.globals.set("lib_sign", "lib_xiaoying");
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/asset_lib/get_folder_id
```text
获取资产包的ID
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | get_folder_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[path] | 11/11/22 | String | 是 | 路径
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "B6B0B2A7-70B5-328E-9CE8-7DE11FD20029"
}
```
## /cgtw7.0/asset_lib/set_download_num
```text
设置下载次数
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | set_download_num | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[folder_id_array][] | {{asset_lib_folder_id}} | Array | 是 | id列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/asset_lib/bulk_download
```text
获取下载数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | bulk_download | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[folder_id_array][] | {{asset_lib_folder_id}} | Array | 是 | id列表
data[id_array] | "" | String | 是 | ID列表
data[current_folder_id] | - | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "71647A21-4E0D-1AEA-E20E-55B8E9E7FCBA",
			"name": "1.dpx",
			"web_path": "/upload_lib/lib_xiaoying/00000000/fce5fd9859c4d02199a7cf751ae47823.dpx",
			"path": "/11/11/22/1.dpx",
			"file_size": "33185792"
		},
		{
			"id": "DAB02FEA-0338-9831-1BAC-BEE20BA12182",
			"name": "1.bmp",
			"web_path": "/upload_lib/lib_xiaoying/00000000/1395810f1d83c5c1cecbe2bf6867c162.bmp",
			"path": "/11/11/22/1.bmp",
			"file_size": "3655734"
		}
	]
}
```
## /cgtw7.0/asset_lib/get_online_file_path_array
```text
获取在线文件对应信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | get_online_file_path_array | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[path_array][0] | /11/11/22/1.dpx | Array | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "71647A21-4E0D-1AEA-E20E-55B8E9E7FCBA",
			"path": "/11/11/22/1.dpx",
			"size": "33185792"
		}
	]
}
```
## /cgtw7.0/asset_lib/create_asset_and_get_id
```text
创建并获取资产ID
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | create_asset_and_get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[asset_path] | /aa/bb | String | 是 | 路径
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
//apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "B6B0B2A7-70B5-328E-9CE8-7DE11FD20029"
}
```
## /cgtw7.0/asset_lib/create_child_and_get_id
```text
创建子目录并获取ID
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | create_child_and_get_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[asset_id] | B6B0B2A7-70B5-328E-9CE8-7DE11FD20029 | String | 是 | 资产id
data[child_path] | test_folder | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "B6B0B2A7-70B5-328E-9CE8-7DE11FD20029"
}
```
## /cgtw7.0/asset_lib/set_cover
```text
设置为封面
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | set_cover | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[image_md5_path] | /upload_lib/lib_xiaoying/00000000/1395810f1d83c5c1cecbe2bf6867c162.bmp | String | 是 | md5路径
data[asset_id] | B6B0B2A7-70B5-328E-9CE8-7DE11FD20029 | String | 是 | 资产id
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/asset_lib/exist_file
```text
检查文件是否存在
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | exist_file | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[folder_id] | B6B0B2A7-70B5-328E-9CE8-7DE11FD20029 | String | 是 | 目录id
data[md5] | 1395810f1d83c5c1cecbe2bf6867c162 | String | 是 | 文件md5
data[entity] | 1.bmp | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"is_exist_data": "Y",
		"is_exist_review_data": "N",
		"md5_path": "/upload_lib/lib_xiaoying/00000000/1395810f1d83c5c1cecbe2bf6867c162.bmp",
		"review_md5_path": "",
		"id": "DAB02FEA-0338-9831-1BAC-BEE20BA12182"
	}
}
```
## /cgtw7.0/asset_lib/upload
```text
更新文件在服务器上的数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | upload | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[md5] | 1395810f1d83c5c1cecbe2bf6867c162 | String | 是 | md5
data[md5_path] | /upload_lib/lib_xiaoying/00000000/1395810f1d83c5c1cecbe2bf6867c162.bmp | String | 是 | 服务器上md5路径
data[entity] | 1.bmp | String | 是 | 实体
data[folder_id] | B6B0B2A7-70B5-328E-9CE8-7DE11FD20029 | String | 是 | 目录id
data[modify_time] | 2018-07-10 10:11 | String | 是 | 文件修改时间
data[size] | 3655734 | String | 是 | 文件大小
data[meta_data_array] | - | Array | 否 | 自定义的数据 (dict), 格式:{key: value}
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "566B47A3-A60F-4CE0-79A0-36A1285476D1"
}
```
## /cgtw7.0/asset_lib/set_metadata
```text
设置其他值
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | set_metadata | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[id] | 566B47A3-A60F-4CE0-79A0-36A1285476D1 | String | 是 | ID
data[meta_data_array][frame] | 1 | Array | 是 | 自定义的数据 (dict), 格式:{key: value}
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/asset_lib/update_file_modify_time
```text
更新服务器上的文件修改时间
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | update_file_modify_time | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | {{lib_sign}} | String | 是 | 资产库标识
data[entity] | 1.bmp | String | 是 | 实体
data[folder_id] | B6B0B2A7-70B5-328E-9CE8-7DE11FD20029 | String | 是 | 目录id
data[md5] | 1395810f1d83c5c1cecbe2bf6867c162 | String | 是 | md5
data[file_modify_time] | 2018-07-10 10:11:11 | Array | 是 | 文件修改
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/asset_lib/get_assetlib
```text
获取资产库
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | get_assetlib | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "lb_test",
			"sign": "lib_lbtest"
		},
		{
			"entity": "xiaoying",
			"sign": "lib_xiaoying"
		},
		{
			"entity": "343243",
			"sign": "lib_4343"
		},
		{
			"entity": "4646",
			"sign": "lib_dfs"
		},
		{
			"entity": "www",
			"sign": "lib_aaa"
		},
		{
			"entity": "11",
			"sign": "lib_11"
		},
		{
			"entity": "xiaoying1",
			"sign": "lib_xiaoying1"
		},
		{
			"entity": "mod",
			"sign": "lib_mod"
		},
		{
			"entity": "aa",
			"sign": "lib_aa"
		},
		{
			"entity": "ZG",
			"sign": "lib_zg"
		},
		{
			"entity": "sm",
			"sign": "lib_sm"
		},
		{
			"entity": "动画题材",
			"sign": "lib_asset"
		},
		{
			"entity": "妖精夜惊魂",
			"sign": "lib_yjyjh"
		},
		{
			"entity": "给v不热",
			"sign": "lib_gvbr"
		}
	]
}
```
## /cgtw7.0/asset_lib/get_asset_tree_folder
```text
获取资产库数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | asset_lib | String | 是 | 控制器
data[method] | get_asset_tree_folder | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[lib_sign] | lib_xiaoying | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "B13E3E52-173E-7BA8-0F7A-89EEDFDB964F",
			"path": "/11",
			"entity": "11",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "B3FF3163-C93B-9394-13C8-E56D146FD54E",
					"path": "/11/11",
					"entity": "11",
					"type": "tree",
					"parent_id": "B13E3E52-173E-7BA8-0F7A-89EEDFDB964F",
					"child": [
						{
							"id": "B6B0B2A7-70B5-328E-9CE8-7DE11FD20029",
							"path": "/11/11/22",
							"entity": "22",
							"type": "asset",
							"parent_id": "B3FF3163-C93B-9394-13C8-E56D146FD54E"
						}
					]
				}
			]
		},
		{
			"id": "4D5DED4C-7847-FE7E-755F-37E351211DFF",
			"path": "/21",
			"entity": "21",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "8F7EFD87-B9A5-AC7F-74F6-FFBE445B692D",
					"path": "/21/1",
					"entity": "1",
					"type": "tree",
					"parent_id": "4D5DED4C-7847-FE7E-755F-37E351211DFF",
					"child": [
						{
							"id": "A7ED914F-5868-AE79-3E06-167BB78C761E",
							"path": "/21/1/232",
							"entity": "232",
							"type": "asset",
							"parent_id": "8F7EFD87-B9A5-AC7F-74F6-FFBE445B692D"
						}
					]
				},
				{
					"id": "230E484D-BD44-03EA-9338-B1ABBE544D69",
					"path": "/21/11",
					"entity": "11",
					"type": "asset",
					"parent_id": "4D5DED4C-7847-FE7E-755F-37E351211DFF"
				},
				{
					"id": "8CE0A3E6-6FBD-1A18-6339-F1CDEFB6AA67",
					"path": "/21/22",
					"entity": "22",
					"type": "asset",
					"parent_id": "4D5DED4C-7847-FE7E-755F-37E351211DFF"
				},
				{
					"id": "BC3EBB0F-C6C0-860B-515E-4D1E4B9D840D",
					"path": "/21/360Downloads",
					"entity": "360Downloads",
					"type": "asset",
					"parent_id": "4D5DED4C-7847-FE7E-755F-37E351211DFF"
				},
				{
					"id": "150183E6-D1DB-B8BB-C3DA-A54F502E3E60",
					"path": "/21/360RecycleBin",
					"entity": "360RecycleBin",
					"type": "asset",
					"parent_id": "4D5DED4C-7847-FE7E-755F-37E351211DFF"
				},
				{
					"id": "6FF6B91C-7CB1-A56B-6312-4F28CFAEBF0E",
					"path": "/21/BaiduNetdiskDownload",
					"entity": "BaiduNetdiskDownload",
					"type": "asset",
					"parent_id": "4D5DED4C-7847-FE7E-755F-37E351211DFF"
				},
				{
					"id": "768CA6CF-3F10-0F25-8D28-FD931CA4F4BD",
					"path": "/21/ep001_eq001_sc003_Animation",
					"entity": "ep001_eq001_sc003_Animation",
					"type": "asset",
					"parent_id": "4D5DED4C-7847-FE7E-755F-37E351211DFF"
				},
				{
					"id": "D71D2C98-EF49-8A5B-ADDC-6EEC2F0D8573",
					"path": "/21/ep001_sc001_Layout",
					"entity": "ep001_sc001_Layout",
					"type": "asset",
					"parent_id": "4D5DED4C-7847-FE7E-755F-37E351211DFF"
				},
				{
					"id": "1E9FA555-ADE7-6F35-4DB2-AF37007D0886",
					"path": "/21/未命名",
					"entity": "未命名",
					"type": "tree",
					"parent_id": "4D5DED4C-7847-FE7E-755F-37E351211DFF"
				},
				{
					"id": "557C7C3B-BB62-2BE8-E2A2-47BAF0BD37EE",
					"path": "/21/未命名1",
					"entity": "未命名1",
					"type": "tree",
					"parent_id": "4D5DED4C-7847-FE7E-755F-37E351211DFF"
				}
			]
		},
		{
			"id": "D6DE872E-BCE3-62F3-EC15-6AF4B08F4479",
			"path": "/22",
			"entity": "22",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "5C0F5D5D-E1C7-886B-E934-6D102AEC92E8",
					"path": "/22/Crack-floating-tlm_server",
					"entity": "Crack-floating-tlm_server",
					"type": "asset",
					"parent_id": "D6DE872E-BCE3-62F3-EC15-6AF4B08F4479"
				}
			]
		},
		{
			"id": "41445E2B-A878-4C0E-E73F-89477045B8F5",
			"path": "/360Downloads",
			"entity": "360Downloads",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "8DBAD6B7-BD9D-0E96-C2F8-A92C74EB9F7F",
					"path": "/360Downloads/360驱动大师目录",
					"entity": "360驱动大师目录",
					"type": "asset",
					"parent_id": "41445E2B-A878-4C0E-E73F-89477045B8F5"
				}
			]
		},
		{
			"id": "D0F3A278-15FA-A86C-D3F4-6E38030239FD",
			"path": "/A2",
			"entity": "A2",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "605F344D-298A-724B-7D9D-36C5D38EFB87",
					"path": "/A2/Shot",
					"entity": "Shot",
					"type": "asset",
					"parent_id": "D0F3A278-15FA-A86C-D3F4-6E38030239FD"
				}
			]
		},
		{
			"id": "59562AB1-61C2-D823-6A9B-6EE08EB6C690",
			"path": "/asset_lib",
			"entity": "asset_lib",
			"type": "asset",
			"parent_id": ""
		},
		{
			"id": "AFED3048-A3BC-7713-4057-744E0B23684D",
			"path": "/comm",
			"entity": "comm",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "CEBECDE7-6132-3CF3-F103-DDDA8549B934",
					"path": "/comm/01",
					"entity": "01",
					"type": "asset",
					"parent_id": "AFED3048-A3BC-7713-4057-744E0B23684D"
				}
			]
		},
		{
			"id": "5D37982C-043A-8716-D12F-308948F29916",
			"path": "/SHOT01",
			"entity": "SHOT01",
			"type": "asset",
			"parent_id": ""
		},
		{
			"id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B",
			"path": "/Unclassified",
			"entity": "Unclassified",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "01297A59-5BCD-4304-4879-513158A9EB32",
					"path": "/Unclassified/11",
					"entity": "11",
					"type": "tree",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B"
				},
				{
					"id": "0C62ED7D-EC41-8934-9068-9E921DFE26FE",
					"path": "/Unclassified/11",
					"entity": "11",
					"type": "asset",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B",
					"child": [
						{
							"id": "E81A563A-B3B5-6969-6CD4-48152AAB3821",
							"path": "/Unclassified/11/11",
							"entity": "11",
							"type": "tree",
							"parent_id": "0C62ED7D-EC41-8934-9068-9E921DFE26FE",
							"child": [
								{
									"id": "808D4A0A-20A8-3775-CA2F-87D90CDEEB4F",
									"path": "/Unclassified/11/11/新建文件夹",
									"entity": "新建文件夹",
									"type": "asset",
									"parent_id": "E81A563A-B3B5-6969-6CD4-48152AAB3821"
								}
							]
						},
						{
							"id": "F1472FCD-EF46-A91F-BC98-EFC3F6ED9537",
							"path": "/Unclassified/11/33",
							"entity": "33",
							"type": "asset",
							"parent_id": "0C62ED7D-EC41-8934-9068-9E921DFE26FE"
						}
					]
				},
				{
					"id": "01801CC0-B5DE-C365-37A0-AE320BEE03BD",
					"path": "/Unclassified/22",
					"entity": "22",
					"type": "tree",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B",
					"child": [
						{
							"id": "17E2D572-3496-046B-0A55-8D0A2471B6EF",
							"path": "/Unclassified/22/js",
							"entity": "js",
							"type": "asset",
							"parent_id": "01801CC0-B5DE-C365-37A0-AE320BEE03BD"
						}
					]
				},
				{
					"id": "ED993DEE-5FF2-638F-BA84-997BA6D646FC",
					"path": "/Unclassified/33",
					"entity": "33",
					"type": "asset",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B"
				},
				{
					"id": "659DF523-0534-47B6-02CA-AC8066C4D7F7",
					"path": "/Unclassified/assembly_reference",
					"entity": "assembly_reference",
					"type": "asset",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B"
				},
				{
					"id": "34ABB964-B7CF-FB5A-03F5-C43388676262",
					"path": "/Unclassified/assetlib_reference",
					"entity": "assetlib_reference",
					"type": "asset",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B"
				},
				{
					"id": "911C3E12-DB66-57EA-3AB7-DE747139B905",
					"path": "/Unclassified/ep001_sc001_Layout",
					"entity": "ep001_sc001_Layout",
					"type": "asset",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B"
				},
				{
					"id": "D368A2CE-E1DF-D8E7-243E-2E2CC1BAD5B0",
					"path": "/Unclassified/EP01_SHOT003_Layout",
					"entity": "EP01_SHOT003_Layout",
					"type": "asset",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B"
				},
				{
					"id": "0CC6FF4E-58AF-0589-6705-69169B85919C",
					"path": "/Unclassified/max动画",
					"entity": "max动画",
					"type": "tree",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B",
					"child": [
						{
							"id": "1D9A5839-C1DE-8167-3A2F-1B46A64D7639",
							"path": "/Unclassified/max动画/sc001_001.mov",
							"entity": "sc001_001.mov",
							"type": "asset",
							"parent_id": "0CC6FF4E-58AF-0589-6705-69169B85919C"
						},
						{
							"id": "56D4BBE1-D099-6AAA-CB28-736D0959B0E6",
							"path": "/Unclassified/max动画/sc001_002.mov",
							"entity": "sc001_002.mov",
							"type": "asset",
							"parent_id": "0CC6FF4E-58AF-0589-6705-69169B85919C"
						},
						{
							"id": "F15A1F33-23AD-DFF1-A79C-C2E92B407769",
							"path": "/Unclassified/max动画/sc001_003.mov",
							"entity": "sc001_003.mov",
							"type": "asset",
							"parent_id": "0CC6FF4E-58AF-0589-6705-69169B85919C"
						},
						{
							"id": "C23D6F21-6D39-D7E2-3F65-5FE70303BF63",
							"path": "/Unclassified/max动画/sc001_004.mov",
							"entity": "sc001_004.mov",
							"type": "asset",
							"parent_id": "0CC6FF4E-58AF-0589-6705-69169B85919C"
						},
						{
							"id": "59BB1B42-42D9-CA45-B3E5-91B168AE8EC7",
							"path": "/Unclassified/max动画/sc001_005.mov",
							"entity": "sc001_005.mov",
							"type": "asset",
							"parent_id": "0CC6FF4E-58AF-0589-6705-69169B85919C"
						},
						{
							"id": "61EB8D8C-C694-ADAB-A5A0-E807C1DE2FD0",
							"path": "/Unclassified/max动画/sc001_006.mov",
							"entity": "sc001_006.mov",
							"type": "asset",
							"parent_id": "0CC6FF4E-58AF-0589-6705-69169B85919C"
						},
						{
							"id": "2EEAAAB2-5A3E-0CC0-06AE-EDA2A52314AD",
							"path": "/Unclassified/max动画/sc001_007.mov",
							"entity": "sc001_007.mov",
							"type": "asset",
							"parent_id": "0CC6FF4E-58AF-0589-6705-69169B85919C"
						},
						{
							"id": "35264C9C-49CB-E953-702B-CBC5C60722E2",
							"path": "/Unclassified/max动画/sc001_008.mov",
							"entity": "sc001_008.mov",
							"type": "asset",
							"parent_id": "0CC6FF4E-58AF-0589-6705-69169B85919C"
						},
						{
							"id": "D595439D-F3A8-A012-39A3-00966EDF34D5",
							"path": "/Unclassified/max动画/sc001_009.mov",
							"entity": "sc001_009.mov",
							"type": "asset",
							"parent_id": "0CC6FF4E-58AF-0589-6705-69169B85919C"
						}
					]
				},
				{
					"id": "D8B32CE9-90C6-7DCE-39CA-8954F46424BF",
					"path": "/Unclassified/max动画",
					"entity": "max动画",
					"type": "tree",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B",
					"child": [
						{
							"id": "823E349C-C27A-80BC-1A0F-0B8CAAC8CFCA",
							"path": "/Unclassified/max动画/sc001_001.mov",
							"entity": "sc001_001.mov",
							"type": "asset",
							"parent_id": "D8B32CE9-90C6-7DCE-39CA-8954F46424BF"
						},
						{
							"id": "E0C853FF-92D0-DFEE-4B61-E27599E3F091",
							"path": "/Unclassified/max动画/sc001_002.mov",
							"entity": "sc001_002.mov",
							"type": "asset",
							"parent_id": "D8B32CE9-90C6-7DCE-39CA-8954F46424BF"
						},
						{
							"id": "B421D766-422B-4CB8-D12D-989CB691D51B",
							"path": "/Unclassified/max动画/sc001_003.mov",
							"entity": "sc001_003.mov",
							"type": "asset",
							"parent_id": "D8B32CE9-90C6-7DCE-39CA-8954F46424BF"
						},
						{
							"id": "261F53CE-A5A4-19BC-3FFD-7E36DDE91338",
							"path": "/Unclassified/max动画/sc001_004.mov",
							"entity": "sc001_004.mov",
							"type": "asset",
							"parent_id": "D8B32CE9-90C6-7DCE-39CA-8954F46424BF"
						},
						{
							"id": "7F3DB1F4-F7E4-AA02-7CAE-5F39C880D15B",
							"path": "/Unclassified/max动画/sc001_005.mov",
							"entity": "sc001_005.mov",
							"type": "asset",
							"parent_id": "D8B32CE9-90C6-7DCE-39CA-8954F46424BF"
						},
						{
							"id": "4C86DF72-C3E6-0E9F-EC94-D399DA277DEB",
							"path": "/Unclassified/max动画/sc001_006.mov",
							"entity": "sc001_006.mov",
							"type": "asset",
							"parent_id": "D8B32CE9-90C6-7DCE-39CA-8954F46424BF"
						},
						{
							"id": "DBE512E6-22DB-2504-5972-F57E9A292102",
							"path": "/Unclassified/max动画/sc001_007.mov",
							"entity": "sc001_007.mov",
							"type": "asset",
							"parent_id": "D8B32CE9-90C6-7DCE-39CA-8954F46424BF"
						},
						{
							"id": "6257FE63-C6A4-3F17-6B04-F8F607BD0322",
							"path": "/Unclassified/max动画/sc001_008.mov",
							"entity": "sc001_008.mov",
							"type": "asset",
							"parent_id": "D8B32CE9-90C6-7DCE-39CA-8954F46424BF"
						},
						{
							"id": "433DCED2-7F64-C37C-8100-CDA73FDE1BE9",
							"path": "/Unclassified/max动画/sc001_009.mov",
							"entity": "sc001_009.mov",
							"type": "asset",
							"parent_id": "D8B32CE9-90C6-7DCE-39CA-8954F46424BF"
						}
					]
				},
				{
					"id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6",
					"path": "/Unclassified/max动画",
					"entity": "max动画",
					"type": "tree",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B",
					"child": [
						{
							"id": "D4A5CC90-D6BF-2CC8-8B6D-27E33894749B",
							"path": "/Unclassified/max动画/sc001_001.mov",
							"entity": "sc001_001.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "28F6CFFB-5C58-337E-6CE5-F17F35A6329C",
							"path": "/Unclassified/max动画/sc001_002.mov",
							"entity": "sc001_002.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "6B0D3402-5EF6-41F8-C4D0-CE3767D75DFB",
							"path": "/Unclassified/max动画/sc001_003.mov",
							"entity": "sc001_003.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "978AF022-BADB-CCC5-3E3B-8E4403DB3ED9",
							"path": "/Unclassified/max动画/sc001_004.mov",
							"entity": "sc001_004.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "82E91994-C64A-410B-6212-EE24AE6059DE",
							"path": "/Unclassified/max动画/sc001_005.mov",
							"entity": "sc001_005.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "A6119ECD-7208-A837-FED0-031A9EB8BB5B",
							"path": "/Unclassified/max动画/sc001_006.mov",
							"entity": "sc001_006.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "372227DC-2906-FF1F-3A58-EA50E471A76D",
							"path": "/Unclassified/max动画/sc001_007.mov",
							"entity": "sc001_007.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "AF7DA6E7-31C6-900A-9D12-A615ED0CD533",
							"path": "/Unclassified/max动画/sc001_008.mov",
							"entity": "sc001_008.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "BACB5728-AD14-5EFE-4A95-9652B7D9BCCA",
							"path": "/Unclassified/max动画/sc001_009.mov",
							"entity": "sc001_009.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "DDBC5765-46BF-F961-8E7D-0CF6FE2C0356",
							"path": "/Unclassified/max动画/sc001_010.mov",
							"entity": "sc001_010.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "C2749E6E-6BDA-FE97-5903-20ABA28453D5",
							"path": "/Unclassified/max动画/sc001_011.mov",
							"entity": "sc001_011.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "40249EAD-E420-E7E3-6BA4-AA9200754F4A",
							"path": "/Unclassified/max动画/sc001_012.mov",
							"entity": "sc001_012.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "A7227628-B246-0EF4-E637-57C17C99C8F9",
							"path": "/Unclassified/max动画/sc001_013.mov",
							"entity": "sc001_013.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "61570E9C-C38B-F93F-E344-BDA3AC07D084",
							"path": "/Unclassified/max动画/sc001_014.mov",
							"entity": "sc001_014.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "B990E044-94AA-088B-C189-40D1EFDBDA96",
							"path": "/Unclassified/max动画/sc001_015.mov",
							"entity": "sc001_015.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "DEB35419-25BF-9D4B-FDF8-8553F0079556",
							"path": "/Unclassified/max动画/sc001_016.mov",
							"entity": "sc001_016.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "B2E67C33-CC06-F24D-752F-916991120546",
							"path": "/Unclassified/max动画/sc001_017.mov",
							"entity": "sc001_017.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "764539C5-1EDD-BC09-314D-565727A355AF",
							"path": "/Unclassified/max动画/sc001_018.mov",
							"entity": "sc001_018.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "F273BF18-CF33-9DFA-6540-5CD1E8F2BA3A",
							"path": "/Unclassified/max动画/sc001_019.mov",
							"entity": "sc001_019.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "4C426C2D-4D44-7D7B-4327-0C35DE885716",
							"path": "/Unclassified/max动画/sc001_020.mov",
							"entity": "sc001_020.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "220BA8C4-42B4-8712-64B1-316EE53F3167",
							"path": "/Unclassified/max动画/sc001_021.mov",
							"entity": "sc001_021.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "83EDB993-1844-6821-2B71-2F939993075B",
							"path": "/Unclassified/max动画/sc001_022.mov",
							"entity": "sc001_022.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "AA5019DA-531D-D17B-2BDA-3A80BA1DBFFA",
							"path": "/Unclassified/max动画/sc001_023.mov",
							"entity": "sc001_023.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "3BB1E426-CC25-9672-C8BC-1539F8131B43",
							"path": "/Unclassified/max动画/sc001_024.mov",
							"entity": "sc001_024.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "9D5B425C-134A-62FD-A7F6-EF998F416B04",
							"path": "/Unclassified/max动画/sc001_025.mov",
							"entity": "sc001_025.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "84BEAB99-9C7D-47DB-50FD-1D18C95D2559",
							"path": "/Unclassified/max动画/sc001_026.mov",
							"entity": "sc001_026.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "17267E15-9F95-631C-947F-8600A7B1A8A2",
							"path": "/Unclassified/max动画/sc001_027.mov",
							"entity": "sc001_027.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "E84E04ED-9549-C795-BE31-0B8014814272",
							"path": "/Unclassified/max动画/sc001_028.mov",
							"entity": "sc001_028.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "2E7E52C8-5E54-2971-BB7C-4D38E61B26D2",
							"path": "/Unclassified/max动画/sc001_029.mov",
							"entity": "sc001_029.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "9655029D-A856-8A6D-E60B-70E1269F21FC",
							"path": "/Unclassified/max动画/sc001_030.mov",
							"entity": "sc001_030.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "0168C48E-430C-9FAF-39CC-4582F98A5321",
							"path": "/Unclassified/max动画/sc001_031.mov",
							"entity": "sc001_031.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "55AA34FD-4FCB-129D-9F98-1710D9D47043",
							"path": "/Unclassified/max动画/sc001_032.mov",
							"entity": "sc001_032.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "828B7B7B-D25D-47D3-1358-83FF30F71276",
							"path": "/Unclassified/max动画/sc001_033.mov",
							"entity": "sc001_033.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "1C0EEEE6-CE1E-633F-2126-416EF46A1CD5",
							"path": "/Unclassified/max动画/sc001_034.mov",
							"entity": "sc001_034.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "494F9413-F561-A84C-E79F-787DD20270DA",
							"path": "/Unclassified/max动画/sc001_035.mov",
							"entity": "sc001_035.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "808E4026-01A4-B955-BB35-1C8D5028406E",
							"path": "/Unclassified/max动画/sc001_036.mov",
							"entity": "sc001_036.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "4ECF5187-13D0-990A-C4E0-68A8015F2CB8",
							"path": "/Unclassified/max动画/sc001_037.mov",
							"entity": "sc001_037.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "398CD910-D015-4F57-DF2E-A44B068C36FA",
							"path": "/Unclassified/max动画/sc001_038.mov",
							"entity": "sc001_038.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "CFFAF964-246A-F23F-C28D-F20B5F624827",
							"path": "/Unclassified/max动画/sc001_039.mov",
							"entity": "sc001_039.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "A03CE6A2-3A5B-2FDF-33C6-E31DB40B437A",
							"path": "/Unclassified/max动画/sc001_040.mov",
							"entity": "sc001_040.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "24616EDB-C60E-CC48-EF26-FB52F01DBA37",
							"path": "/Unclassified/max动画/sc001_041.mov",
							"entity": "sc001_041.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "19CE23E4-D93F-F757-533F-009EEA646B12",
							"path": "/Unclassified/max动画/sc001_042.mov",
							"entity": "sc001_042.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "9DEED840-557E-075D-B63C-16AF6A5C1649",
							"path": "/Unclassified/max动画/sc001_043.mov",
							"entity": "sc001_043.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "9CF5FFE2-C7F1-AB1F-771D-9F642CC6AE28",
							"path": "/Unclassified/max动画/sc001_044.mov",
							"entity": "sc001_044.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "8B681756-A9A8-3409-BA17-A91AF33B69AF",
							"path": "/Unclassified/max动画/sc001_045.mov",
							"entity": "sc001_045.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "9C885FF3-1042-7238-3727-0F3AB987AD88",
							"path": "/Unclassified/max动画/sc001_046.mov",
							"entity": "sc001_046.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "3AD768E2-5A5C-450E-7D7D-692DC427D659",
							"path": "/Unclassified/max动画/sc001_047.mov",
							"entity": "sc001_047.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "2F354343-5AC7-A884-D422-9B6C07DBA37C",
							"path": "/Unclassified/max动画/sc001_048.mov",
							"entity": "sc001_048.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "F755433B-E749-A9E9-6BD2-06035F7B8C2B",
							"path": "/Unclassified/max动画/sc001_049.mov",
							"entity": "sc001_049.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "0AE4E993-B067-2466-D2ED-F71C86895BF9",
							"path": "/Unclassified/max动画/sc001_050.mov",
							"entity": "sc001_050.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "C5C54971-9A57-D33E-E58B-EE7026EDF0B2",
							"path": "/Unclassified/max动画/sc001_051.mov",
							"entity": "sc001_051.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "067FDD9B-E0DB-DF57-4B12-93A3CED2E279",
							"path": "/Unclassified/max动画/sc001_052.mov",
							"entity": "sc001_052.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "F91FA3CF-1CA3-CB95-E94A-FF1C0A8E271D",
							"path": "/Unclassified/max动画/sc001_053.mov",
							"entity": "sc001_053.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "9CD19109-08DA-978B-BF3D-4B25E8FEE522",
							"path": "/Unclassified/max动画/sc001_054.mov",
							"entity": "sc001_054.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "420049F6-6DCB-BD1C-5AE5-C5B5CA038C81",
							"path": "/Unclassified/max动画/sc001_055.mov",
							"entity": "sc001_055.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "618F1A5E-C552-FE52-2F11-6491CC97A044",
							"path": "/Unclassified/max动画/sc001_056.mov",
							"entity": "sc001_056.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "161B9893-A757-C19B-686A-347FA8C90824",
							"path": "/Unclassified/max动画/sc001_057.mov",
							"entity": "sc001_057.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "28570F60-5F47-B61B-2397-2C7892C2CC81",
							"path": "/Unclassified/max动画/sc001_058.mov",
							"entity": "sc001_058.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "7DB9A7A4-9DE9-3DDC-E92B-729B3B350AB4",
							"path": "/Unclassified/max动画/sc001_059.mov",
							"entity": "sc001_059.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "21CCB7D8-7428-661F-15BF-267DE38DB44A",
							"path": "/Unclassified/max动画/sc001_060.mov",
							"entity": "sc001_060.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "6189C62E-4A2A-A524-41EA-CC4C6FCD93DF",
							"path": "/Unclassified/max动画/sc001_061.mov",
							"entity": "sc001_061.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "5781784B-CA57-3F07-CF2A-43E9F56E8008",
							"path": "/Unclassified/max动画/sc001_062.mov",
							"entity": "sc001_062.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "5953D771-3215-CAA9-226D-2BFED1D0926B",
							"path": "/Unclassified/max动画/sc001_063.mov",
							"entity": "sc001_063.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "30661313-F53B-D2E8-28C7-0E7DAD1D0E86",
							"path": "/Unclassified/max动画/sc001_064.mov",
							"entity": "sc001_064.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "0E307D17-1269-5A85-C764-0C6FE90F889A",
							"path": "/Unclassified/max动画/sc001_065.mov",
							"entity": "sc001_065.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "B57BE2B9-A52F-59D0-F82C-EA711728C1B1",
							"path": "/Unclassified/max动画/sc001_066.mov",
							"entity": "sc001_066.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "F0771F84-2088-3184-26F0-3BCAA09AB87A",
							"path": "/Unclassified/max动画/sc001_067.mov",
							"entity": "sc001_067.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "0D9BFE33-ABBF-6436-7279-B93AF3F011C1",
							"path": "/Unclassified/max动画/sc001_068.mov",
							"entity": "sc001_068.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "8EBBF84C-3882-1671-EB8E-CE4F64CFD344",
							"path": "/Unclassified/max动画/sc001_069.mov",
							"entity": "sc001_069.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "0375EB1B-C5DE-E7C9-29F0-41A9D51D992D",
							"path": "/Unclassified/max动画/sc001_070.mov",
							"entity": "sc001_070.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "92F7249A-52D3-FA68-31EF-54A0F6D73EC7",
							"path": "/Unclassified/max动画/sc001_071.mov",
							"entity": "sc001_071.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "9724671F-E495-50B9-3D65-2B24D7F4DEE1",
							"path": "/Unclassified/max动画/sc001_072.mov",
							"entity": "sc001_072.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "3E044D59-3F62-BE11-38AB-604FCFAA6CA9",
							"path": "/Unclassified/max动画/sc001_073.mov",
							"entity": "sc001_073.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "4BF18A87-D274-9E20-BA8B-19BBD26A1650",
							"path": "/Unclassified/max动画/sc001_074.mov",
							"entity": "sc001_074.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "638F71EB-63FF-1AFA-00D5-7A83B4E88D8B",
							"path": "/Unclassified/max动画/sc001_075.mov",
							"entity": "sc001_075.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "38EB68AB-2909-D8D9-B9B5-74D2B5DF7870",
							"path": "/Unclassified/max动画/sc001_076.mov",
							"entity": "sc001_076.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "B0C5C84D-2217-C323-C3F6-00A5F05741CD",
							"path": "/Unclassified/max动画/sc001_077.mov",
							"entity": "sc001_077.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "3826FD89-ED74-1241-B00E-F9AA87570231",
							"path": "/Unclassified/max动画/sc001_078.mov",
							"entity": "sc001_078.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "742BA9C7-0D6F-AB39-5653-3A14C1468D39",
							"path": "/Unclassified/max动画/sc001_079.mov",
							"entity": "sc001_079.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "D7ED9437-8159-334D-BFA7-F30F10468BE8",
							"path": "/Unclassified/max动画/sc001_080.mov",
							"entity": "sc001_080.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "BA3ED4E8-27A4-7147-A21F-2C340D89A1F2",
							"path": "/Unclassified/max动画/sc001_081.mov",
							"entity": "sc001_081.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "D0E72FE9-34B2-63EC-BBD4-DF7F0F380A09",
							"path": "/Unclassified/max动画/sc001_082.mov",
							"entity": "sc001_082.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "584FE5B2-2593-1407-488A-4E4433B43710",
							"path": "/Unclassified/max动画/sc001_083.mov",
							"entity": "sc001_083.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "2ADCBBFA-6F67-2868-8836-AD0843E2ECDE",
							"path": "/Unclassified/max动画/sc001_084.mov",
							"entity": "sc001_084.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "9BF4E4F8-4B9F-775B-637E-1B55898EA58F",
							"path": "/Unclassified/max动画/sc001_085.mov",
							"entity": "sc001_085.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "6FC6CF7D-45BD-0AFF-01FD-369A0B1CB592",
							"path": "/Unclassified/max动画/sc001_086.mov",
							"entity": "sc001_086.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "C993DC6A-72C6-4893-F08D-D9761DFB5852",
							"path": "/Unclassified/max动画/sc001_087.mov",
							"entity": "sc001_087.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "7F2EB865-B163-D3DB-7F3D-B784055A47E6",
							"path": "/Unclassified/max动画/sc001_088.mov",
							"entity": "sc001_088.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "CA2DE059-6A77-2C3B-29E1-AB9FE7EC3EAC",
							"path": "/Unclassified/max动画/sc001_089.mov",
							"entity": "sc001_089.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "25CA1FEB-E919-E10F-7E17-C48F7042078B",
							"path": "/Unclassified/max动画/sc001_090.mov",
							"entity": "sc001_090.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "C3C53C23-54EF-5AB5-425F-66596D12436A",
							"path": "/Unclassified/max动画/sc001_091.mov",
							"entity": "sc001_091.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "9B72EDA0-8B19-2325-9346-E67668953566",
							"path": "/Unclassified/max动画/sc001_092.mov",
							"entity": "sc001_092.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "3EE383F6-3189-06BE-BCC0-D1FC41E084F4",
							"path": "/Unclassified/max动画/sc001_093.mov",
							"entity": "sc001_093.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "46DD41FD-8A74-BA0D-6EC4-6E62A53DA6C8",
							"path": "/Unclassified/max动画/sc001_094.mov",
							"entity": "sc001_094.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "D80AD542-2C88-9F4B-9BCB-7BE2A217E2F3",
							"path": "/Unclassified/max动画/sc001_095.mov",
							"entity": "sc001_095.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "CE5F40C6-BB12-63C3-CEE6-C443F6EF919F",
							"path": "/Unclassified/max动画/sc001_096.mov",
							"entity": "sc001_096.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "A09DEE47-20B9-028E-B049-200DCCFCEA9E",
							"path": "/Unclassified/max动画/sc001_097.mov",
							"entity": "sc001_097.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "E612168C-6AC6-BC0B-6AE7-6E7A4FDE26BC",
							"path": "/Unclassified/max动画/sc001_098.mov",
							"entity": "sc001_098.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						},
						{
							"id": "80845232-A3B1-50F5-70C5-7508D0DC2D5E",
							"path": "/Unclassified/max动画/sc001_099.mov",
							"entity": "sc001_099.mov",
							"type": "asset",
							"parent_id": "3D2FAD29-6171-E15F-612E-BB4D24987CF6"
						}
					]
				},
				{
					"id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37",
					"path": "/Unclassified/max动画_20230202164113",
					"entity": "max动画_20230202164113",
					"type": "tree",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B",
					"child": [
						{
							"id": "3CCC423C-5840-AC3C-E641-C91B57EDC717",
							"path": "/Unclassified/max动画_20230202164113/sc001_001.mov",
							"entity": "sc001_001.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "092543DB-E062-0719-F352-401846634A92",
							"path": "/Unclassified/max动画_20230202164113/sc001_002.mov",
							"entity": "sc001_002.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "A31F1F6D-7AC1-1F3C-8C72-351991B01F78",
							"path": "/Unclassified/max动画_20230202164113/sc001_003.mov",
							"entity": "sc001_003.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "19871B12-3988-0FEB-8478-A1ED9609C648",
							"path": "/Unclassified/max动画_20230202164113/sc001_004.mov",
							"entity": "sc001_004.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "10E3C35D-6D95-73BA-A7A2-FF914901550F",
							"path": "/Unclassified/max动画_20230202164113/sc001_005.mov",
							"entity": "sc001_005.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "E48A048F-34D2-61CB-021F-03D69411C6F2",
							"path": "/Unclassified/max动画_20230202164113/sc001_006.mov",
							"entity": "sc001_006.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "23CF55A1-876A-64E7-474A-C83B612082D0",
							"path": "/Unclassified/max动画_20230202164113/sc001_007.mov",
							"entity": "sc001_007.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "3A15A42A-243F-D9F1-4328-2175084C3E1E",
							"path": "/Unclassified/max动画_20230202164113/sc001_008.mov",
							"entity": "sc001_008.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "330CAC05-3E25-FCDC-4E78-D19267535DC3",
							"path": "/Unclassified/max动画_20230202164113/sc001_009.mov",
							"entity": "sc001_009.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "E38156AC-4EA8-3B6F-D638-E0703C2F3943",
							"path": "/Unclassified/max动画_20230202164113/sc001_010.mov",
							"entity": "sc001_010.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "67AC971F-735C-EFCE-BD33-3702A9E97C84",
							"path": "/Unclassified/max动画_20230202164113/sc001_011.mov",
							"entity": "sc001_011.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "AB1FFD27-E932-EDBB-3ACB-719D0D3FD6EF",
							"path": "/Unclassified/max动画_20230202164113/sc001_012.mov",
							"entity": "sc001_012.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "7F10AE01-00E0-79C9-BF05-F6567FBAB6ED",
							"path": "/Unclassified/max动画_20230202164113/sc001_013.mov",
							"entity": "sc001_013.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "5FD6C369-132D-2012-46EC-1E7E0269B9D0",
							"path": "/Unclassified/max动画_20230202164113/sc001_014.mov",
							"entity": "sc001_014.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "0AF23C1A-5FC4-5BB3-2DA5-C0EF5C036E73",
							"path": "/Unclassified/max动画_20230202164113/sc001_015.mov",
							"entity": "sc001_015.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "32983095-405C-D96E-71C6-086AC252D587",
							"path": "/Unclassified/max动画_20230202164113/sc001_016.mov",
							"entity": "sc001_016.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "FE9C85DF-FA6B-D36E-17C0-B3DEC2357A2E",
							"path": "/Unclassified/max动画_20230202164113/sc001_017.mov",
							"entity": "sc001_017.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "0D4F6C59-74F6-ABDD-CFAB-7281E1FE3718",
							"path": "/Unclassified/max动画_20230202164113/sc001_018.mov",
							"entity": "sc001_018.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "A24EFCB5-7608-2809-2583-341CA9B7CA04",
							"path": "/Unclassified/max动画_20230202164113/sc001_019.mov",
							"entity": "sc001_019.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "2C74F6DB-97C4-6E5A-0009-5ED685D7C7BD",
							"path": "/Unclassified/max动画_20230202164113/sc001_020.mov",
							"entity": "sc001_020.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "9FFDEA12-DB8F-4DF2-9F5F-EEE55E6180FB",
							"path": "/Unclassified/max动画_20230202164113/sc001_021.mov",
							"entity": "sc001_021.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "0E27C47A-F2F9-3BF2-678A-C888AF6CF3B4",
							"path": "/Unclassified/max动画_20230202164113/sc001_022.mov",
							"entity": "sc001_022.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "85D988B2-25D7-5D16-0F38-67CD44AF60C4",
							"path": "/Unclassified/max动画_20230202164113/sc001_023.mov",
							"entity": "sc001_023.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "9FD29830-FB13-8252-855C-77C9F2DA7D62",
							"path": "/Unclassified/max动画_20230202164113/sc001_024.mov",
							"entity": "sc001_024.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "D9B669AF-2E52-5BBF-089F-91F6FB600891",
							"path": "/Unclassified/max动画_20230202164113/sc001_025.mov",
							"entity": "sc001_025.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "0A619BD5-E346-F6E4-7098-B32BD68A2C8D",
							"path": "/Unclassified/max动画_20230202164113/sc001_026.mov",
							"entity": "sc001_026.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "36778305-C2AF-3DC2-52B5-97832A33A9A3",
							"path": "/Unclassified/max动画_20230202164113/sc001_027.mov",
							"entity": "sc001_027.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "78D46314-8450-A3E4-4069-EFEE125E33B9",
							"path": "/Unclassified/max动画_20230202164113/sc001_028.mov",
							"entity": "sc001_028.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "E7E158EA-9B50-375B-0066-71007BD41ABA",
							"path": "/Unclassified/max动画_20230202164113/sc001_029.mov",
							"entity": "sc001_029.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "2C90260B-61C0-2B7B-8EE3-C48FE9C100BD",
							"path": "/Unclassified/max动画_20230202164113/sc001_030.mov",
							"entity": "sc001_030.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "B92039C9-1B93-9039-1256-1971F1EF5541",
							"path": "/Unclassified/max动画_20230202164113/sc001_031.mov",
							"entity": "sc001_031.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "31E1949D-9497-FC0D-4B56-C5A77A552374",
							"path": "/Unclassified/max动画_20230202164113/sc001_032.mov",
							"entity": "sc001_032.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "39BE1400-634D-5A88-CFF6-BA7E7A9A3A23",
							"path": "/Unclassified/max动画_20230202164113/sc001_033.mov",
							"entity": "sc001_033.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "E47E3BD1-06D0-1B12-527A-23396D646B6A",
							"path": "/Unclassified/max动画_20230202164113/sc001_034.mov",
							"entity": "sc001_034.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "E77CCD0F-527F-25F9-59D1-994848E8BB16",
							"path": "/Unclassified/max动画_20230202164113/sc001_035.mov",
							"entity": "sc001_035.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "F6E80591-EB63-8D69-0654-506FE5C875DF",
							"path": "/Unclassified/max动画_20230202164113/sc001_036.mov",
							"entity": "sc001_036.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "D5D26AAB-A411-41F0-0B17-B153FA462B33",
							"path": "/Unclassified/max动画_20230202164113/sc001_037.mov",
							"entity": "sc001_037.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "CC417FEB-FFFB-129D-5C90-30B08E468F04",
							"path": "/Unclassified/max动画_20230202164113/sc001_038.mov",
							"entity": "sc001_038.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "335867B6-2AE0-ACFD-1050-178A12973DA3",
							"path": "/Unclassified/max动画_20230202164113/sc001_039.mov",
							"entity": "sc001_039.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "08769613-C232-D52D-5237-84A00E1F7CE8",
							"path": "/Unclassified/max动画_20230202164113/sc001_040.mov",
							"entity": "sc001_040.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "3B3BB622-7E9B-3964-95B5-E798097B851C",
							"path": "/Unclassified/max动画_20230202164113/sc001_041.mov",
							"entity": "sc001_041.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "59BB3192-4EA2-F86D-E57F-7CBD0C501E35",
							"path": "/Unclassified/max动画_20230202164113/sc001_042.mov",
							"entity": "sc001_042.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "85D5D92F-FB45-F5C0-D343-73A0C00721B4",
							"path": "/Unclassified/max动画_20230202164113/sc001_043.mov",
							"entity": "sc001_043.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "DCA3D1B2-A1F4-2FB1-FA33-4B3FF61C3E7A",
							"path": "/Unclassified/max动画_20230202164113/sc001_044.mov",
							"entity": "sc001_044.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "701BC905-CEC7-2F3E-43C1-A93A335626DF",
							"path": "/Unclassified/max动画_20230202164113/sc001_045.mov",
							"entity": "sc001_045.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "B9E4AAD4-2FB3-1498-FA0A-92742EDB4AA1",
							"path": "/Unclassified/max动画_20230202164113/sc001_046.mov",
							"entity": "sc001_046.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "7529BC98-D8AE-528F-D810-BF92962BF863",
							"path": "/Unclassified/max动画_20230202164113/sc001_047.mov",
							"entity": "sc001_047.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "37A0CA75-4627-15F0-6F79-BF5DCA7A745E",
							"path": "/Unclassified/max动画_20230202164113/sc001_048.mov",
							"entity": "sc001_048.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "FAA4113C-B8D6-CB07-C4F6-8DF734BA116E",
							"path": "/Unclassified/max动画_20230202164113/sc001_049.mov",
							"entity": "sc001_049.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "93112FEA-BEBA-E099-E4C4-552C0DDBD69D",
							"path": "/Unclassified/max动画_20230202164113/sc001_050.mov",
							"entity": "sc001_050.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "63259916-E53C-B3FB-D73E-6937CE217DDB",
							"path": "/Unclassified/max动画_20230202164113/sc001_051.mov",
							"entity": "sc001_051.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "225D6C4B-16C7-3EDD-62E0-A550480BDCB4",
							"path": "/Unclassified/max动画_20230202164113/sc001_052.mov",
							"entity": "sc001_052.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "B416CC85-9238-F3C4-BF00-AE32858F0552",
							"path": "/Unclassified/max动画_20230202164113/sc001_053.mov",
							"entity": "sc001_053.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "BA869860-FD30-B325-DF7A-DB4B809D672E",
							"path": "/Unclassified/max动画_20230202164113/sc001_054.mov",
							"entity": "sc001_054.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "6EA0B494-3662-CB50-8E64-D8C4F98922F5",
							"path": "/Unclassified/max动画_20230202164113/sc001_055.mov",
							"entity": "sc001_055.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "065C6B40-8F69-1D39-EE79-C93F9F4CE3C0",
							"path": "/Unclassified/max动画_20230202164113/sc001_056.mov",
							"entity": "sc001_056.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "4551D897-81EC-967A-0DBC-B0933A2FD7E6",
							"path": "/Unclassified/max动画_20230202164113/sc001_057.mov",
							"entity": "sc001_057.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "93BB9CF5-8C07-8318-A865-7B49C9AE9280",
							"path": "/Unclassified/max动画_20230202164113/sc001_058.mov",
							"entity": "sc001_058.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "E7E87FBF-B7E2-B079-A794-EF828C50CCBB",
							"path": "/Unclassified/max动画_20230202164113/sc001_059.mov",
							"entity": "sc001_059.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "779B3B59-3FFF-E00F-C65A-2D7E58567701",
							"path": "/Unclassified/max动画_20230202164113/sc001_060.mov",
							"entity": "sc001_060.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "D77AD559-A835-533B-2FBC-4F3069641683",
							"path": "/Unclassified/max动画_20230202164113/sc001_061.mov",
							"entity": "sc001_061.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "9A63C37A-D32F-8927-FAEB-0AE9D5B9588A",
							"path": "/Unclassified/max动画_20230202164113/sc001_062.mov",
							"entity": "sc001_062.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "C8023A75-827E-C175-E437-E2D2DC89D24A",
							"path": "/Unclassified/max动画_20230202164113/sc001_063.mov",
							"entity": "sc001_063.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "ECF0D90E-EF50-A183-AB13-7D1B5A18EDB0",
							"path": "/Unclassified/max动画_20230202164113/sc001_064.mov",
							"entity": "sc001_064.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "C0E730CC-B72D-9A26-E03B-3CC4887453E0",
							"path": "/Unclassified/max动画_20230202164113/sc001_065.mov",
							"entity": "sc001_065.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "37B2AF5F-65F8-0D8C-EC9F-0081D230FE0F",
							"path": "/Unclassified/max动画_20230202164113/sc001_066.mov",
							"entity": "sc001_066.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "DD3048DF-B082-1F50-A941-C65A451223F7",
							"path": "/Unclassified/max动画_20230202164113/sc001_067.mov",
							"entity": "sc001_067.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "7B562605-C202-E1F6-83C8-6C91D8770BFD",
							"path": "/Unclassified/max动画_20230202164113/sc001_068.mov",
							"entity": "sc001_068.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "2879331B-89DC-C162-BF2C-98BAA681B4D5",
							"path": "/Unclassified/max动画_20230202164113/sc001_069.mov",
							"entity": "sc001_069.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "FB66D794-2948-2D7F-52D1-8D4FA395D99D",
							"path": "/Unclassified/max动画_20230202164113/sc001_070.mov",
							"entity": "sc001_070.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "3E2BE21B-7908-6FF2-1A75-0EEA8364DFD4",
							"path": "/Unclassified/max动画_20230202164113/sc001_071.mov",
							"entity": "sc001_071.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "49628E42-3FE1-633A-F239-374645A68C85",
							"path": "/Unclassified/max动画_20230202164113/sc001_072.mov",
							"entity": "sc001_072.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "1EDE93A0-96A1-36B4-68A4-947198285445",
							"path": "/Unclassified/max动画_20230202164113/sc001_073.mov",
							"entity": "sc001_073.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "71CD44BB-0598-3238-E0FE-F53CDFA75263",
							"path": "/Unclassified/max动画_20230202164113/sc001_074.mov",
							"entity": "sc001_074.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "1E53FF0A-59D3-22AD-34BD-4FF3AD53D98F",
							"path": "/Unclassified/max动画_20230202164113/sc001_075.mov",
							"entity": "sc001_075.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "B05FB268-F0BB-0B4E-35D9-A25EFD6A6F2B",
							"path": "/Unclassified/max动画_20230202164113/sc001_076.mov",
							"entity": "sc001_076.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "40EDBE1E-C172-AF87-80CD-D54F0BFCA949",
							"path": "/Unclassified/max动画_20230202164113/sc001_077.mov",
							"entity": "sc001_077.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "630ADEDB-E507-8EF3-421B-4CD7DEFDDA46",
							"path": "/Unclassified/max动画_20230202164113/sc001_078.mov",
							"entity": "sc001_078.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "FB9F573C-838B-760F-4528-1A7327B1F65B",
							"path": "/Unclassified/max动画_20230202164113/sc001_079.mov",
							"entity": "sc001_079.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "B6788BEC-2BBE-1C0E-76CF-9EB4FC258DDF",
							"path": "/Unclassified/max动画_20230202164113/sc001_080.mov",
							"entity": "sc001_080.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "5E46EC9D-33AE-DC05-FA75-6C7AD379BE80",
							"path": "/Unclassified/max动画_20230202164113/sc001_081.mov",
							"entity": "sc001_081.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "5463BA64-A5C0-0F7F-BAEB-B1A5EAC88E67",
							"path": "/Unclassified/max动画_20230202164113/sc001_082.mov",
							"entity": "sc001_082.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "A6E3B9D1-6B54-A2CC-BFAD-5740F87ECFF0",
							"path": "/Unclassified/max动画_20230202164113/sc001_083.mov",
							"entity": "sc001_083.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "F962883B-7CDB-10CF-3D22-03E5B4927D76",
							"path": "/Unclassified/max动画_20230202164113/sc001_084.mov",
							"entity": "sc001_084.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "ED9B0CDD-9D36-D6E6-B7FB-E0292DDCF047",
							"path": "/Unclassified/max动画_20230202164113/sc001_085.mov",
							"entity": "sc001_085.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "EDFBF152-A577-F5E0-64C0-CE37B1556FDF",
							"path": "/Unclassified/max动画_20230202164113/sc001_086.mov",
							"entity": "sc001_086.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "9A5537C9-C110-4B0C-78DB-98E1C725E7CA",
							"path": "/Unclassified/max动画_20230202164113/sc001_087.mov",
							"entity": "sc001_087.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "C79508E7-9783-3F4E-E9B0-B6343CDA177F",
							"path": "/Unclassified/max动画_20230202164113/sc001_088.mov",
							"entity": "sc001_088.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "A3B6035A-F396-3CEA-3264-05072FFFFEDD",
							"path": "/Unclassified/max动画_20230202164113/sc001_089.mov",
							"entity": "sc001_089.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "CBB0FE3B-49C7-B282-DCE1-DD96CB73F075",
							"path": "/Unclassified/max动画_20230202164113/sc001_090.mov",
							"entity": "sc001_090.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "D7D7FD3A-E935-88A5-4960-ABB7416F1A9F",
							"path": "/Unclassified/max动画_20230202164113/sc001_091.mov",
							"entity": "sc001_091.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "1110AEFA-2AE6-1E9C-7DAD-452043897767",
							"path": "/Unclassified/max动画_20230202164113/sc001_092.mov",
							"entity": "sc001_092.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "A023AC6E-101A-0DBE-46DA-99532E22EBC6",
							"path": "/Unclassified/max动画_20230202164113/sc001_093.mov",
							"entity": "sc001_093.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "F6772602-AD8F-E497-64CB-3B3E185F133D",
							"path": "/Unclassified/max动画_20230202164113/sc001_094.mov",
							"entity": "sc001_094.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "F210E0BD-3EE6-BDA7-F912-8F6F1C7D9750",
							"path": "/Unclassified/max动画_20230202164113/sc001_095.mov",
							"entity": "sc001_095.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "054C3F93-354D-8BD5-7CE4-5ABD1BF77FA4",
							"path": "/Unclassified/max动画_20230202164113/sc001_096.mov",
							"entity": "sc001_096.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "EC8DCF3C-CF0F-CC7E-6754-DFDE918FCCC5",
							"path": "/Unclassified/max动画_20230202164113/sc001_097.mov",
							"entity": "sc001_097.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "BDA4EF70-CE90-34D4-F850-52FB1E4B3F3C",
							"path": "/Unclassified/max动画_20230202164113/sc001_098.mov",
							"entity": "sc001_098.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						},
						{
							"id": "4C3D39B9-621D-CE25-B4A4-9468044952FC",
							"path": "/Unclassified/max动画_20230202164113/sc001_099.mov",
							"entity": "sc001_099.mov",
							"type": "asset",
							"parent_id": "7BD30D20-8A9D-2576-EEB9-DB649B260E37"
						}
					]
				},
				{
					"id": "3C11F6D4-E2BD-AF77-6A34-E7514F9A9E63",
					"path": "/Unclassified/未命名",
					"entity": "未命名",
					"type": "tree",
					"parent_id": "DD44F9AB-B47F-F58D-BF8D-D4E21E64EF1B"
				}
			]
		},
		{
			"id": "80E1BAA7-BDFB-E5A5-546A-603CE36B746B",
			"path": "/xiaoying",
			"entity": "xiaoying",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "5146291B-0353-EAC7-F37F-3B04668ADB9A",
					"path": "/xiaoying/max动画",
					"entity": "max动画",
					"type": "tree",
					"parent_id": "80E1BAA7-BDFB-E5A5-546A-603CE36B746B",
					"child": [
						{
							"id": "3BF29407-7F72-3907-FBAA-BB0AA1D8EC06",
							"path": "/xiaoying/max动画/sc001_001.mov",
							"entity": "sc001_001.mov",
							"type": "asset",
							"parent_id": "5146291B-0353-EAC7-F37F-3B04668ADB9A"
						},
						{
							"id": "A835FD3D-371F-6A01-FB55-7EE6E1A07165",
							"path": "/xiaoying/max动画/sc001_002.mov",
							"entity": "sc001_002.mov",
							"type": "asset",
							"parent_id": "5146291B-0353-EAC7-F37F-3B04668ADB9A"
						},
						{
							"id": "FFDCA600-A351-856C-917E-6AB9B9C7F7A4",
							"path": "/xiaoying/max动画/sc001_003.mov",
							"entity": "sc001_003.mov",
							"type": "asset",
							"parent_id": "5146291B-0353-EAC7-F37F-3B04668ADB9A"
						},
						{
							"id": "19190E4E-D667-185B-11CC-D297E1079320",
							"path": "/xiaoying/max动画/sc001_004.mov",
							"entity": "sc001_004.mov",
							"type": "asset",
							"parent_id": "5146291B-0353-EAC7-F37F-3B04668ADB9A"
						},
						{
							"id": "9D8D8C59-20C7-05CF-FBC1-903241BB00B6",
							"path": "/xiaoying/max动画/sc001_005.mov",
							"entity": "sc001_005.mov",
							"type": "asset",
							"parent_id": "5146291B-0353-EAC7-F37F-3B04668ADB9A"
						},
						{
							"id": "2BD0EA7C-7117-B4F2-865F-A699C18A0069",
							"path": "/xiaoying/max动画/sc001_006.mov",
							"entity": "sc001_006.mov",
							"type": "asset",
							"parent_id": "5146291B-0353-EAC7-F37F-3B04668ADB9A"
						},
						{
							"id": "B0D5BF67-5C62-CDD1-E227-CBC0A80902F5",
							"path": "/xiaoying/max动画/sc001_007.mov",
							"entity": "sc001_007.mov",
							"type": "asset",
							"parent_id": "5146291B-0353-EAC7-F37F-3B04668ADB9A"
						},
						{
							"id": "0AEFFF34-C420-3FE9-D55A-3D1483E9867B",
							"path": "/xiaoying/max动画/sc001_008.mov",
							"entity": "sc001_008.mov",
							"type": "asset",
							"parent_id": "5146291B-0353-EAC7-F37F-3B04668ADB9A"
						},
						{
							"id": "906234FA-B641-AD2D-3013-484B0FEA0098",
							"path": "/xiaoying/max动画/sc001_009.mov",
							"entity": "sc001_009.mov",
							"type": "asset",
							"parent_id": "5146291B-0353-EAC7-F37F-3B04668ADB9A"
						}
					]
				}
			]
		},
		{
			"id": "15D6FBE9-BF14-0FAE-039A-F6F21BF5FC3D",
			"path": "/xiaoying_20230202164649",
			"entity": "xiaoying_20230202164649",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E",
					"path": "/xiaoying_20230202164649/max动画",
					"entity": "max动画",
					"type": "tree",
					"parent_id": "15D6FBE9-BF14-0FAE-039A-F6F21BF5FC3D",
					"child": [
						{
							"id": "780516EA-DA11-FA30-965C-B0D1FA3362C5",
							"path": "/xiaoying_20230202164649/max动画/sc001_001.mov",
							"entity": "sc001_001.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "0408F940-07BF-8148-9702-56A8481E1512",
							"path": "/xiaoying_20230202164649/max动画/sc001_002.mov",
							"entity": "sc001_002.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "4C2EFDE9-AC6D-BE9D-21AE-45F9368855D8",
							"path": "/xiaoying_20230202164649/max动画/sc001_003.mov",
							"entity": "sc001_003.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "6AE0DBC3-3C29-2C19-116E-5E2E0A9E068C",
							"path": "/xiaoying_20230202164649/max动画/sc001_004.mov",
							"entity": "sc001_004.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "04388D71-81A0-12D7-4C5D-06958FE68C32",
							"path": "/xiaoying_20230202164649/max动画/sc001_005.mov",
							"entity": "sc001_005.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "CB3B787D-4F30-2A5C-5A63-3ABCD9095B1C",
							"path": "/xiaoying_20230202164649/max动画/sc001_006.mov",
							"entity": "sc001_006.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "BEDB20AD-F6A9-DDA0-5453-1441B6DD4567",
							"path": "/xiaoying_20230202164649/max动画/sc001_007.mov",
							"entity": "sc001_007.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "5956A8B7-5830-3D46-A48D-4DABF76A57FA",
							"path": "/xiaoying_20230202164649/max动画/sc001_008.mov",
							"entity": "sc001_008.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "3EC05EB9-CBD2-4429-09CE-B732BC4EA4F6",
							"path": "/xiaoying_20230202164649/max动画/sc001_009.mov",
							"entity": "sc001_009.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "472B58B9-618A-7F0F-3F6D-C7B735CF5103",
							"path": "/xiaoying_20230202164649/max动画/sc001_010.mov",
							"entity": "sc001_010.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "8DD9674D-877E-3EAC-0C73-397E9E74EC07",
							"path": "/xiaoying_20230202164649/max动画/sc001_011.mov",
							"entity": "sc001_011.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "61732325-D2A1-2EE7-462D-AD3FDBB7083E",
							"path": "/xiaoying_20230202164649/max动画/sc001_012.mov",
							"entity": "sc001_012.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "7349CCC5-3216-93D2-CF27-177F8FC46F98",
							"path": "/xiaoying_20230202164649/max动画/sc001_013.mov",
							"entity": "sc001_013.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "49625AFA-6484-672C-DD58-70B8FAC450D2",
							"path": "/xiaoying_20230202164649/max动画/sc001_014.mov",
							"entity": "sc001_014.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "12B03AFA-4EBB-00C4-C48C-72330CCC4492",
							"path": "/xiaoying_20230202164649/max动画/sc001_015.mov",
							"entity": "sc001_015.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "27A3800B-667E-B9A9-B579-8CA9CF990060",
							"path": "/xiaoying_20230202164649/max动画/sc001_016.mov",
							"entity": "sc001_016.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "49770473-C58B-732B-B6E8-D357BF2691FF",
							"path": "/xiaoying_20230202164649/max动画/sc001_017.mov",
							"entity": "sc001_017.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "EE829B77-58C7-E2DF-0C95-A2BA2ABB75AD",
							"path": "/xiaoying_20230202164649/max动画/sc001_018.mov",
							"entity": "sc001_018.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "8DB0D4C2-BC61-0483-5D24-265C42CE269A",
							"path": "/xiaoying_20230202164649/max动画/sc001_019.mov",
							"entity": "sc001_019.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "50F475C6-1D92-0DA3-26AE-2FD6EFBD9A0D",
							"path": "/xiaoying_20230202164649/max动画/sc001_020.mov",
							"entity": "sc001_020.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "F6E1A7F8-63D2-97F5-68A3-C4569B3F7291",
							"path": "/xiaoying_20230202164649/max动画/sc001_021.mov",
							"entity": "sc001_021.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "27903D4E-B40F-166B-5959-CACBCC48C9F2",
							"path": "/xiaoying_20230202164649/max动画/sc001_022.mov",
							"entity": "sc001_022.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "F982AB5F-46EA-7A1D-F91D-CF2840B20A1B",
							"path": "/xiaoying_20230202164649/max动画/sc001_023.mov",
							"entity": "sc001_023.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "C987D83C-5126-A1C9-36D7-A4163A78C923",
							"path": "/xiaoying_20230202164649/max动画/sc001_024.mov",
							"entity": "sc001_024.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "6D687D65-25DE-137E-55DE-E291E31F1F1B",
							"path": "/xiaoying_20230202164649/max动画/sc001_025.mov",
							"entity": "sc001_025.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "51769EC3-54E1-808C-D39B-F7DF75950CFA",
							"path": "/xiaoying_20230202164649/max动画/sc001_026.mov",
							"entity": "sc001_026.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "29171C88-3338-0939-12B4-B26AC53F52C6",
							"path": "/xiaoying_20230202164649/max动画/sc001_027.mov",
							"entity": "sc001_027.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "79E4E6C0-3A61-85F3-0BFA-716565089576",
							"path": "/xiaoying_20230202164649/max动画/sc001_028.mov",
							"entity": "sc001_028.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "703E16C7-599D-0447-BF64-9B30DB730539",
							"path": "/xiaoying_20230202164649/max动画/sc001_029.mov",
							"entity": "sc001_029.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "F4AF7255-2507-84E7-20B5-120C1441DDC2",
							"path": "/xiaoying_20230202164649/max动画/sc001_030.mov",
							"entity": "sc001_030.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "8B5DE88B-3F3E-DE8D-2DBB-AC9907A6B4CC",
							"path": "/xiaoying_20230202164649/max动画/sc001_031.mov",
							"entity": "sc001_031.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "6A37EB61-67B6-9F97-1BB6-73D4BD5BC300",
							"path": "/xiaoying_20230202164649/max动画/sc001_032.mov",
							"entity": "sc001_032.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "C51E4FD2-25AA-46F9-6941-324683A30A91",
							"path": "/xiaoying_20230202164649/max动画/sc001_033.mov",
							"entity": "sc001_033.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "43509659-D7FF-E56D-4FA0-ECE67CC1F3F5",
							"path": "/xiaoying_20230202164649/max动画/sc001_034.mov",
							"entity": "sc001_034.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "7BBD73F1-25DD-BBCE-DB41-33E9E564BC69",
							"path": "/xiaoying_20230202164649/max动画/sc001_035.mov",
							"entity": "sc001_035.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "056D329C-4B40-8D29-1448-3CAC9C41ABEE",
							"path": "/xiaoying_20230202164649/max动画/sc001_036.mov",
							"entity": "sc001_036.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "DD336BE9-586C-A18C-205E-FE012F18CA4B",
							"path": "/xiaoying_20230202164649/max动画/sc001_037.mov",
							"entity": "sc001_037.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "0D41D1A7-9DD0-7848-89C5-1477D6AEA2DF",
							"path": "/xiaoying_20230202164649/max动画/sc001_038.mov",
							"entity": "sc001_038.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "2D642B02-822A-FE6D-6B29-8416BF518C7E",
							"path": "/xiaoying_20230202164649/max动画/sc001_039.mov",
							"entity": "sc001_039.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "2A4095DA-E336-4812-7BF8-54E8FE15ACF4",
							"path": "/xiaoying_20230202164649/max动画/sc001_040.mov",
							"entity": "sc001_040.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "BCE1022C-669E-7335-CE12-036A96D205E0",
							"path": "/xiaoying_20230202164649/max动画/sc001_041.mov",
							"entity": "sc001_041.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "081F07BE-05D2-EA37-6589-F06882A03C9D",
							"path": "/xiaoying_20230202164649/max动画/sc001_042.mov",
							"entity": "sc001_042.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "CA96A79C-9D2F-508B-E219-E8AC8F419254",
							"path": "/xiaoying_20230202164649/max动画/sc001_043.mov",
							"entity": "sc001_043.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "79DD051B-6690-ABC7-91F0-42E65E6EC51B",
							"path": "/xiaoying_20230202164649/max动画/sc001_044.mov",
							"entity": "sc001_044.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "CA267216-50E7-31D4-C0C2-4D5FA953A342",
							"path": "/xiaoying_20230202164649/max动画/sc001_045.mov",
							"entity": "sc001_045.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "4D6B1871-5812-F679-4727-B15A8D07AA1E",
							"path": "/xiaoying_20230202164649/max动画/sc001_046.mov",
							"entity": "sc001_046.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "BC5B51B6-EC5C-0AEE-E7A5-115CA8DA527E",
							"path": "/xiaoying_20230202164649/max动画/sc001_047.mov",
							"entity": "sc001_047.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "09174F45-E000-673B-ECC5-CFAB872FA8B7",
							"path": "/xiaoying_20230202164649/max动画/sc001_048.mov",
							"entity": "sc001_048.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "0E96807C-DD8C-6646-090F-7FD10C3D3D0C",
							"path": "/xiaoying_20230202164649/max动画/sc001_049.mov",
							"entity": "sc001_049.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "6D299DE0-3D86-FF3D-CC0A-8DBFE69778E9",
							"path": "/xiaoying_20230202164649/max动画/sc001_050.mov",
							"entity": "sc001_050.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "897D70D2-00A7-7366-624F-765F00CC9BD2",
							"path": "/xiaoying_20230202164649/max动画/sc001_064.mov",
							"entity": "sc001_064.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "29CE3EE6-19F6-943C-EA47-4E588BE869FD",
							"path": "/xiaoying_20230202164649/max动画/sc001_065.mov",
							"entity": "sc001_065.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "B5B5B3DD-110D-6139-8D89-2821B45F26C7",
							"path": "/xiaoying_20230202164649/max动画/sc001_066.mov",
							"entity": "sc001_066.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "11D394D4-A934-12F5-90E1-BC1E8E5C2616",
							"path": "/xiaoying_20230202164649/max动画/sc001_067.mov",
							"entity": "sc001_067.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "08DB9C7B-A361-0C18-583D-C332CCC67DE4",
							"path": "/xiaoying_20230202164649/max动画/sc001_068.mov",
							"entity": "sc001_068.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "1D709800-F97B-5E26-D139-0B85C6AD7927",
							"path": "/xiaoying_20230202164649/max动画/sc001_068.mov",
							"entity": "sc001_068.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "C86D8FCF-4F4A-BF91-B4D7-5D9295BD8AA2",
							"path": "/xiaoying_20230202164649/max动画/sc001_069.mov",
							"entity": "sc001_069.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "6E4EEB2C-B85E-65E6-653F-BCF7452618AE",
							"path": "/xiaoying_20230202164649/max动画/sc001_069.mov",
							"entity": "sc001_069.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "4D7F8AC6-2C1A-0ACD-78D6-4EABDEA66E3C",
							"path": "/xiaoying_20230202164649/max动画/sc001_070.mov",
							"entity": "sc001_070.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "A99C0D03-97B3-30CB-5A60-C19A4FF5DDF4",
							"path": "/xiaoying_20230202164649/max动画/sc001_070.mov",
							"entity": "sc001_070.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "F5D60894-8DFD-67FF-E35A-694CE7E4720C",
							"path": "/xiaoying_20230202164649/max动画/sc001_071.mov",
							"entity": "sc001_071.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "A2DC9B33-2CF7-5829-3A5F-79F0B2157D93",
							"path": "/xiaoying_20230202164649/max动画/sc001_072.mov",
							"entity": "sc001_072.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "9B2A5148-A717-1063-8146-615988FFE4FA",
							"path": "/xiaoying_20230202164649/max动画/sc001_073.mov",
							"entity": "sc001_073.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "EFBFCB55-CBAE-8355-E8D7-BFA6793DD43C",
							"path": "/xiaoying_20230202164649/max动画/sc001_074.mov",
							"entity": "sc001_074.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "0CDF0155-E90F-EB40-937B-31F0E4D005C3",
							"path": "/xiaoying_20230202164649/max动画/sc001_075.mov",
							"entity": "sc001_075.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "06E0C261-3436-6357-BE0C-342A0AADD1F8",
							"path": "/xiaoying_20230202164649/max动画/sc001_076.mov",
							"entity": "sc001_076.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "821674A8-9ED3-677C-5658-31D8BDE10BA5",
							"path": "/xiaoying_20230202164649/max动画/sc001_077.mov",
							"entity": "sc001_077.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "A0FFE80A-B4E7-C0B8-AAA3-8F37806888A4",
							"path": "/xiaoying_20230202164649/max动画/sc001_078.mov",
							"entity": "sc001_078.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "BF288A57-1E33-D885-C1CB-529BB3C9CA25",
							"path": "/xiaoying_20230202164649/max动画/sc001_079.mov",
							"entity": "sc001_079.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "305F3C38-4EB7-A00A-06D9-5A96161D4AF2",
							"path": "/xiaoying_20230202164649/max动画/sc001_080.mov",
							"entity": "sc001_080.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "ACB0B2F0-ADAD-022D-1BBF-589936A78F9F",
							"path": "/xiaoying_20230202164649/max动画/sc001_081.mov",
							"entity": "sc001_081.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "9BA68D73-FECC-D62B-35FC-8BAECA51DC74",
							"path": "/xiaoying_20230202164649/max动画/sc001_082.mov",
							"entity": "sc001_082.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "139275C0-C105-2914-5612-3844D81BC2D9",
							"path": "/xiaoying_20230202164649/max动画/sc001_083.mov",
							"entity": "sc001_083.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "4A10131B-7004-6AA1-06E6-E6DCDB5C17C5",
							"path": "/xiaoying_20230202164649/max动画/sc001_084.mov",
							"entity": "sc001_084.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "71639384-4BFE-08C6-22D0-34EF209A161D",
							"path": "/xiaoying_20230202164649/max动画/sc001_085.mov",
							"entity": "sc001_085.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "83E4ECCD-FDDF-58C6-8255-FDECDBA96ACF",
							"path": "/xiaoying_20230202164649/max动画/sc001_086.mov",
							"entity": "sc001_086.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "5FB856C1-FA0C-B6FE-011B-B0CAFDFBCB79",
							"path": "/xiaoying_20230202164649/max动画/sc001_087.mov",
							"entity": "sc001_087.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "A324BE72-E07D-709E-3542-F61E28D34BC2",
							"path": "/xiaoying_20230202164649/max动画/sc001_088.mov",
							"entity": "sc001_088.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "D4FA9B43-BFDA-4058-1679-080CB67331DC",
							"path": "/xiaoying_20230202164649/max动画/sc001_089.mov",
							"entity": "sc001_089.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "9BBA52D8-8350-3A85-1C7C-533FD89522C0",
							"path": "/xiaoying_20230202164649/max动画/sc001_090.mov",
							"entity": "sc001_090.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "35267E3A-6659-58BB-0BFD-2B6557DD81C0",
							"path": "/xiaoying_20230202164649/max动画/sc001_091.mov",
							"entity": "sc001_091.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "0DFCDC34-3277-E9FA-FD5F-0971742B3FDA",
							"path": "/xiaoying_20230202164649/max动画/sc001_092.mov",
							"entity": "sc001_092.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "9DB8BD26-4CB2-56BD-617F-C679D236EAAF",
							"path": "/xiaoying_20230202164649/max动画/sc001_093.mov",
							"entity": "sc001_093.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "E317F8EB-0A62-2835-C6F7-961FD8388A20",
							"path": "/xiaoying_20230202164649/max动画/sc001_094.mov",
							"entity": "sc001_094.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "D990319A-EEB3-8C39-521A-76DDC16693FA",
							"path": "/xiaoying_20230202164649/max动画/sc001_095.mov",
							"entity": "sc001_095.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "2C9AF85B-99AC-C9BD-EEC9-2F11666BE53C",
							"path": "/xiaoying_20230202164649/max动画/sc001_096.mov",
							"entity": "sc001_096.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "5B973D48-3862-FBED-82B6-27ABDC39A8B6",
							"path": "/xiaoying_20230202164649/max动画/sc001_097.mov",
							"entity": "sc001_097.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "15466A5F-2B28-D7D1-F3AF-B7525887FDAE",
							"path": "/xiaoying_20230202164649/max动画/sc001_098.mov",
							"entity": "sc001_098.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						},
						{
							"id": "603DA5E6-4954-E9E3-BFAA-20B1703A42AA",
							"path": "/xiaoying_20230202164649/max动画/sc001_099.mov",
							"entity": "sc001_099.mov",
							"type": "asset",
							"parent_id": "46FBB27E-D8D0-3F2F-7640-D35237EE726E"
						}
					]
				}
			]
		},
		{
			"id": "447D8B91-FA2C-D360-093A-3FEA25584292",
			"path": "/xiaoying_20230202164649",
			"entity": "xiaoying_20230202164649",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "A362CC1E-3FDD-CA63-30B0-ECEF55B9276E",
					"path": "/xiaoying_20230202164649/max动画",
					"entity": "max动画",
					"type": "tree",
					"parent_id": "447D8B91-FA2C-D360-093A-3FEA25584292",
					"child": [
						{
							"id": "98AEB577-A684-B0EA-85FD-586E395CF145",
							"path": "/xiaoying_20230202164649/max动画/sc001_001.mov",
							"entity": "sc001_001.mov",
							"type": "asset",
							"parent_id": "A362CC1E-3FDD-CA63-30B0-ECEF55B9276E"
						},
						{
							"id": "28B1680E-548C-E7CF-D503-0315F47E0977",
							"path": "/xiaoying_20230202164649/max动画/sc001_002.mov",
							"entity": "sc001_002.mov",
							"type": "asset",
							"parent_id": "A362CC1E-3FDD-CA63-30B0-ECEF55B9276E"
						},
						{
							"id": "F6858EBA-6CEB-1D4B-F223-9608DD162B38",
							"path": "/xiaoying_20230202164649/max动画/sc001_003.mov",
							"entity": "sc001_003.mov",
							"type": "asset",
							"parent_id": "A362CC1E-3FDD-CA63-30B0-ECEF55B9276E"
						},
						{
							"id": "2100D9C7-A024-CE20-85C8-1C32CB5FBCFE",
							"path": "/xiaoying_20230202164649/max动画/sc001_004.mov",
							"entity": "sc001_004.mov",
							"type": "asset",
							"parent_id": "A362CC1E-3FDD-CA63-30B0-ECEF55B9276E"
						},
						{
							"id": "4E0291D5-4E2E-001A-2874-1E986C0DFCE0",
							"path": "/xiaoying_20230202164649/max动画/sc001_005.mov",
							"entity": "sc001_005.mov",
							"type": "asset",
							"parent_id": "A362CC1E-3FDD-CA63-30B0-ECEF55B9276E"
						},
						{
							"id": "E06976A0-8D27-A228-EE82-8C9DCAF2D4BA",
							"path": "/xiaoying_20230202164649/max动画/sc001_006.mov",
							"entity": "sc001_006.mov",
							"type": "asset",
							"parent_id": "A362CC1E-3FDD-CA63-30B0-ECEF55B9276E"
						},
						{
							"id": "BF384866-3396-B08F-8CE0-3785C8E9A1E8",
							"path": "/xiaoying_20230202164649/max动画/sc001_007.mov",
							"entity": "sc001_007.mov",
							"type": "asset",
							"parent_id": "A362CC1E-3FDD-CA63-30B0-ECEF55B9276E"
						},
						{
							"id": "EDB854E3-B9A1-D434-5E40-BDED81F29CEC",
							"path": "/xiaoying_20230202164649/max动画/sc001_008.mov",
							"entity": "sc001_008.mov",
							"type": "asset",
							"parent_id": "A362CC1E-3FDD-CA63-30B0-ECEF55B9276E"
						},
						{
							"id": "3FE9A483-9F9C-ECE3-12E8-F9B987985A41",
							"path": "/xiaoying_20230202164649/max动画/sc001_009.mov",
							"entity": "sc001_009.mov",
							"type": "asset",
							"parent_id": "A362CC1E-3FDD-CA63-30B0-ECEF55B9276E"
						}
					]
				}
			]
		},
		{
			"id": "5E65DACC-C72A-C143-49E1-4644A5D7BF59",
			"path": "/未命名",
			"entity": "未命名",
			"type": "tree",
			"parent_id": ""
		},
		{
			"id": "6B2E4EB3-7B99-400F-AC75-8CD361BA253C",
			"path": "/未命名",
			"entity": "未命名",
			"type": "tree",
			"parent_id": ""
		},
		{
			"id": "F695E7B9-4DE1-98FA-2FDD-B487F2CB89FC",
			"path": "/未命名1",
			"entity": "未命名1",
			"type": "tree",
			"parent_id": ""
		},
		{
			"id": "69CE1A4B-F30E-74A2-EC17-3673F51F4AEC",
			"path": "/未命名2",
			"entity": "未命名2",
			"type": "tree",
			"parent_id": ""
		},
		{
			"id": "CDF75B68-B65C-4DAE-13CF-633AD6CEA695",
			"path": "/未命名3",
			"entity": "未命名3",
			"type": "tree",
			"parent_id": ""
		},
		{
			"id": "B90AB4F9-7223-7F42-472F-19EAD16970C1",
			"path": "/未命名4",
			"entity": "未命名4",
			"type": "tree",
			"parent_id": ""
		},
		{
			"id": "729D20D2-9859-5253-CB15-012BF8C20090",
			"path": "/未命名5",
			"entity": "未命名5",
			"type": "tree",
			"parent_id": ""
		},
		{
			"id": "6183107C-314F-664E-7E10-EBD74133E042",
			"path": "/未命名6",
			"entity": "未命名6",
			"type": "tree",
			"parent_id": ""
		},
		{
			"id": "78D8C0C1-ECC4-CF43-B37C-1EE74B03BAEA",
			"path": "/未命名6_20230202164649",
			"entity": "未命名6_20230202164649",
			"type": "tree",
			"parent_id": ""
		},
		{
			"id": "A48FE769-A5AD-D4D4-4323-60E44A0217F1",
			"path": "/测试分类",
			"entity": "测试分类",
			"type": "tree",
			"parent_id": "",
			"child": [
				{
					"id": "06E45016-1FC3-FFE7-5BF2-E0F3575EDB01",
					"path": "/测试分类/11",
					"entity": "11",
					"type": "asset",
					"parent_id": "A48FE769-A5AD-D4D4-4323-60E44A0217F1",
					"child": [
						{
							"id": "B8DAC57D-4D67-E939-465B-4AF4D7C878C3",
							"path": "/测试分类/11/assetlib_reference",
							"entity": "assetlib_reference",
							"type": "asset",
							"parent_id": "06E45016-1FC3-FFE7-5BF2-E0F3575EDB01"
						},
						{
							"id": "34AEB44B-0A4E-8700-DE55-E571E5AEFEEB",
							"path": "/测试分类/11/clipboard.js-master",
							"entity": "clipboard.js-master",
							"type": "asset",
							"parent_id": "06E45016-1FC3-FFE7-5BF2-E0F3575EDB01"
						},
						{
							"id": "64F0BC88-1AA6-A1DB-5E57-E4D6CD7F80B0",
							"path": "/测试分类/11/copy",
							"entity": "copy",
							"type": "asset",
							"parent_id": "06E45016-1FC3-FFE7-5BF2-E0F3575EDB01"
						},
						{
							"id": "4F1F4B75-12AD-9CA9-0AD4-BB5A053C5628",
							"path": "/测试分类/11/document",
							"entity": "document",
							"type": "asset",
							"parent_id": "06E45016-1FC3-FFE7-5BF2-E0F3575EDB01"
						},
						{
							"id": "78116E45-B5DB-1A63-738D-962BD52EFF3A",
							"path": "/测试分类/11/download",
							"entity": "download",
							"type": "asset",
							"parent_id": "06E45016-1FC3-FFE7-5BF2-E0F3575EDB01"
						}
					]
				}
			]
		}
	]
}
```
## /cgtw7.0/media_file
```text
网盘
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/media_file/get_filebox_bulk_download_data
```text
获取下载文件信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | get_filebox_bulk_download_data | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[os] | mac | String | 是 | 系统平台
data[is_all] | Y | String | 是 | Y/N
data[filebox_id] | {{task_asset_filebox_id}} | String | 是 | 文件框Id
data[task_id_array][] | {{task_asset_id}} | Array | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"current_folder_id": "30FEE35C-C9C9-FE19-3197-C276B069F28B",
			"data_list": [
				{
					"id": "E90EBB3F-1CC5-36C4-53B8-24F955CAE443",
					"name": "cat001_002.tiff",
					"is_folder": "N",
					"is_move": "N",
					"modify_time": "2019-03-19 10:21:30",
					"version": "002"
				},
				{
					"id": "7CDEC591-A029-919B-E3D0-2FA94B1007AB",
					"name": "cat001_003.tga",
					"is_folder": "N",
					"is_move": "N",
					"modify_time": "2020-04-27 13:09:34",
					"version": "003"
				}
			],
			"des_dir": "/tmp/xiaoying/Asset/Chars/cat001/Design/file_ver",
			"server": "/tmp/",
			"filebox_data": {
				"path": "/tmp/xiaoying/Asset/Chars/cat001/Design/file_ver",
				"move_to_history": "N",
				"is_in_history_add_version": "N",
				"is_in_history_add_datetime": "N",
				"is_version": "Y",
				"version_type": "file"
			},
			"task_id": "FCDB2F54-66D1-866B-E9FE-D3E7625DAD88"
		}
	]
}
```
## /cgtw7.0/media_file/bulk_download
```text
获取下载文件信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | bulk_download | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[id_array][] | 3056B5A7-627E-74F8-50B4-D94892E9D3A6 | String | 是 | ID列表
data[folder_id_array][] | E3A633BF-FB9B-70BF-7845-2076F593D6B1 | String | 是 | -
data[current_folder_id] | E3A633BF-FB9B-70BF-7845-2076F593D6B1 | String | 是 | -
data[language] | en | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"current_folder_id": "30FEE35C-C9C9-FE19-3197-C276B069F28B",
			"data_list": [
				{
					"id": "E90EBB3F-1CC5-36C4-53B8-24F955CAE443",
					"name": "cat001_002.tiff",
					"is_folder": "N",
					"is_move": "N",
					"modify_time": "2019-03-19 10:21:30",
					"version": "002"
				},
				{
					"id": "7CDEC591-A029-919B-E3D0-2FA94B1007AB",
					"name": "cat001_003.tga",
					"is_folder": "N",
					"is_move": "N",
					"modify_time": "2020-04-27 13:09:34",
					"version": "003"
				}
			],
			"des_dir": "/tmp/xiaoying/Asset/Chars/cat001/Design/file_ver",
			"server": "/tmp/",
			"filebox_data": {
				"path": "/tmp/xiaoying/Asset/Chars/cat001/Design/file_ver",
				"move_to_history": "N",
				"is_in_history_add_version": "N",
				"is_in_history_add_datetime": "N",
				"is_version": "Y",
				"version_type": "file"
			},
			"task_id": "FCDB2F54-66D1-866B-E9FE-D3E7625DAD88"
		}
	]
}
```
## /cgtw7.0/media_file/create_path_and_get_folder_id
```text
在media_folder中创建记录,并取回folder_id
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | create_path_and_get_folder_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[path] | /xiaoying/Shot/Layout/ep001/eq002_sc001_b/check | String | 是 | 目录路径
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "47E1C25B-D4D6-D4F0-1A02-FE6387CA865D"
}
```
## /cgtw7.0/media_file/exist_file
```text
检查文件是否在服务器
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | exist_file | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[file_name] | 11.py | String | 是 | 文件名,如sc001.mp4
data[folder_id] | 47E1C25B-D4D6-D4F0-1A02-FE6387CA865D | String | 是 | 目录ID
data[md5] | 2c35d00994fde2a7b71c147c772d02fd | String | 是 | 文件md5
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"is_exist_data": "Y",
		"is_exist_convert_data": "N",
		"md5_path": "/upload/proj_xiaoying/00000000/2c35d00994fde2a7b71c147c772d02fd.py",
		"convert_md5_path": "",
		"id": "1E64D25C-98AA-1FCD-55A0-344B79842362",
		"base_id": "55CDCE3D-FC24-AED0-CA65-2DA553DCF467",
		"convert_image": [],
		"store_type": ""
	}
}
```
## /cgtw7.0/media_file/upload
```text
文件已经在服务器上。这个时候则需要插入数据
不存在数据时使用
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | upload | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[path] | /xiaoying/Shot/Layout/ep001/eq002_sc001_b/check | String | 是 | 目录路径
data[file_name] | - | String | 是 | 文件名,如sc001.mp4
data[folder_id] | - | String | 是 | 目录ID
data[md5] | - | String | 是 | 文件md5
data[md5_path] | - | String | 是 | -
data[sys_size] | - | String | 是 | -
data[sys_modify_time] | - | String | 是 | -
data[is_convert_format] | - | String | 是 | -
data[meta_data_array][task_id] | - | String | 是 | -
data[meta_data_array][module] | - | String | 是 | -
data[meta_data_array][module_type] | - | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "47E1C25B-D4D6-D4F0-1A02-FE6387CA865D"
}
```
## /cgtw7.0/media_file/update_file_modify_time
```text
文件已经在服务器上。数据也存在的情况,
更改文件修改时间
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | update_file_modify_time | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[file_name] | 11.py | String | 是 | 文件名,如sc001.mp4
data[folder_id] | 47E1C25B-D4D6-D4F0-1A02-FE6387CA865D | String | 是 | 目录ID
data[md5] | 2c35d00994fde2a7b71c147c772d02fd | String | 是 | 文件md5
data[file_modify_time] | 2022-10-19 16:24:51 | String | 是 | 文件修改时间
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/media_file/get_online_file_path_array
```text
获取在线文件对应信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | get_online_file_path_array | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[path_array][] | /xiaoying/Shot/Layout/ep001/eq002_sc001_b/check/11.py | Array | 是 | 网盘路径列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "1E64D25C-98AA-1FCD-55A0-344B79842362",
			"path": "/xiaoying/Shot/Layout/ep001/eq002_sc001_b/check/11.py",
			"size": "71122",
			"modify_time": "2022-10-19 16:24:51",
			"md5": "2c35d00994fde2a7b71c147c772d02fd"
		}
	]
}
```
## /cgtw7.0/media_file/get_online_file_with_filter
```text
获取在线文件对应信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | get_online_file_with_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[filter_array][0][] | file.sys_create_time | Array | 是 | 过滤语句列表
data[filter_array][0][] | > | Array | 是 | 过滤语句列表
data[filter_array][0][] | 2023-02-20 | Array | 是 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "7CDEC591-A029-919B-E3D0-2FA94B1007AB",
			"name": "cat001_003.tga",
			"path": "/xiaoying/Asset/Chars/cat001/Design/file_ver/cat001_003.tga",
			"size": "388771",
			"modify_time": "2020-04-27 13:09:34",
			"md5": "0d83731b88b64093d26748b98b02624c"
		},
		{
			"id": "7ED73D1A-D31A-D0DC-86AE-C3D64A7B16C3",
			"name": "ep005_sc003_013.mov",
			"path": "/xiaoying/Shot/Layout/ep005/sc003/check/ep005_sc003_013.mov",
			"size": "44580110",
			"modify_time": "2018-10-25 19:07:38",
			"md5": "f859214b0a0f91a7604fff846ebe5ef5"
		},
		{
			"id": "BF284A48-FF30-5025-A9B8-5CD976A4EFDD",
			"name": "ep005_sc003_015.mov",
			"path": "/xiaoying/Shot/Layout/ep005/sc003/check/ep005_sc003_015.mov",
			"size": "44580110",
			"modify_time": "2018-10-25 19:07:38",
			"md5": "f859214b0a0f91a7604fff846ebe5ef5"
		},
		{
			"id": "443F42A8-EF0D-ED8E-F917-CCB9309FD5BA",
			"name": "ep005_sc003_015.mp4",
			"path": "/xiaoying/Shot/Layout/ep005/sc003/check/mp4/ep005_sc003_015.mp4",
			"size": "3515967",
			"modify_time": "2023-02-20 10:27:50",
			"md5": "ddf6647f6545f0db4ace4547974a6207"
		},
		{
			"id": "434A21DF-9ACB-3B3B-61B6-E789BBD5C042",
			"name": "ct_file.py",
			"path": "/xiaoying/Shot/Layout/test_rv/sc002/check/sc002v([aa]@bb./7.0/ct_file.py",
			"size": "27804",
			"modify_time": "2023-01-18 16:18:53",
			"md5": "1320d79a21e837b65224aa5b6f78a05f"
		},
		{
			"id": "D2C6BD82-B7DA-9147-23C1-6484633E5C5B",
			"name": "ct_file.py",
			"path": "/xiaoying/Shot/Layout/test_rv/sc003/check/sc003v([aa]@bb./6.2/ct_file.py",
			"size": "26946",
			"modify_time": "2023-01-18 16:14:59",
			"md5": "c0ed5bb3e94fd4b7482da239f47a234e"
		},
		{
			"id": "1995B397-F69E-3113-076F-8833B1A3943D",
			"name": "file.zip",
			"path": "/xiaoying/Shot/Layout/test_rv/sc002/check/sc002v([aa]@bb./file.zip",
			"size": "10446",
			"modify_time": "2023-01-18 16:54:45",
			"md5": "dce87e83b989a7c9f626efe5b5d2c5b9"
		},
		{
			"id": "FA1ECC91-7D4B-D731-1D02-F6221384AA7C",
			"name": "file.zip",
			"path": "/xiaoying/Shot/Layout/test_rv/sc003/check/sc003v([aa]@bb./file.zip",
			"size": "10446",
			"modify_time": "2023-01-18 16:54:45",
			"md5": "dce87e83b989a7c9f626efe5b5d2c5b9"
		},
		{
			"id": "C0D19BD4-3473-FCA3-3C67-46B50AC12A68",
			"name": "ct_file.py",
			"path": "/xiaoying/Shot/Layout/test_rv/sc002/check/sc002v([aa]@bb./6.2/ct_file.py",
			"size": "26946",
			"modify_time": "2023-01-18 16:14:59",
			"md5": "c0ed5bb3e94fd4b7482da239f47a234e"
		},
		{
			"id": "5DE327D9-B3D0-DA64-98F2-9C95EB214CAB",
			"name": "ct_file.py",
			"path": "/xiaoying/Shot/Layout/test_rv/sc003/check/sc003v([aa]@bb./7.0/ct_file.py",
			"size": "27804",
			"modify_time": "2023-01-18 16:18:53",
			"md5": "1320d79a21e837b65224aa5b6f78a05f"
		},
		{
			"id": "7C0B69D2-D323-461C-283D-1A46A9E53C00",
			"name": "test_rv_sc003_009.mov",
			"path": "/xiaoying/Shot/Layout/test_rv/sc003/check/test_rv_sc003_009.mov",
			"size": "44580110",
			"modify_time": "2018-10-25 19:07:38",
			"md5": "f859214b0a0f91a7604fff846ebe5ef5"
		},
		{
			"id": "3BD75ACC-AAF9-956C-467C-A2A11F3345C3",
			"name": "test_rv_sc003_010.mp4",
			"path": "/xiaoying/Shot/Layout/test_rv/sc003/check/test_rv_sc003_010.mp4",
			"size": "21958569",
			"modify_time": "2019-04-27 18:52:10",
			"md5": "cb208bde30d454164c764e8ad337139d"
		},
		{
			"id": "F9CFC4D9-947D-0B8B-4426-B29BCE3E6F6F",
			"name": "test_rv_sc003_011.mp4",
			"path": "/xiaoying/Shot/Layout/test_rv/sc003/check/test_rv_sc003_011.mp4",
			"size": "21958569",
			"modify_time": "2019-04-27 18:52:10",
			"md5": "cb208bde30d454164c764e8ad337139d"
		},
		{
			"id": "F56368D7-6256-878B-F263-AC6C309B7D3C",
			"name": "sc003v([aa]@bb.mp4",
			"path": "/xiaoying/Shot/Layout/test_rv/sc003/check/sc003v([aa]@bb.mp4",
			"size": "21958569",
			"modify_time": "2019-04-27 18:52:10",
			"md5": "cb208bde30d454164c764e8ad337139d"
		},
		{
			"id": "69261128-09E6-CA4C-69A5-1345FD10953E",
			"name": "test_rv_sc003_012.mp4",
			"path": "/xiaoying/Shot/Layout/test_rv/sc003/check/test_rv_sc003_012.mp4",
			"size": "21958569",
			"modify_time": "2019-04-27 18:52:10",
			"md5": "cb208bde30d454164c764e8ad337139d"
		},
		{
			"id": "9807DA86-48C5-D35B-8A3D-BF9B30CFC1A0",
			"name": "test_rv_sc003_013.mp4",
			"path": "/xiaoying/Shot/Layout/test_rv/sc003/check/test_rv_sc003_013.mp4",
			"size": "21958569",
			"modify_time": "2019-04-27 18:52:10",
			"md5": "cb208bde30d454164c764e8ad337139d"
		},
		{
			"id": "125D9DD7-CD2C-2188-4F13-A76BD40E05F4",
			"name": "test_rv_sc003_014.mov",
			"path": "/xiaoying/Shot/Layout/test_rv/sc003/check/test_rv_sc003_014.mov",
			"size": "44580110",
			"modify_time": "2018-10-25 19:07:38",
			"md5": "f859214b0a0f91a7604fff846ebe5ef5"
		},
		{
			"id": "E90EBB3F-1CC5-36C4-53B8-24F955CAE443",
			"name": "cat001_002.tiff",
			"path": "/xiaoying/Asset/Chars/cat001/Design/file_ver/cat001_002.tiff",
			"size": "604378",
			"modify_time": "2019-03-19 10:21:30",
			"md5": "53fd16441f3df0eb82d07470b42d732a"
		}
	]
}
```
## /cgtw7.0/media_file/get_data_with_id
```text
根据目录ID获取数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | get_data_with_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[folder_id] | 47E1C25B-D4D6-D4F0-1A02-FE6387CA865D | String | 是 | 目录ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "A1EC5922-ADE0-2689-95A2-0EFEECDB283E",
			"name": "11.py",
			"create_by": "",
			"last_update_time": "",
			"is_folder": "Y",
			"md5": "",
			"web_exist": "Y"
		},
		{
			"id": "1E64D25C-98AA-1FCD-55A0-344B79842362",
			"name": "11.py",
			"create_by": "",
			"last_update_time": "",
			"is_folder": "N",
			"md5": "2c35d00994fde2a7b71c147c772d02fd",
			"web_exist": "Y"
		}
	]
}
```
## /cgtw7.0/media_file/create_folder
```text
创建目录
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | create_folder | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[p_id] | 47E1C25B-D4D6-D4F0-1A02-FE6387CA865D | String | 是 | 目录ID
data[name] | new_folder | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"exist": false,
		"data": [
			{
				"id": "A1EC5922-ADE0-2689-95A2-0EFEECDB283E",
				"name": "11.py",
				"create_by": "",
				"last_update_time": "",
				"is_folder": "Y",
				"md5": "",
				"web_exist": "Y"
			},
			{
				"id": "409C1763-DD44-E762-DE47-217D82D06657",
				"name": "new_folder",
				"create_by": "",
				"last_update_time": "",
				"is_folder": "Y",
				"md5": "",
				"web_exist": "Y"
			},
			{
				"id": "1E64D25C-98AA-1FCD-55A0-344B79842362",
				"name": "11.py",
				"create_by": "",
				"last_update_time": "",
				"is_folder": "N",
				"md5": "2c35d00994fde2a7b71c147c772d02fd",
				"web_exist": "Y"
			}
		]
	}
}
```
## /cgtw7.0/media_file/get_filebox_bulk_upload_data
```text
获取文件框上传数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | get_filebox_bulk_upload_data | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[task_id_array][] | {{task_asset_id}} | Array | 是 | 记录数据
data[filebox_id] | {{task_asset_filebox_id}} | String | 是 | 文件框ID
data[os] | mac | String | 是 | 系统平台
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"show_type": "Files and Folders",
		"filebox_data_list": [
			{
				"path": "/tmp/xiaoying/Asset/Chars/cat001/Design/file_ver",
				"rule": [
					"cat001_{ver}.*",
					"cat001_{ver}"
				],
				"server": "/tmp/",
				"task_id": "FCDB2F54-66D1-866B-E9FE-D3E7625DAD88",
				"title": "file_ver"
			}
		],
		"is_upload_online": "Y",
		"convert_type": []
	}
}
```
## /cgtw7.0/media_file/get_filter
```text
在media_folder中创建记录,并取回folder_id
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[field_array][] | path | String | 是 | 目录路径
data[filter_array][0][] | - | String | 是 | 字段标识列表
data[filter_array][0][] | - | String | 是 | 过滤语句列表
data[filter_array][0][] | - | String | 是 | 过滤语句列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
## /cgtw7.0/media_file/get_online_file_path_array
```text
在media_folder中创建记录,并取回folder_id
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | get_online_file_path_array | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[field_array][] | path | String | 是 | 目录路径
data[filter_array][0][] | - | String | 是 | 字段标识列表
data[filter_array][0][] | - | String | 是 | 过滤语句列表
data[filter_array][0][] | - | String | 是 | 过滤语句列表
data[path_array][0] | /xiaoying | String | 是 | 拖入插件时抄送链接文件问题-
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
## /cgtw7.0/media_file/search_folder
```text
在media_folder中创建记录,并取回folder_id
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | search_folder | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[dir] | /xiaoying | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
## /cgtw7.0/media_file/get_folder_modify_time
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | get_folder_modify_time | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[id_array][0] | 51EC9A65-6233-E94D-3366-AA6FC5889282 | String | 是 | ID列表
data[id_array][1] | 0F0F3619-58AB-1369-16FA-7B49E8800C66 | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
## /cgtw7.0/media_file/update_folder_modify_time
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | update_folder_modify_time | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | proj_xiaoying | String | 是 | 数据库
data[folder_data][/xiaoying/Shot/Layout/rv_123/sc001/work] | 2023-10-25 11:11:11 | String | 是 | ID列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
## /cgtw7.0/media_file/delete
```text
获取在线文件对应信息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_file | String | 是 | 控制器
data[method] | delete | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[file_array][] | /xiaoying/Shot/Layout/ep001/eq002_sc001_b/check/11.py | Array | 是 | 网盘路径列表
data[dir_array][] | - | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"id": "1E64D25C-98AA-1FCD-55A0-344B79842362",
			"path": "/xiaoying/Shot/Layout/ep001/eq002_sc001_b/check/11.py",
			"size": "71122",
			"modify_time": "2022-10-19 16:24:51",
			"md5": "2c35d00994fde2a7b71c147c772d02fd"
		}
	]
}
```
## /cgtw7.0/media_data
```text
暂无描述
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/media_data/get_convert_format
```text
取转码允许格式
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | media_data | String | 是 | 控制器
data[method] | get_convert_format | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
apt.globals.set("asset_lib_folder_id", response.json.data);
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": {
		"mov": [
			"avi",
			"mp4",
			"mov",
			"mxf",
			"m4v"
		],
		"image": [
			"jpg",
			"jpeg",
			"png",
			"exr",
			"tiff",
			"tif",
			"tga",
			"dpx",
			"psd",
			"bmp",
			"gif"
		]
	}
}
```
## /cgtw7.0/template
```text
模版
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/template/get_link_module
```text
查看模块关联父集
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | template | String | 是 | 控制器
data[method] | get_link_module | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "eps"
}
```
## /cgtw7.0/template/get_2many_module
```text
查看模块的关联模块列表
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | template | String | 是 | 控制器
data[method] | get_2many_module | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"asset",
		"cross_module"
	]
}
```
## /cgtw7.0/template/get_filter
```text
获取模板数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | template | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[field_array][] | entity | String | 是 | 数据库
data[filter_array] | - | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "2_电影",
			"#id": "B8FB9E8C-6CEA-8174-7833-65C750FED087"
		},
		{
			"entity": "演示模板",
			"#id": "19702160-203E-4062-8AB9-17316006AE7B"
		},
		{
			"entity": "A模板（简易流程）",
			"#id": "827DA74D-9D58-4F09-8E4C-A78C7F98A5FE"
		},
		{
			"entity": "1_剧集",
			"#id": "3902ADA0-95ED-4D6B-B063-851A0E31C2FE"
		},
		{
			"entity": "李白",
			"#id": "E62BA9E7-BA6E-49FB-9606-849F07D11B6F"
		},
		{
			"entity": "公共模板",
			"#id": "AB400EBB-25C8-B7E1-57BA-617C7E2FADEA"
		}
	]
}
```
## /cgtw7.0/module
```text
模块
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/module/get
```text
获取模块数据

field可选
en_name 英文名
module_str 中文名
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | module | String | 是 | 控制器
data[method] | get | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[module] | shot | String | 是 | 模块标识
data[field] | module_str | String | 是 | -
data[field_array] | - | String | 是 | 字段标识列表
data[language] | en | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "镜头"
}
```
## /cgtw7.0/module/get_filter
```text
获取模块数据

field可选
en_name 英文名
module_str 中文名
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | module | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[filter_array] | - | String | 是 | 模块标识
data[field_array] | - | String | 是 | 字段标识列表
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "镜头"
}
```
## /cgtw7.0/event_filter
```text
事件
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/event_filter/exec
```text
发送事件
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | event_filter | String | 是 | 控制器
data[method] | exec | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[type] | data | String | 是 | 事件类型-数据data 文件框filebox之类
data[data_array][db] | {{db}} | Array | 是 | 数据库
data[data_array][module] | shot | Array | 是 | 模块
data[data_array][module_type] | info | Array | 是 | 模块类型
data[data_array][action] | update | Array | 是 | 触发类型创建create、更新update.等
data[data_array][id_list][] | 0ABB0965-9F79-E003-2E39-A7EB5904BB42 | Array | 否 | ID列表(已弃用)
data[data_array][field_sign_list][] | shot.frame | Array | 是 | 字段列表
data[data_array][filter_data][0]['id'] | 11 | String | 是 | 原id列表调整.
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/group
```text
权限组
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/group/get_group_id_array
```text
获取权限组ID数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | group | String | 是 | 控制器
data[method] | get_group_id_array | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"AEA1D0BE-63DA-45A2-5F45-C2683F4B8D8F",
		"5273E2A4-F9FF-53A2-4D9F-350F37E3D1D2"
	]
}
```
## /cgtw7.0/group/is_in_group
```text
是否在权限组
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | group | String | 是 | 控制器
data[method] | is_in_group | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[check_group_id] | AEA1D0BE-63DA-45A2-5F45-C2683F4B8D8F | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/com
```text
暂无描述
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/com/get_time
```text
获取服务器时间
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | com | String | 是 | 控制器
data[method] | get_time | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "2023-02-28 11:00:00"
}
```
## /cgtw7.0/com/get_company
```text
获取服务器时间
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | com | String | 是 | 控制器
data[method] | get_company | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": "2023-02-28 11:00:00"
}
```
## /cgtw7.0/msg
```text
消息
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/msg/send_task
```text
发送消息
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | msg | String | 是 | 控制器
data[method] | send_task | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | asset | String | 是 | 模块标识
data[module_type] | task | String | 是 | 模块类型
data[task_id] | {{asset_task_id}} | String | 是 | 任务ID
data[content] | "" | Array | 是 | 发送内容
data[account_id_array][] | {{account_id}} | Array | 是 | 账号ID列表
data[server] | - | String | 否 | 拖入插件时抄送链接文件问题-
data[server_id] | - | String | 否 | 拖入插件时抄送链接文件问题-
data[path_array] | - | String | 否 | 拖入插件时抄送链接文件问题-
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/permission
```text
权限
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/permission/permission
```text
是否有权限
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | permission | String | 是 | 控制器
data[method] | has_permission | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[permission] | main_task_show_all | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": true
}
```
## /cgtw7.0/work_flow
```text
工作流程
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/work_flow/get_check_filter
```text
获取待审核过滤条件
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | work_flow | String | 是 | 控制器
data[method] | get_check_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"(",
		[
			"task.flow_id",
			"=",
			"672A349D-A765-FBFB-CC5E-06C8A06B2B79"
		],
		"and",
		[
			"task.check_field_sign",
			"=",
			"task.leader_status"
		],
		")",
		"or",
		"(",
		[
			"task.flow_id",
			"=",
			"672A349D-A765-FBFB-CC5E-06C8A06B2B79"
		],
		"and",
		[
			"task.check_field_sign",
			"=",
			"task.director_status"
		],
		")",
		"or",
		"(",
		[
			"task.flow_id",
			"=",
			"672A349D-A765-FBFB-CC5E-06C8A06B2B79"
		],
		"and",
		[
			"task.check_field_sign",
			"=",
			"task.client_status"
		],
		")",
		"or",
		"(",
		[
			"task.flow_id",
			"=",
			"672A349D-A765-FBFB-CC5E-06C8A06B2B79"
		],
		"and",
		[
			"task.check_field_sign",
			"=",
			"task.file_status"
		],
		")",
		"or",
		"(",
		[
			"task.flow_id",
			"=",
			"3B0FFB50-7EFB-FE5E-07F3-EA2A04A77D49"
		],
		"and",
		[
			"task.check_field_sign",
			"=",
			"task.leader_status"
		],
		")",
		"or",
		"(",
		[
			"task.flow_id",
			"=",
			"3B0FFB50-7EFB-FE5E-07F3-EA2A04A77D49"
		],
		"and",
		[
			"task.check_field_sign",
			"=",
			"task.director_status"
		],
		")"
	]
}
```
## /cgtw7.0/work_flow/get_qc_data
```text
获取修改审核字段数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | work_flow | String | 是 | 控制器
data[method] | get_qc_data | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[task_id] | B006E913-4B83-C465-D2A5-6A38D087F243 | String | 是 | 任务ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"field_sign": "task.leader_status",
			"field_str": "内部审核",
			"en_name": "Leader_review",
			"status_id": "1C82E03F-574D-43EC-A07B-89B948C68D5E",
			"status": "Approve",
			"status_type": "approve",
			"color": "#0cc991",
			"uuid": "447E906F-5B92-58E3-E678-E39FCC209AAD"
		},
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"field_sign": "task.leader_status",
			"field_str": "内部审核",
			"en_name": "Leader_review",
			"status_id": "53B682BA-4F03-84D5-98E4-68738E618CC0",
			"status": "Retake",
			"status_type": "retake",
			"color": "#ff6952",
			"uuid": "447E906F-5B92-58E3-E678-E39FCC209AAD"
		},
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"field_sign": "task.leader_status",
			"field_str": "内部审核",
			"en_name": "Leader_review",
			"status_id": "1b5a9ede-167b-4a5f-af67-f8dd13f88381",
			"status": "Pause",
			"status_type": "pause",
			"color": "#FF9E3E",
			"uuid": "447E906F-5B92-58E3-E678-E39FCC209AAD"
		},
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"field_sign": "task.leader_status",
			"field_str": "内部审核",
			"en_name": "Leader_review",
			"status_id": "3E2E8845-3D4D-785F-1784-56101A946AF4",
			"status": "Revert",
			"status_type": "revert",
			"color": "#3E9EFF",
			"uuid": "447E906F-5B92-58E3-E678-E39FCC209AAD"
		},
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"field_sign": "task.director_status",
			"field_str": "导演审核",
			"en_name": "Director_review",
			"status_id": "53B682BA-4F03-84D5-98E4-68738E618CC0",
			"status": "Retake",
			"status_type": "retake",
			"color": "#ff6952",
			"uuid": "447E906F-5B92-58E3-E678-E39FCC209AAD"
		},
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"field_sign": "task.director_status",
			"field_str": "导演审核",
			"en_name": "Director_review",
			"status_id": "1C82E03F-574D-43EC-A07B-89B948C68D5E",
			"status": "Approve",
			"status_type": "approve",
			"color": "#0cc991",
			"uuid": "447E906F-5B92-58E3-E678-E39FCC209AAD"
		},
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"field_sign": "task.client_status",
			"field_str": "客户审核",
			"en_name": "Client_review",
			"status_id": "1C82E03F-574D-43EC-A07B-89B948C68D5E",
			"status": "Approve",
			"status_type": "approve",
			"color": "#0cc991",
			"uuid": "447E906F-5B92-58E3-E678-E39FCC209AAD"
		},
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"field_sign": "task.client_status",
			"field_str": "客户审核",
			"en_name": "Client_review",
			"status_id": "53B682BA-4F03-84D5-98E4-68738E618CC0",
			"status": "Retake",
			"status_type": "retake",
			"color": "#ff6952",
			"uuid": "447E906F-5B92-58E3-E678-E39FCC209AAD"
		},
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"field_sign": "task.file_status",
			"field_str": "工程审核",
			"en_name": "File Status",
			"status_id": "1C82E03F-574D-43EC-A07B-89B948C68D5E",
			"status": "Approve",
			"status_type": "approve",
			"color": "#0cc991",
			"uuid": "A360590A-2EF5-F34B-DEFA-FB2AA0680ABC"
		},
		{
			"flow_id": "672A349D-A765-FBFB-CC5E-06C8A06B2B79",
			"field_sign": "task.file_status",
			"field_str": "工程审核",
			"en_name": "File Status",
			"status_id": "53B682BA-4F03-84D5-98E4-68738E618CC0",
			"status": "Retake",
			"status_type": "retake",
			"color": "#ff6952",
			"uuid": "A360590A-2EF5-F34B-DEFA-FB2AA0680ABC"
		}
	]
}
```
## /cgtw7.0/work_flow/get_first_qc_with_task_id
```text
获取第一审核审核抄送人员账号id
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | work_flow | String | 是 | 控制器
data[method] | get_first_qc_with_task_id | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[task_id] | B006E913-4B83-C465-D2A5-6A38D087F243 | String | 是 | 任务ID
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		"B8B95A85-36E8-B6FB-DB78-301A358C77F3",
		"F2E31BCA-63C9-55A2-3D24-5FF65CC5C20F",
		"A98C9570-F63D-84A5-1620-3EA8CB13D87E"
	]
}
```
## /cgtw7.0/work_flow/get_task_status_data
```text
获取任务状态字段中数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | work_flow | String | 是 | 控制器
data[method] | get_task_status_data | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[db] | {{db}} | String | 是 | 数据库
data[module] | shot | String | 是 | 模块标识
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"field_str": "Task staus",
			"field_sign": "etask.status",
			"status": "Retake",
			"status_id": "53B682BA-4F03-84D5-98E4-68738E618CC0",
			"status_type": "retake",
			"color": "#f20c0c"
		},
		{
			"field_str": "Task staus",
			"field_sign": "etask.status",
			"status": "Pause",
			"status_id": "1b5a9ede-167b-4a5f-af67-f8dd13f88381",
			"status_type": "pause",
			"color": "#FF9E3E"
		},
		{
			"field_str": "Task staus",
			"field_sign": "etask.status",
			"status": "Approve",
			"status_id": "1C82E03F-574D-43EC-A07B-89B948C68D5E",
			"status_type": "approve",
			"color": "#0cc991"
		},
		{
			"field_str": "Task staus",
			"field_sign": "etask.status",
			"status": "Wait",
			"status_id": "9b9326ce-9f59-42a7-b5d3-fb98dfcce987",
			"status_type": "wait",
			"color": "#5d636b"
		},
		{
			"field_str": "Task staus",
			"field_sign": "etask.status",
			"status": "Rework",
			"status_id": "F988477A-7A90-208C-68B8-1E38D5D9E9E4",
			"status_type": "rework",
			"color": "#FE5858"
		}
	]
}
```
## /cgtw7.0/tag
```text
标签
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/tag/get_filter
```text
获取标签数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | tag | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[field_array][] | entity | String | 是 | 字段标识列表
data[field_array][] | color | String | 是 | -
data[field_array][] | classify_id | String | 是 | -
data[field_array][] | #id | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "大雄兔",
			"color": "#000000",
			"classify_id": "56b55c08-b4fd-43d5-b34c-d572569ef68b",
			"#id": "3F7AB746-D907-C16C-22C2-D506DC0FF85A"
		},
		{
			"entity": "etask",
			"color": "#000000",
			"classify_id": "0cbc7cb9-8216-4401-bd27-967dcad5a8ed",
			"#id": "2B3E49D0-E390-DB7F-E8EF-36AE6D9DBA13"
		},
		{
			"entity": "古娜拉黑暗之神，呼卡拉卡",
			"color": "#000000",
			"classify_id": "56b55c08-b4fd-43d5-b34c-d572569ef68b",
			"#id": "2928CC44-B99A-B555-75DB-6FE7CE1B1C22"
		},
		{
			"entity": "2324",
			"color": "#000000",
			"classify_id": "56b55c08-b4fd-43d5-b34c-d572569ef68b",
			"#id": "0A231D72-DD78-8ED2-EE1B-DCA1CF415C77"
		},
		{
			"entity": "ttttttt",
			"color": "#000000",
			"classify_id": "56b55c08-b4fd-43d5-b34c-d572569ef68b",
			"#id": "D2EDFDF2-195A-9356-A487-EED8B085261C"
		},
		{
			"entity": "ad",
			"color": "#000000",
			"classify_id": "56b55c08-b4fd-43d5-b34c-d572569ef68b",
			"#id": "3A46776C-8CD4-9240-B600-F5558E32F1CC"
		}
	]
}
```
## /cgtw7.0/tag_classify
```text
标签分类
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/tag_classify/get_filter
```text
获取标签分类数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | tag_classify | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[field_array][] | entity | Array | 是 | 字段标识列表
data[filter_array][] | - | Array | 否 | 过滤条件
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "lb_test",
			"#id": "A5462BC8-B985-4EC4-93E3-3B206F820F2A"
		},
		{
			"entity": "ss",
			"#id": "28B0BB17-8BCC-4681-8E77-5F10C2E488A8"
		},
		{
			"entity": "aa",
			"#id": "EA5EA2C9-6DE9-4608-A915-D28CDE9B0CD6"
		},
		{
			"entity": "a1",
			"#id": "00D35777-A5B7-4BE6-A8DE-E95A169B29CE"
		},
		{
			"entity": "ddddd",
			"#id": "94FB57D0-9A6A-4AC9-B963-EBCAC91E38E6"
		},
		{
			"entity": "DM",
			"#id": "8eeb914e-6cb8-4c56-8cfc-737ca26b982c"
		},
		{
			"entity": "lb简单审核",
			"#id": "e4bfdf67-b7a3-4fa7-9a17-b632c5b1f04f"
		},
		{
			"entity": "B模板",
			"#id": "d1aa7bba-32ff-4e4a-aea7-dc4f087e606e"
		},
		{
			"entity": "QK_eee",
			"#id": "6f23f0ab-4492-4568-8dc7-9d871a6108a6"
		},
		{
			"entity": "jianhua_e",
			"#id": "d5c2cde1-cee8-4d0c-85af-60eb97f7aabc"
		},
		{
			"entity": "jianhua_test",
			"#id": "f4917bb1-508f-4e6a-8663-3f5361950117"
		},
		{
			"entity": "B",
			"#id": "41dca9e9-1b86-438a-bd56-4ecbda92bf0b"
		},
		{
			"entity": "YYZGZ-集-场-镜",
			"#id": "ba642838-6941-4209-87be-6bd9b08a34ff"
		},
		{
			"entity": "YYZGZ",
			"#id": "d2b44160-603a-4d63-b609-04b52c3e0535"
		},
		{
			"entity": "xiaoying_tmp",
			"#id": "b782f5c4-7c6e-43a7-b019-321f3e2037da"
		},
		{
			"entity": "xiaoying_no_parent",
			"#id": "a422aef2-e3a9-44c5-831a-fb5260c05e1a"
		},
		{
			"entity": "A模板",
			"#id": "a5a1a9f9-b4be-4fc9-9d19-b3adb8afbb46"
		},
		{
			"entity": "2_dianyyy",
			"#id": "e26be05e-5645-412b-a893-5e0195dc9128"
		},
		{
			"entity": "恭禧",
			"#id": "92c13f7f-cb1f-4074-a159-d1c7fbd74aab"
		},
		{
			"entity": "YT-标签",
			"#id": "964E98BF-01FB-4A1F-B9CB-63559CA35C55"
		},
		{
			"entity": "test模板",
			"#id": "e87ea081-a63c-41e6-b52d-e4aaca611a10"
		},
		{
			"entity": "简易流程",
			"#id": "3beda69b-aec4-4697-84da-1dd942a7de82"
		},
		{
			"entity": "简易版模板",
			"#id": "fbf90af0-5dd1-4b52-939c-b1d8566b7242"
		},
		{
			"entity": "DM_ETASK",
			"#id": "ff34c672-44a4-46ff-ae22-a428eb88fe66"
		},
		{
			"entity": "九映7.0问题整理",
			"#id": "2f54e3f8-9d26-4e33-bfc1-156bff804b54"
		},
		{
			"entity": "__K__",
			"#id": "68bb9ac9-34b4-4b88-894e-900cb7da7e5c"
		},
		{
			"entity": "lb_test简易",
			"#id": "1c8a8821-2b5e-45f8-a8d2-7fd1ca06a568"
		},
		{
			"entity": "曾瑞垦的模板",
			"#id": "966cee69-ea8a-4c90-b98d-e244b65ad933"
		},
		{
			"entity": "TXT",
			"#id": "4f4a4da4-6e6b-4ada-9f99-7416406d854e"
		},
		{
			"entity": "xiaoying_etask",
			"#id": "1feac796-4b2f-4195-a1c8-022161ffcddc"
		},
		{
			"entity": "A模板（简易流程）",
			"#id": "014c09c4-6956-4823-86be-a74a44a5ba45"
		},
		{
			"entity": "SM_eTASK",
			"#id": "f5e26e7b-c2f6-4ce5-bb08-ab8fbaccfd1b"
		},
		{
			"entity": "E",
			"#id": "c104821c-a654-4a40-9c8a-2a1bb8832fb2"
		},
		{
			"entity": "SM",
			"#id": "eb209991-1f17-4c5f-af10-bbcc60e32936"
		},
		{
			"entity": "etask",
			"#id": "0cbc7cb9-8216-4401-bd27-967dcad5a8ed"
		},
		{
			"entity": "1_剧集",
			"#id": "56b55c08-b4fd-43d5-b34c-d572569ef68b"
		},
		{
			"entity": "LMH_ETASK",
			"#id": "eaa62e71-663f-4ee7-96a4-e072c7218481"
		},
		{
			"entity": "集数&镜头号",
			"#id": "8d9c9efa-c4f5-4ce8-aa44-922ff583f078"
		},
		{
			"entity": "恭禧1",
			"#id": "1fb64761-6af7-4032-ac63-744b21cfd6e4"
		},
		{
			"entity": "king",
			"#id": "3ad295e1-5681-43f1-a96f-aab85d1e62f1"
		},
		{
			"entity": "__K__etask",
			"#id": "490cfa36-993b-4b19-b4f9-fcf934077431"
		},
		{
			"entity": "CG动画电影",
			"#id": "ceac08d4-e53e-46d4-a575-48bd663eb4d3"
		},
		{
			"entity": "QK_M",
			"#id": "391c5db5-9266-41b9-931e-7a8c8f9275a5"
		},
		{
			"entity": "沙雕文化资产",
			"#id": "4519c6d4-86c9-4b57-aa8b-ba45c46b53ef"
		},
		{
			"entity": "jianhua_test2",
			"#id": "f9ae4d7f-1187-442e-a14f-4b8a1e3f7d83"
		},
		{
			"entity": "集数&场次&镜头号",
			"#id": "b47ad2df-d1e4-4abe-ae8e-b86350c30507"
		},
		{
			"entity": "xiaoying_new",
			"#id": "66b2a721-842a-438f-884c-6ff74676d8b8"
		},
		{
			"entity": "QK",
			"#id": "4ded6d48-ea93-496f-9c61-9ce35825b714"
		},
		{
			"entity": "2_电影",
			"#id": "e6ce931d-01c9-4cfe-8d78-b6e16b6931eb"
		},
		{
			"entity": "K_test2",
			"#id": "8e2b2619-aa2a-4a15-88ea-06b209dafe77"
		}
	]
}
```
## /cgtw7.0/client
```text
暂无描述
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/client/get_sys_key
```text
Key:
retake_pipeline_id_list  返修阶段id列表
change   获取修改前数据
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/

#### 请求方式
> POST

#### Content-Type
> none

#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/client/get_department
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | client | String | 是 | 控制器
data[method] | get_department | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/client/get_myjob_db
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | client | String | 是 | 控制器
data[method] | get_myjob_db | String | 是 | 方法
data[app] | api | String | 是 | 固定值
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/token
```text
暂无描述
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/token/get_account_id
```text
retake_pipeline_id_list
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/

#### 请求方式
> POST

#### Content-Type
> none

#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/token/get_account
```text
retake_pipeline_id_list
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/

#### 请求方式
> POST

#### Content-Type
> none

#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/token/get_username
```text
retake_pipeline_id_list
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/

#### 请求方式
> POST

#### Content-Type
> none

#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/status
```text
暂无描述
```
#### Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /cgtw7.0/status/get_filter
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://192.168.199.48/api.php

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
data[controller] | status | String | 是 | 控制器
data[method] | get_filter | String | 是 | 方法
data[app] | api | String | 是 | 固定值
data[field_array][] | entity | String | 是 | 字段标识列表
data[field_array][] | color | String | 是 | -
data[status_type] | - | String | 是 | -
#### 认证方式
```text
noauth
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": "1",
	"type": "json",
	"data": [
		{
			"entity": "大雄兔",
			"color": "#000000",
			"classify_id": "56b55c08-b4fd-43d5-b34c-d572569ef68b",
			"#id": "3F7AB746-D907-C16C-22C2-D506DC0FF85A"
		},
		{
			"entity": "etask",
			"color": "#000000",
			"classify_id": "0cbc7cb9-8216-4401-bd27-967dcad5a8ed",
			"#id": "2B3E49D0-E390-DB7F-E8EF-36AE6D9DBA13"
		},
		{
			"entity": "古娜拉黑暗之神，呼卡拉卡",
			"color": "#000000",
			"classify_id": "56b55c08-b4fd-43d5-b34c-d572569ef68b",
			"#id": "2928CC44-B99A-B555-75DB-6FE7CE1B1C22"
		},
		{
			"entity": "2324",
			"color": "#000000",
			"classify_id": "56b55c08-b4fd-43d5-b34c-d572569ef68b",
			"#id": "0A231D72-DD78-8ED2-EE1B-DCA1CF415C77"
		},
		{
			"entity": "ttttttt",
			"color": "#000000",
			"classify_id": "56b55c08-b4fd-43d5-b34c-d572569ef68b",
			"#id": "D2EDFDF2-195A-9356-A487-EED8B085261C"
		},
		{
			"entity": "ad",
			"color": "#000000",
			"classify_id": "56b55c08-b4fd-43d5-b34c-d572569ef68b",
			"#id": "3A46776C-8CD4-9240-B600-F5558E32F1CC"
		}
	]
}
```