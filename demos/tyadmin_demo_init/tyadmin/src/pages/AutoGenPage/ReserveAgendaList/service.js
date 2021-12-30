import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryReserveAgenda(params) {
  return request('/api/xadmin/v1/reserve_agenda', {
    params,
  });
}
export async function removeReserveAgenda(params) {
  return request(`/api/xadmin/v1/reserve_agenda/${params}`, {
    method: 'DELETE',
  });
}
export async function addReserveAgenda(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/reserve_agenda', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateReserveAgenda(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/reserve_agenda/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryReserveAgendaVerboseName(params) {
  return request('/api/xadmin/v1/reserve_agenda/verbose_name', {
    params,
  });
}
export async function queryReserveAgendaListDisplay(params) {
  return request('/api/xadmin/v1/reserve_agenda/list_display', {
    params,
  });
}
export async function queryReserveAgendaDisplayOrder(params) {
  return request('/api/xadmin/v1/reserve_agenda/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

