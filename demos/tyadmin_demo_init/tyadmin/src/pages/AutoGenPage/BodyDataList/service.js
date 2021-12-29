import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryBodyData(params) {
  return request('/api/xadmin/v1/body_data', {
    params,
  });
}
export async function removeBodyData(params) {
  return request(`/api/xadmin/v1/body_data/${params}`, {
    method: 'DELETE',
  });
}
export async function addBodyData(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/body_data', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateBodyData(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/body_data/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryBodyDataVerboseName(params) {
  return request('/api/xadmin/v1/body_data/verbose_name', {
    params,
  });
}
export async function queryBodyDataListDisplay(params) {
  return request('/api/xadmin/v1/body_data/list_display', {
    params,
  });
}
export async function queryBodyDataDisplayOrder(params) {
  return request('/api/xadmin/v1/body_data/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

