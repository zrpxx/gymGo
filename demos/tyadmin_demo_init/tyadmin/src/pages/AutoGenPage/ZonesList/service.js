import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryZones(params) {
  return request('/api/xadmin/v1/zones', {
    params,
  });
}
export async function removeZones(params) {
  return request(`/api/xadmin/v1/zones/${params}`, {
    method: 'DELETE',
  });
}
export async function addZones(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/zones', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateZones(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/zones/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryZonesVerboseName(params) {
  return request('/api/xadmin/v1/zones/verbose_name', {
    params,
  });
}
export async function queryZonesListDisplay(params) {
  return request('/api/xadmin/v1/zones/list_display', {
    params,
  });
}
export async function queryZonesDisplayOrder(params) {
  return request('/api/xadmin/v1/zones/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

