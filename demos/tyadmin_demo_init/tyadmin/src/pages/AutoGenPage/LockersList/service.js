import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryLockers(params) {
  return request('/api/xadmin/v1/lockers', {
    params,
  });
}
export async function removeLockers(params) {
  return request(`/api/xadmin/v1/lockers/${params}`, {
    method: 'DELETE',
  });
}
export async function addLockers(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/lockers', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateLockers(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/lockers/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryLockersVerboseName(params) {
  return request('/api/xadmin/v1/lockers/verbose_name', {
    params,
  });
}
export async function queryLockersListDisplay(params) {
  return request('/api/xadmin/v1/lockers/list_display', {
    params,
  });
}
export async function queryLockersDisplayOrder(params) {
  return request('/api/xadmin/v1/lockers/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

