import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryAttends(params) {
  return request('/api/xadmin/v1/attends', {
    params,
  });
}
export async function removeAttends(params) {
  return request(`/api/xadmin/v1/attends/${params}`, {
    method: 'DELETE',
  });
}
export async function addAttends(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/attends', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateAttends(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/attends/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryAttendsVerboseName(params) {
  return request('/api/xadmin/v1/attends/verbose_name', {
    params,
  });
}
export async function queryAttendsListDisplay(params) {
  return request('/api/xadmin/v1/attends/list_display', {
    params,
  });
}
export async function queryAttendsDisplayOrder(params) {
  return request('/api/xadmin/v1/attends/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

