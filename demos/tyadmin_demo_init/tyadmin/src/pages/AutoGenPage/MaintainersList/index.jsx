import { DeleteOutlined, DownOutlined, EditOutlined, PlusOutlined, ExportOutlined } from '@ant-design/icons';
import { notification, Button, Col, Descriptions, Divider, Dropdown, Form, Input, Menu, message, Popconfirm, Popover, Row, Select, Tag, Transfer, Switch } from 'antd';
import React, { useEffect, useRef, useState } from 'react';
import KeyOutlined from '@ant-design/icons/lib/icons/KeyOutlined';
import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable from 'mtianyan-pro-table';
import CreateForm from './components/CreateForm';
import { addMaintainers, queryMaintainers, removeMaintainers, updateMaintainers, queryMaintainersVerboseName, queryMaintainersListDisplay, queryMaintainersDisplayOrder} from './service';
import UpdateForm from './components/UpdateForm';
import UploadAvatar from '@/components/UploadAvatar';
import {queryUser, queryUserVerboseName} from '@/pages/AutoGenPage/UserList/service';import {queryGroup} from '@/pages/AutoGenPage/GroupList/service';import {queryPermission} from '@/pages/AutoGenPage/PermissionList/service';

import moment from 'moment';
const { Option } = Select;
import { BooleanFormItem, dealManyToManyFieldTags, fileUpload, twoColumns, richForm, richCol, dealPureSelectField, orderForm, exportExcelCurrent, exportExcelAll, getUpdateColumns, dealRemoveError, dealError, BooleanDisplay, dealDateTimeDisplay, dealManyToManyField, dealTime, deepCopy, fieldErrorHandle, getTableColumns, renderManyToMany, richTrans, dealForeignKeyField, renderForeignKey, fieldsLevelErrorHandle } from '@/utils/utils';
import 'braft-editor/dist/index.css'
const FormItem = Form.Item;
const TableList = () => {
  const [createModalVisible, handleModalVisible] = useState(false);
  const [updateModalVisible, handleUpdateModalVisible] = useState(false);
 
  const [updateFormValues, setUpdateFormValues] = useState({});
  const actionRef = useRef();
  const addFormRef = useRef();
  const updateFormRef = useRef();

  const handleAdd = async fields => {
    const hide = message.loading('正在添加');

    try {
      await addMaintainers({ ...fields });
      hide();
      message.success('添加成功');
      return true;
    } catch (error) {
      return dealError(error, addFormRef, hide, "添加");
    }
  };

  const handleUpdate = async (value, current_id) => {
    const hide = message.loading('正在修改');

    try {
      await updateMaintainers(value, current_id);
      hide();
      message.success('修改成功');
      return true;
    } catch (error) {
      return dealError(error, updateFormRef, hide, "修改");
    }
  };

  const handleRemove = async selectedRows => {
    const hide = message.loading('正在删除');
    if (!selectedRows) return true;

    try {
      const ids = selectedRows.map(row => row.id).join(',');
      await removeMaintainers(ids);
      hide();
      message.success('删除成功');
      return true;
    } catch (error) {
      hide()
      return dealRemoveError(error, "删除");
    }
  };
 
  const dateFieldList = ["last_login","date_joined"]
  const base_columns = [{
                             title: 'id',
                             
        hideInForm: true,
        hideInSearch: true,
        
                             
                             dataIndex: 'id',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'password',
                             
        hideInTable: true,
        hideInSearch: true,
        
                             
                             dataIndex: 'password',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'password为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: 'last_login',
                             
                             
                             dataIndex: 'last_login',
                             valueType: 'dateTime',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'is_superuser',
                             
                             initialValue: false,
                             dataIndex: 'is_superuser',
                             
                             rules: [
                                     
                             ],
                             
                                     render: (text, record) => {
                                  return BooleanDisplay(text);
                                },
                        renderFormItem: (item, {value, onChange}) => {
                          return BooleanFormItem(value, onChange);
                        },
        
                             
                        },
                      {
                             title: 'username',
                             
                             
                             dataIndex: 'username',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'username为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: 'first_name',
                             
                             
                             dataIndex: 'first_name',
                             
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'last_name',
                             
                             
                             dataIndex: 'last_name',
                             
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'email',
                             
                             
                             dataIndex: 'email',
                             
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'is_staff',
                             
                             initialValue: false,
                             dataIndex: 'is_staff',
                             
                             rules: [
                                     
                             ],
                             
                                     render: (text, record) => {
                                  return BooleanDisplay(text);
                                },
                        renderFormItem: (item, {value, onChange}) => {
                          return BooleanFormItem(value, onChange);
                        },
        
                             
                        },
                      {
                             title: 'is_active',
                             
                             initialValue: true,
                             dataIndex: 'is_active',
                             
                             rules: [
                                     
                             ],
                             
                                     render: (text, record) => {
                                  return BooleanDisplay(text);
                                },
                        renderFormItem: (item, {value, onChange}) => {
                          return BooleanFormItem(value, onChange);
                        },
        
                             
                        },
                      {
                             title: 'date_joined',
                             
            hideInForm: true,
            
                             
                             dataIndex: 'date_joined',
                             valueType: 'dateTime',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: '用户类型',
                             
                             initialValue: 1,
                             dataIndex: 'type',
                             
                             rules: [
                                     
                             ],
                             
                             valueEnum:{"1":"超级管理员","2":"教练","3":"维修员","4":"顾客"}
                        },
                      {
                             title: 'user_ptr',
                             
                             
                             dataIndex: 'user_ptr',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'user_ptr为必填项',
                     },
                             ],
                             
                        renderFormItem: (item, {value, onChange}) => {
                                          return dealForeignKeyField(item, value, onChange, user_ptrForeignKeyList);
                                  },
                        render: (text, record) => {
                              return renderForeignKey(text, user_ptrVerboseNameMap);
                            },
                             
                        },
                      {
                             title: '工种',
                             
                             initialValue: "全能大师",
                             dataIndex: 'work_type',
                             valueType: 'textarea',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: '工资',
                             
                             
                             dataIndex: 'salary',
                             
                             rules: [
                                     {
                      required: true,
                      message: '工资为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: 'groups',
                             
                             
                             dataIndex: 'groups',
                             
                             rules: [
                                     
                             ],
                             
                
                renderFormItem: (item, {value, onChange, type, defaultRender}) => {
                      return dealManyToManyField(item, value,onChange,type, groupsManyToManyList)
                },
               render: (text, record) => {
                    return renderManyToMany(text)
            }, 
        
                             
                        },
                      {
                             title: 'user_permissions',
                             
                             
                             dataIndex: 'user_permissions',
                             
                             rules: [
                                     
                             ],
                             
                
                renderFormItem: (item, {value, onChange, type, defaultRender}) => {
                      return dealManyToManyField(item, value,onChange,type, user_permissionsManyToManyList)
                },
               render: (text, record) => {
                    return renderManyToMany(text)
            }, 
        
                             
                        },
                          {
                              title: '操作',
                              dataIndex: 'option',
                              valueType: 'option',
                                    fixed: 'right',
          width: 100,
                              render: (text, record) => (
                                <>

                                  <EditOutlined title="编辑" className="icon" onClick={async () => {
                                   record.last_login = record.last_login === null ? record.last_login : moment(record.last_login);record.date_joined = record.date_joined === null ? record.date_joined : moment(record.date_joined);
                                    handleUpdateModalVisible(true);
                                    setUpdateFormValues(record);
                                  }} />
                                  <Divider type="vertical" />
                                  <Popconfirm
                                    title="您确定要删除修理员管理吗？"
                                    placement="topRight"
                                    onConfirm={() => {
                                      handleRemove([record])
                                      actionRef.current.reloadAndRest();
                                    }}
                                    okText="确定"
                                    cancelText="取消"
                                  >
                                    <DeleteOutlined title="删除" className="icon" />
                                  </Popconfirm>
                                </>
                              ),
                            },];

  let cp = deepCopy(base_columns);

  const [formOrder, setFormOrder] = useState([]);

  useEffect(() => {
    queryMaintainersDisplayOrder().then(r => {
      setFormOrder(r.form_order)
    })
  }, [])
  const table_columns = getTableColumns(cp);

  let order_cp = deepCopy(base_columns);
  const form_ordered = orderForm(formOrder, order_cp);

  const create_columns = [...form_ordered];
  const update_cp = deepCopy(form_ordered)
  const update_columns = getUpdateColumns(update_cp);

  const [columnsStateMap, setColumnsStateMap] = useState({});

  const [paramState, setParamState] = useState({});

  useEffect(() => {
    queryMaintainersListDisplay().then(value => {
      setColumnsStateMap(value)
    })
  }, [])


   
                                const [user_ptrForeignKeyList, setUser_ptrForeignKeyList] = useState([]);
                                useEffect(() => {
                                queryUser({all: 1}).then(value => {
                                     setUser_ptrForeignKeyList(value);
                                });
                                }, []);
                                const [user_ptrVerboseNameMap, setUser_ptrVerboseNameMap] = useState([]);
                                useEffect(() => {
                                queryUserVerboseName().then(value => {
                                    setUser_ptrVerboseNameMap(value);
                                });
                                }, []);

   const [groupsManyToManyList, setGroupsManyToManyList] = useState([]);
                        useEffect(() => {
                          queryGroup({all:1}).then(value => {
                            setGroupsManyToManyList(value);
                          });
                        }, []);const [user_permissionsManyToManyList, setUser_permissionsManyToManyList] = useState([]);
                        useEffect(() => {
                          queryPermission({all:1}).then(value => {
                            setUser_permissionsManyToManyList(value);
                          });
                        }, []);
  return (
    <PageHeaderWrapper>
      <ProTable
        beforeSearchSubmit={(params => {
          dealTime(params, dateFieldList);
          return params;
        })}
        params={paramState}
        scroll={{ x: '100%' }}
        columnsStateMap={columnsStateMap}
        onColumnsStateChange={(map) => setColumnsStateMap(map)}
        headerTitle="修理员管理表格"
        actionRef={actionRef}
        rowKey="id"
        toolBarRender={(action, { selectedRows }) => [
          <Button type="primary" onClick={() => handleModalVisible(true)}>
            <PlusOutlined /> 新建
          </Button>,
          <Button type="primary" onClick={() => exportExcelAll(paramState, queryMaintainers, table_columns, '修理员管理-All')}>
            <ExportOutlined /> 导出全部
          </Button>,
          <Input.Search style={{ marginRight: 20 }} placeholder="搜索修理员管理" onSearch={value => {
            setParamState({
              search: value,
            });
            actionRef.current.reload();
          }} />,
          selectedRows && selectedRows.length > 0 && (
            <Dropdown
              overlay={
                <Menu
                  onClick={async e => {
                    if (e.key === 'remove') {
                      await handleRemove(selectedRows);
                      actionRef.current.reloadAndRest();
                    }
                    else if (e.key === 'export_current') {
                      exportExcelCurrent(selectedRows, table_columns, '修理员管理-select')
                    }
                  }}
                  selectedKeys={[]}
                >
                  <Menu.Item key="remove">批量删除</Menu.Item>
                  <Menu.Item key="export_current">导出已选</Menu.Item>
                </Menu>
              }
            >
              <Button>
                批量操作 <DownOutlined />
              </Button>
            </Dropdown>
          ),
        ]}
        tableAlertRender={({ selectedRowKeys, selectedRows }) => (
          selectedRowKeys.length > 0 ? <div>
            已选择{' '}
            <a
              style={{
                fontWeight: 600,
              }}
            >
              {selectedRowKeys.length}
            </a>{' '}
            项&nbsp;&nbsp;
          </div> : false

        )}
        request={(params, sorter, filter) => queryMaintainers({ ...params, sorter, filter })}
        columns={table_columns}
        rowSelection={{}}
      />
      <CreateForm onCancel={() => handleModalVisible(false)} modalVisible={createModalVisible}>
        <ProTable
          formRef={addFormRef}
          onSubmit={async value => {
            richTrans(value);
            const success = await handleAdd(value);

            if (success) {
              handleModalVisible(false);

              if (actionRef.current) {
                actionRef.current.reload();
              }
            }
          }}
          rowKey="key"
          type="form"
          search={twoColumns}
          form={
            {
              labelCol: { span: 6 },
              labelAlign: 'left',
            }}
          columns={create_columns}
          rowSelection={{}}
        />
      </CreateForm>
      <UpdateForm onCancel={() => handleUpdateModalVisible(false)} modalVisible={updateModalVisible}>
        <ProTable
          formRef={updateFormRef}
          onSubmit={async value => {
            richTrans(value);
            const success = await handleUpdate(value, updateFormValues.id);

            if (success) {
              handleUpdateModalVisible(false);

              if (actionRef.current) {
                actionRef.current.reload();
              }
            }
          }}
          rowKey="key"
          search={twoColumns}
          type="form"
          form={{
            initialValues: updateFormValues, labelCol: { span: 6 },
            labelAlign: 'left',
          }}
          columns={update_columns}
          rowSelection={{}}
        />
      </UpdateForm>
       
    </PageHeaderWrapper>
  );
};

export default TableList;