import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryBuys(params) {
  return request('/api/xadmin/v1/buys', {
    params,
  });
}
export async function removeBuys(params) {
  return request(`/api/xadmin/v1/buys/${params}`, {
    method: 'DELETE',
  });
}
export async function addBuys(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/buys', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateBuys(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/buys/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryBuysVerboseName(params) {
  return request('/api/xadmin/v1/buys/verbose_name', {
    params,
  });
}
export async function queryBuysListDisplay(params) {
  return request('/api/xadmin/v1/buys/list_display', {
    params,
  });
}
export async function queryBuysDisplayOrder(params) {
  return request('/api/xadmin/v1/buys/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

