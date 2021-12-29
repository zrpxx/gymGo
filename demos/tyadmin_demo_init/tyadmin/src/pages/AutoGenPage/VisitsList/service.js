import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryVisits(params) {
  return request('/api/xadmin/v1/visits', {
    params,
  });
}
export async function removeVisits(params) {
  return request(`/api/xadmin/v1/visits/${params}`, {
    method: 'DELETE',
  });
}
export async function addVisits(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/visits', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateVisits(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/visits/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryVisitsVerboseName(params) {
  return request('/api/xadmin/v1/visits/verbose_name', {
    params,
  });
}
export async function queryVisitsListDisplay(params) {
  return request('/api/xadmin/v1/visits/list_display', {
    params,
  });
}
export async function queryVisitsDisplayOrder(params) {
  return request('/api/xadmin/v1/visits/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

