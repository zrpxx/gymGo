import request from '@/utils/request';

export async function query() {
  return request('/api/xadmin/v1/users');
}
export async function queryCurrent() {
  return request('/api/xadmin/v1/currentUser');
}
export async function queryNotices() {
  return request('/api/xadmin/v1/notices');
}

export async function queryMenu(user_id) {
  return request('/api/xadmin/v1/sys/menu?user_id='+user_id);
}

export async function queryCount() {
  return request('/api/xadmin/v1/dashboard');
}