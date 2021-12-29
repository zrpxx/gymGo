import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryReviews(params) {
  return request('/api/xadmin/v1/reviews', {
    params,
  });
}
export async function removeReviews(params) {
  return request(`/api/xadmin/v1/reviews/${params}`, {
    method: 'DELETE',
  });
}
export async function addReviews(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/reviews', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateReviews(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/reviews/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryReviewsVerboseName(params) {
  return request('/api/xadmin/v1/reviews/verbose_name', {
    params,
  });
}
export async function queryReviewsListDisplay(params) {
  return request('/api/xadmin/v1/reviews/list_display', {
    params,
  });
}
export async function queryReviewsDisplayOrder(params) {
  return request('/api/xadmin/v1/reviews/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

