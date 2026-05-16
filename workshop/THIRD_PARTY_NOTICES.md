# Third-Party Notices

老爱同学，本文件记录本 workshop 借用的第三方上游项目及其许可证信息。

## 借用的上游项目

### microsoft/TechWorkshop-L300-AI-Apps-and-agents

- **仓库**：<https://github.com/microsoft/TechWorkshop-L300-AI-Apps-and-agents>
- **许可证**：MIT License
- **Copyright**：Microsoft Corporation

#### 借用范围

借用为**思路 / 结构参考**，不直接 vendor 上游源代码：

| 本 workshop 模块 | 借用内容 |
| --- | --- |
| D3 | Bicep 模板结构思路（上游 Ex01） |
| D6a | SDK 路径跑通基线（上游 Ex03 第一段） |
| D6b | A2A server 实现参考（上游 Ex03） |
| D7 | multi-agent 编排参考（上游 Ex02 多 agent 段） |
| D8 | 红队 SDK 调用模式（上游 Ex06） |
| D9 | GitHub Actions workflow 思路（上游 Ex05） |

详细对照见 [`../docs/03-workshop-fork-mapping.md`](../docs/03-workshop-fork-mapping.md)。

#### 说明

本 workshop 当前阶段不直接 vendor 上游代码，仅作为思路 / 结构参考；**具体代码 fork 实操阶段**才会落地引入，届时具体文件会在文件头或邻近位置标注 attribution（指明来源文件、commit、许可证）。

---

## MIT License 全文

以下为 MIT 许可证原文（保留英文）：

```
MIT License

Copyright (c) Microsoft Corporation.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
