import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryEquipment(params) {
  return request('/api/xadmin/v1/equipment', {
    params,
  });
}
export async function removeEquipment(params) {
  return request(`/api/xadmin/v1/equipment/${params}`, {
    method: 'DELETE',
  });
}
export async function addEquipment(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/equipment', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateEquipment(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/equipment/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryEquipmentVerboseName(params) {
  return request('/api/xadmin/v1/equipment/verbose_name', {
    params,
  });
}
export async function queryEquipmentListDisplay(params) {
  return request('/api/xadmin/v1/equipment/list_display', {
    params,
  });
}
export async function queryEquipmentDisplayOrder(params) {
  return request('/api/xadmin/v1/equipment/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

