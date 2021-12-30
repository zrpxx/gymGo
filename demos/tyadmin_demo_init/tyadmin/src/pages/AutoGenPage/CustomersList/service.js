import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCustomers(params) {
  return request('/api/xadmin/v1/customers', {
    params,
  });
}
export async function removeCustomers(params) {
  return request(`/api/xadmin/v1/customers/${params}`, {
    method: 'DELETE',
  });
}
export async function addCustomers(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/customers', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCustomers(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/customers/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCustomersVerboseName(params) {
  return request('/api/xadmin/v1/customers/verbose_name', {
    params,
  });
}
export async function queryCustomersListDisplay(params) {
  return request('/api/xadmin/v1/customers/list_display', {
    params,
  });
}
export async function queryCustomersDisplayOrder(params) {
  return request('/api/xadmin/v1/customers/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

