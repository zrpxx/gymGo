import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryArchiveBodyData(params) {
  return request('/api/xadmin/v1/archive_body_data', {
    params,
  });
}
export async function removeArchiveBodyData(params) {
  return request(`/api/xadmin/v1/archive_body_data/${params}`, {
    method: 'DELETE',
  });
}
export async function addArchiveBodyData(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/archive_body_data', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateArchiveBodyData(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/archive_body_data/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryArchiveBodyDataVerboseName(params) {
  return request('/api/xadmin/v1/archive_body_data/verbose_name', {
    params,
  });
}
export async function queryArchiveBodyDataListDisplay(params) {
  return request('/api/xadmin/v1/archive_body_data/list_display', {
    params,
  });
}
export async function queryArchiveBodyDataDisplayOrder(params) {
  return request('/api/xadmin/v1/archive_body_data/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

