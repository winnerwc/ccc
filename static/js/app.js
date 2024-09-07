$(document).ready(function () {
    // 默认显示 Projects 页面
    console.log("00001");
    showPage('projects');

    // 绑定点击事件
    $('#baselinesLink').click(function () {
        console.log("2222");
        $('#'+"projectsBody").empty()
        showPage('baselines');
    });

    $('#projectsLink').click(function () {
        console.log("1111");
        $('#'+"baselinesBody").empty()
        showPage('projects');
    });

    // 绑定按钮点击事件
    $('#getBaselinesButton').click(function () {

        fetchBaselinesData();
    });

    $('#getProjectsButton').click(function () {
        fetchProjectsData();
    });

    function showPage(page) {
        if (page === 'baselines') {
            $('#baselinesPage').show();
            $('#projectsPage').hide();
            $('.nav-link').removeClass('active');
            $('#baselinesLink').addClass('active');
        } else if (page === 'projects') {
            $('#baselinesPage').hide();
            $('#projectsPage').show();
            $('.nav-link').removeClass('active');
            $('#projectsLink').addClass('active');
        }
    }

    $('#queryProjectsButton').click(function () {
        var projectName = $('#projectNameInput').val().trim();
        if (projectName) {
            fetchProjectsData(projectName);
        } else {
            alert('请输入项目名称！');
        }
    });

    // 通过 AJAX 获取 Baselines 数据
    function fetchBaselinesData() {
        $.ajax({
            url: '/baselines',
            method: 'GET',
            success: function (data) {
                console.log('Baselines data:', data);
                populateTable('baselinesBody', data);
            },
            error: function (error) {
                console.error('Error fetching baselines:', error);
            }
        });
    }

    // 通过 AJAX 获取 Projects 数据
    function fetchProjectsData(projectName) {
        $.ajax({
            url: `/projects/${projectName}`,
            method: 'GET',
            success: function (data) {
                console.log('Projects data:', data);
                populateTable('projectsBody', data);
            },
            error: function (error) {
                console.error('Error fetching projects:', error);
            }
        });
    }

    // 示例数据填充函数
    function populateTable(tableId, data) {
        console.log(`Data for ${tableId}:`, data);
        if (!Array.isArray(data)) {
            console.error(`${tableId} data is not an array.`);
            return;
        }

        $('#' + tableId).empty();
        data.forEach(function (row) {
            var newRow = '';
            if (tableId === 'baselinesBody') {
                newRow = `
                    <tr>
                        <td>${row.id}</td>
                        <td>${row.baseline_name}</td>
                        <td>${row.baseline_status}</td>
                        <td>${row.owner}</td>
                        <td>${new Date(row.timestamp).toLocaleString()}</td>
                    </tr>
                `;
            } else if (tableId === 'projectsBody') {
                newRow = `
                    <tr>
                        <td>${row.id}</td>
                        <td>${row.project_name}</td>
                        <td>${row.job_name}</td>
                        <td>${row.job_num}</td>
                        <td>${row.job_status}</td>
                        <td>${row.fail_reason || ''}</td>
                        <td>${row.owner}</td>
                        <td>${new Date(row.time).toLocaleString()}</td>
                    </tr>
                `;
            }
            $('#' + tableId).append(newRow);
        });
    }
    $('#submitBaselineButton').click(function (event) {
                event.preventDefault(); // 阻止表单默认提交行为

                var baselineName = $('#baselineNameInput').val();
                var baseline_status = $('#statusInput').val();
                var owner = $('#ownerInput').val();
                var time = new Date().toISOString(); // 获取当前时间

                // AJAX POST 请求提交数据
                $.ajax({
                    url: '/baseline',
                    method: 'POST',
                    data: JSON.stringify({baseline_name: baselineName, baseline_status: baseline_status, owner: owner, time: time}),
                    contentType: 'application/json',
                    success: function (response) {
                        alert('Baseline added successfully!');
                        // 重新加载数据
                        $('#fetchDataButton').click();
                    },
                    error: function (error) {
                        console.error('Error adding baseline:', error);
                        alert('Failed to add baseline. Please check the console for more details.');
                    }
                });
            });
            $('#searchForm').on('submit', function (event) {
                event.preventDefault(); // 阻止表单默认提交行为
                var projectName = $('#projectNameInput').val();
                  // 发送 AJAX GET 请求
                $.ajax({
                    url: `/projects/${projectName}`, // 假设你的后端接口路径是这样的
                    method: 'GET',
                    success: function (data) {
                        // 清空现有的表格行
                        $('#resultsBody').empty();

                        // 动态填充表格
                        $.each(data, function (index, project) {
                            var row = `
                                <tr>
                                    <td>${project.id}</td>
                                    <td>${project.project_name}</td>
                                    <td>${project.job_name}</td>
                                    <td>${project.job_num}</td>
                                    <td>${project.job_status}</td>
                                    <td>${project.fail_reason}</td>
                                    <td>${project.owner}</td>
                                    <td>${new Date(project.time).toLocaleString()}</td>
                                </tr>
                            `;
                            $('#resultsBody').append(row);
                        });
                    },
                    error: function (error) {
                        console.error('Error fetching data:', error);
                        alert('Failed to fetch data. Please check the console for more details.');
                    }
                });
            });
            $('#submitJobButton').click(function (event) {
                event.preventDefault(); // 阻止表单默认提交行为

                var baselineName = $('#baselineNameInput').val();
                var baseline_status = $('#statusInput').val();
                var owner = $('#ownerInput').val();
                var time = new Date().toISOString(); // 获取当前时间

                // AJAX POST 请求提交数据
                $.ajax({
                    url: '/',
                    method: 'POST',
                    data: JSON.stringify({baseline_name: baselineName, baseline_status: baseline_status, owner: owner, time: time}),
                    contentType: 'application/json',
                    success: function (response) {
                        alert('Baseline added successfully!');
                        // 重新加载数据
                        $('#fetchDataButton').click();
                    },
                    error: function (error) {
                        console.error('Error adding baseline:', error);
                        alert('Failed to add baseline. Please check the console for more details.');
                    }
                });
            });
            $('#searchForm').on('submit', function (event) {
                event.preventDefault(); // 阻止表单默认提交行为
                var projectName = $('#projectNameInput').val();
                  // 发送 AJAX GET 请求
                $.ajax({
                    url: `/projects/${projectName}`, // 假设你的后端接口路径是这样的
                    method: 'GET',
                    success: function (data) {
                        // 清空现有的表格行
                        $('#resultsBody').empty();

                        // 动态填充表格
                        $.each(data, function (index, project) {
                            var row = `
                                <tr>
                                    <td>${project.id}</td>
                                    <td>${project.project_name}</td>
                                    <td>${project.job_name}</td>
                                    <td>${project.job_num}</td>
                                    <td>${project.job_status}</td>
                                    <td>${project.fail_reason}</td>
                                    <td>${project.owner}</td>
                                    <td>${new Date(project.time).toLocaleString()}</td>
                                </tr>
                            `;
                            $('#resultsBody').append(row);
                        });
                    },
                    error: function (error) {
                        console.error('Error fetching data:', error);
                        alert('Failed to fetch data. Please check the console for more details.');
                    }
                });
            });
});