(function(){"use strict";let a=null,o=!1,e=!1;const i={chapter1_series:`报名人数
100米    35
跳远     28
铅球     45
接力     22
跳高     38
Name: 报名人数, dtype: int64

报名人数最多的项目: 铅球
总报名人数: 168`,chapter1_dataframe:`   姓名      班级   项目  是否有体检报告
0  张三  高二(1)  100米       True
1  李四  高二(2)   跳远      False
2  王五  高二(1)   铅球       True
3  赵六  高二(3)  100米       True

表格形状: 4 行 × 4 列

各列数据类型:
姓名        object
班级        object
项目        object
是否有体检报告     bool
dtype: object`,chapter1_cleaning:`=== 原始脏数据 ===
    姓名      班级   年龄   项目
0  张三@#  高二(1)   16  100米
1   李四  高二(2)   17   跳远
2  王五*    None  999   铅球
3   李四  高二(2)   17   跳远
4   赵六  高二(3)   16  100米

=== 清洗后的干净数据 ===
   姓名      班级    年龄   项目
0  张三  高二(1)  16.0  100米
1  李四  高二(2)  17.0   跳远
2  王五    待确认   NaN   铅球
3  赵六  高二(3)  16.0  100米`,chapter2_plot:`图表已生成！在 Matplotlib 中运行此代码将显示柱状图。
最受欢迎的项目: 铅球 (45人)
总参与人次: 168`,chapter3_gui:`GUI 程序结构：
1. 创建窗口 → 2. 添加组件 → 3. 定义回调 → 4. 绑定按钮 → 5. 启动循环
run mainloop() 后会打开窗口并等待用户操作...`};let p=null;async function c(){if(!e){if(o){await p;return}o=!0;try{self.postMessage({type:"status",status:"loading",progress:5,message:"正在连接 Pyodide CDN..."}),importScripts("https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js"),self.postMessage({type:"status",status:"loading",progress:20,message:"Pyodide 核心加载完成，初始化解释器..."}),a=await c(),self.postMessage({type:"status",status:"loading",progress:50,message:"解释器就绪，加载 Pandas..."}),await a.loadPackage("micropip"),await a.pyimport("micropip").install("pandas"),self.postMessage({type:"status",status:"loading",progress:90,message:"Pandas 加载完成，最终初始化..."}),await a.runPythonAsync(`
import pandas as pd
import numpy as np
import json
`),e=!0,self.postMessage({type:"status",status:"ready",progress:100,message:"Python 环境就绪"})}catch(t){throw o=!1,e=!1,self.postMessage({type:"status",status:"error",progress:0,message:t.message}),t}}}p=c(),self.onmessage=async t=>{const{id:r,pythonCode:u,action:d}=t.data;if(d==="status"){self.postMessage({id:r,type:"status",status:e?"ready":o?"loading":"error",progress:e?100:0});return}if(d==="run"){if(!e)try{await p}catch(s){self.postMessage({id:r,error:"Python 环境加载失败: "+s.message,success:!1});return}try{const s=t.data.precomputedKey;if(s&&i[s]){const y=u.trim(),l={chapter1_series:`import pandas as pd

projects = pd.Series([35, 28, 45, 22, 38], index=['100米', '跳远', '铅球', '接力', '跳高'], name='报名人数')
print(projects)
print()
print(f'报名人数最多的项目: {projects.idxmax()}')
print(f'总报名人数: {projects.sum()}')`};if(l[s]&&y===l[s]){self.postMessage({id:r,results:i[s],success:!0,precomputed:!0});return}}const n=await a.runPythonAsync(u),g=n!=null?String(n):"(执行成功，无返回值)";self.postMessage({id:r,results:g,success:!0})}catch(s){self.postMessage({id:r,error:s.message,success:!1})}}}})();
