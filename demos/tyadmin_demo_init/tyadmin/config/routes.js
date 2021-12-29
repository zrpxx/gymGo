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
        name: 'Demo',
        icon: 'BarsOutlined',
        path: '/xadmin/demo',
        routes:
        [
            {
                name: '全部字段非必填[被外键关联]',
                path: '/xadmin/demo/demo_foreign_key',
                component: './AutoGenPage/DemoForeignKeyList',
            },
            {
                name: '标签[被多对多关联]',
                path: '/xadmin/demo/tags',
                component: './AutoGenPage/TagsList',
            },
            {
                name: '分类[被外键关联]',
                path: '/xadmin/demo/category',
                component: './AutoGenPage/CategoryList',
            },
            {
                name: '富文本示例[关联外键，多对多标签]',
                path: '/xadmin/demo/rich_text_demo',
                component: './AutoGenPage/RichTextDemoList',
            },
            {
                name: '下拉选择示例(choices)',
                path: '/xadmin/demo/demo_model_require',
                component: './AutoGenPage/DemoModelRequireList',
            },
            {
                name: '全部字段类型-必填',
                path: '/xadmin/demo/demo_model',
                component: './AutoGenPage/DemoModelList',
            },
            {
                name: '全部字段类型-提供默认值',
                path: '/xadmin/demo/demo_default_model',
                component: './AutoGenPage/DemoDefaultModelList',
            },
            {
                name: '用户管理',
                path: '/xadmin/demo/user_profile',
                component: './AutoGenPage/UserProfileList',
            },
            {
                name: 'agendas',
                path: '/xadmin/demo/agendas',
                component: './AutoGenPage/AgendasList',
            },
            {
                name: 'archive body data',
                path: '/xadmin/demo/archive_body_data',
                component: './AutoGenPage/ArchiveBodyDataList',
            },
            {
                name: 'attends',
                path: '/xadmin/demo/attends',
                component: './AutoGenPage/AttendsList',
            },
            {
                name: 'bills',
                path: '/xadmin/demo/bills',
                component: './AutoGenPage/BillsList',
            },
            {
                name: 'body data',
                path: '/xadmin/demo/body_data',
                component: './AutoGenPage/BodyDataList',
            },
            {
                name: 'buys',
                path: '/xadmin/demo/buys',
                component: './AutoGenPage/BuysList',
            },
            {
                name: 'check logs',
                path: '/xadmin/demo/check_logs',
                component: './AutoGenPage/CheckLogsList',
            },
            {
                name: 'lockers',
                path: '/xadmin/demo/lockers',
                component: './AutoGenPage/LockersList',
            },
            {
                name: 'reviews',
                path: '/xadmin/demo/reviews',
                component: './AutoGenPage/ReviewsList',
            },
            {
                name: 'visits',
                path: '/xadmin/demo/visits',
                component: './AutoGenPage/VisitsList',
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
