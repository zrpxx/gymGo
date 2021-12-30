import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCurriculums(params) {
  return request('/api/xadmin/v1/curriculums', {
    params,
  });
}
export async function removeCurriculums(params) {
  return request(`/api/xadmin/v1/curriculums/${params}`, {
    method: 'DELETE',
  });
}
export async function addCurriculums(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/curriculums', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCurriculums(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/curriculums/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCurriculumsVerboseName(params) {
  return request('/api/xadmin/v1/curriculums/verbose_name', {
    params,
  });
}
export async function queryCurriculumsListDisplay(params) {
  return request('/api/xadmin/v1/curriculums/list_display', {
    params,
  });
}
export async function queryCurriculumsDisplayOrder(params) {
  return request('/api/xadmin/v1/curriculums/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

