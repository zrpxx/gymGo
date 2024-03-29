[
    {
        name: 'Home',
        path: '/xadmin/index',
        icon: 'dashboard',
        component: './TyAdminBuiltIn/DashBoard'
    },
    {
        path: '/xadmin/',
        redirect: '/xadmin/index',
    },
    {
        name: 'Authentication and Authorization',
        icon: 'BarsOutlined',
        path: '/xadmin/auth',
        routes:
        [
            {
                name: 'permission',
                path: '/xadmin/auth/permission',
                component: './AutoGenPage/PermissionList',
            },
            {
                name: 'group',
                path: '/xadmin/auth/group',
                component: './AutoGenPage/GroupList',
            }
        ]
    },
    {
        name: 'Api',
        icon: 'BarsOutlined',
        path: '/xadmin/api',
        routes:
        [
            {
                name: '用户管理',
                path: '/xadmin/api/user',
                component: './AutoGenPage/UserList',
            },
            {
                name: '区域管理',
                path: '/xadmin/api/zones',
                component: './AutoGenPage/ZonesList',
            },
            {
                name: '顾客信息管理',
                path: '/xadmin/api/customers',
                component: './AutoGenPage/CustomersList',
            },
            {
                name: '日程管理',
                path: '/xadmin/api/agendas',
                component: './AutoGenPage/AgendasList',
            },
            {
                name: '身体数据（存档）',
                path: '/xadmin/api/archive_body_data',
                component: './AutoGenPage/ArchiveBodyDataList',
            },
            {
                name: '账单管理',
                path: '/xadmin/api/bills',
                component: './AutoGenPage/BillsList',
            },
            {
                name: '身体数据',
                path: '/xadmin/api/body_data',
                component: './AutoGenPage/BodyDataList',
            },
            {
                name: '课程管理',
                path: '/xadmin/api/curriculums',
                component: './AutoGenPage/CurriculumsList',
            },
            {
                name: '课程参加记录管理',
                path: '/xadmin/api/attends',
                component: './AutoGenPage/AttendsList',
            },
            {
                name: '课余量管理',
                path: '/xadmin/api/buys',
                component: './AutoGenPage/BuysList',
            },
            {
                name: '设备管理',
                path: '/xadmin/api/equipment',
                component: './AutoGenPage/EquipmentList',
            },
            {
                name: '维护日志',
                path: '/xadmin/api/check_logs',
                component: './AutoGenPage/CheckLogsList',
            },
            {
                name: '柜子管理',
                path: '/xadmin/api/lockers',
                component: './AutoGenPage/LockersList',
            },
            {
                name: '评论管理',
                path: '/xadmin/api/reviews',
                component: './AutoGenPage/ReviewsList',
            },
            {
                name: '设备预约',
                path: '/xadmin/api/reserve_equipment',
                component: './AutoGenPage/ReserveEquipmentList',
            },
            {
                name: '教练日程预约',
                path: '/xadmin/api/reserve_agenda',
                component: './AutoGenPage/ReserveAgendaList',
            }
        ]
    },
    {
        name: 'TyadminBuiltin',
        icon: 'VideoCamera',
        path: '/xadmin/sys',
        routes:
        [
            {
                name: 'TyAdminLog',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_sys_log',
                component: './TyAdminBuiltIn/TyAdminSysLogList'
            },
            {
                name: 'TyAdminVerify',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_email_verify_record',
                component: './TyAdminBuiltIn/TyAdminEmailVerifyRecordList'
            }
        ]
    },
    {
        name: 'passwordModify',
        path: '/xadmin/account/change_password',
        hideInMenu: true,
        icon: 'dashboard',
        component: './TyAdminBuiltIn/ChangePassword',
    },
    {
        component: './404',
    },
]
