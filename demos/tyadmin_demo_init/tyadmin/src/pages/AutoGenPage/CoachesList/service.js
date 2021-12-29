import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCoaches(params) {
  return request('/api/xadmin/v1/coaches', {
    params,
  });
}
export async function removeCoaches(params) {
  return request(`/api/xadmin/v1/coaches/${params}`, {
    method: 'DELETE',
  });
}
export async function addCoaches(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/coaches', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCoaches(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/coaches/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCoachesVerboseName(params) {
  return request('/api/xadmin/v1/coaches/verbose_name', {
    params,
  });
}
export async function queryCoachesListDisplay(params) {
  return request('/api/xadmin/v1/coaches/list_display', {
    params,
  });
}
export async function queryCoachesDisplayOrder(params) {
  return request('/api/xadmin/v1/coaches/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

