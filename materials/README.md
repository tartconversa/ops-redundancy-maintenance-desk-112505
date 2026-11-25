# 演练资料格式

机柜服务维护演练。时钟单位为分钟。设备 capacity 为可接纳的吞吐单位，故障域是可能共同失效的电力单元，站点只用于限制可服务区域。

## `cells` 设备容量和独立故障域

services 表示设备可承载的服务及地域，capacity 是这些服务消费的共享量。warm_min 为设备恢复后独立探针判定稳定所需时间。

字段为 `device`、`fault_domain`、`capacity`、`warm_min`、`services`。

## `coverage` 运行需求和故障域约束

load 表示必须持续有去处的负载。min_domains 是承载该服务的不同电力单元数下限。peak_min 表示开始生效的分钟。

字段为 `service`、`peak_min`、`load`、`min_domains`。

## `jobs` 现场班组申请

rank 越大越紧急。earliest、latest 为允许开工的闭区间。duration_min 是预计断开时段。all_devices 必须作为整体一起维护。 latest 只约束最晚开工。维护窗口长度以停机到完成为准，恢复探针达到稳定时刻后才将容量交还。

字段为 `job`、`crew`、`all_devices`、`earliest`、`latest`、`duration_min`、`rank`。

## `timeline` 实际进度与外部能力变化

request_start 为班组申请开工。lease_seen 与 work_started 回执中的 permit 为现场作业取得的标识，格式由产品返回，材料用外部关联号示意。route_active 和 route_clear 是流量实际迁移回执。 回执的 received 为接收时间，occurred 为设备侧时间。许可超时后由班组确认未开工或提供已开工回执；无法确认的设备视为可能不可用。

字段为 `received`、`occurred`、`kind`、`job`、`device`、`permit`、`value`。
