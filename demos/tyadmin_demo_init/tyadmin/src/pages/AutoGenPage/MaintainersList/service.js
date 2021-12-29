import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryMaintainers(params) {
  return request('/api/xadmin/v1/maintainers', {
    params,
  });
}
export async function removeMaintainers(params) {
  return request(`/api/xadmin/v1/maintainers/${params}`, {
    method: 'DELETE',
  });
}
export async function addMaintainers(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/maintainers', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateMaintainers(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/maintainers/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryMaintainersVerboseName(params) {
  return request('/api/xadmin/v1/maintainers/verbose_name', {
    params,
  });
}
export async function queryMaintainersListDisplay(params) {
  return request('/api/xadmin/v1/maintainers/list_display', {
    params,
  });
}
export async function queryMaintainersDisplayOrder(params) {
  return request('/api/xadmin/v1/maintainers/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

