import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryAgendas(params) {
  return request('/api/xadmin/v1/agendas', {
    params,
  });
}
export async function removeAgendas(params) {
  return request(`/api/xadmin/v1/agendas/${params}`, {
    method: 'DELETE',
  });
}
export async function addAgendas(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/agendas', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateAgendas(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/agendas/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryAgendasVerboseName(params) {
  return request('/api/xadmin/v1/agendas/verbose_name', {
    params,
  });
}
export async function queryAgendasListDisplay(params) {
  return request('/api/xadmin/v1/agendas/list_display', {
    params,
  });
}
export async function queryAgendasDisplayOrder(params) {
  return request('/api/xadmin/v1/agendas/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

