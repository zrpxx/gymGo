import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryReserveEquipment(params) {
  return request('/api/xadmin/v1/reserve_equipment', {
    params,
  });
}
export async function removeReserveEquipment(params) {
  return request(`/api/xadmin/v1/reserve_equipment/${params}`, {
    method: 'DELETE',
  });
}
export async function addReserveEquipment(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/reserve_equipment', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateReserveEquipment(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/reserve_equipment/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryReserveEquipmentVerboseName(params) {
  return request('/api/xadmin/v1/reserve_equipment/verbose_name', {
    params,
  });
}
export async function queryReserveEquipmentListDisplay(params) {
  return request('/api/xadmin/v1/reserve_equipment/list_display', {
    params,
  });
}
export async function queryReserveEquipmentDisplayOrder(params) {
  return request('/api/xadmin/v1/reserve_equipment/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

