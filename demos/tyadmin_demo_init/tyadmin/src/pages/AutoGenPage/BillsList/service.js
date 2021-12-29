import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryBills(params) {
  return request('/api/xadmin/v1/bills', {
    params,
  });
}
export async function removeBills(params) {
  return request(`/api/xadmin/v1/bills/${params}`, {
    method: 'DELETE',
  });
}
export async function addBills(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/bills', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateBills(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/bills/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryBillsVerboseName(params) {
  return request('/api/xadmin/v1/bills/verbose_name', {
    params,
  });
}
export async function queryBillsListDisplay(params) {
  return request('/api/xadmin/v1/bills/list_display', {
    params,
  });
}
export async function queryBillsDisplayOrder(params) {
  return request('/api/xadmin/v1/bills/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

