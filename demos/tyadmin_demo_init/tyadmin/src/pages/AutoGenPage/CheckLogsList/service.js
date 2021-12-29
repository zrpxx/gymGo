import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCheckLogs(params) {
  return request('/api/xadmin/v1/check_logs', {
    params,
  });
}
export async function removeCheckLogs(params) {
  return request(`/api/xadmin/v1/check_logs/${params}`, {
    method: 'DELETE',
  });
}
export async function addCheckLogs(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/check_logs', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCheckLogs(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/check_logs/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCheckLogsVerboseName(params) {
  return request('/api/xadmin/v1/check_logs/verbose_name', {
    params,
  });
}
export async function queryCheckLogsListDisplay(params) {
  return request('/api/xadmin/v1/check_logs/list_display', {
    params,
  });
}
export async function queryCheckLogsDisplayOrder(params) {
  return request('/api/xadmin/v1/check_logs/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

