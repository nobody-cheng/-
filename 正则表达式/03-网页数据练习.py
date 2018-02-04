import re

d = """<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div>
        <p>岗位职责:</p>
<p>1. 负责公司运维系统的开发和设计；</p>
<p>2. 负责公司系统标准化方案的设计与实施；</p>
<p>3. 负责公司运维自动化的设计与实施。</p>
<p>&nbsp;</p>
<p>岗位需求:</p>
<p>1. 计算机相关专业本科以上学历；</p>
<p>2. 精通Python语言，3年以上Python开发经验；</p>
<p>3. 熟练使用常用的Web框架Django, Flask, Tornado中的一个；</p>
<p>4. 熟悉Mysql数据库，熟悉Mongodb, Hadoop优先；</p>
<p>5. 掌握 MVC 架构，熟悉常用的设计模式,对web后端技术架构有很好的理解和规划能力；</p>
<p>6. 熟悉 Linux 、Redis、RabbitMQ；</p>
<p>7. 有良好的编码习惯，学习沟通能力强，能快速熟悉理解复杂业务；</p>
<p>8. 熟悉HTML、CSS、JavaScript等前端开发技术优先。</p>
        </div>
    </dd>
"""
result = re.sub(r'</?\w+>|&nbsp|\n', '', d)

# result = re.sub(r"<[^>]*>|&nbsp;|\n", "", d)

print(result)