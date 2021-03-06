## 动态规划
>1.思路方向

刷表法--考虑每个状态影响到的状态
填表法--考虑每个状态的依赖
状态方向：has/remain
*完全背包问题*
- 总体积不超过T的情况下最大重量dp[T]=dp[T-v[i]]+w[i]

- 总体积剩余T时最大重量dp[T]=dp[T-v[i]]+w[i]

- ~~总体积达到T后还剩余的最大重量dp[T]=dp[T+v[i]]+w[i]~~


#### `这时可以综合考虑刷表/填表法需要啊考虑的因素区别+思考方向是否习惯,另一方面可根据搜索元素的顺序调整内外循环顺序,如下`
```cpp
for(i=0;i<m;++i)for(j=t-v[i].g;j>=0;--j)
dp[j]=max(dp[j],dp[j+g[i]]+w[i]);
```
`小结:`

#### (1)最后的处理
如果聚零为整(不断累加背包，看影响后面的价值)，最后要求min/max_element-->

如果化整为零(最大容量减少),最后只需求端点值

#### (2)涉及求字典序(或涉及dp的序号获取)

法1:去掉不可达结点，初始化为-inf(max)inf(min)

法2:加入实际has数组

>2.经典模型总结
- 线性dp
*LCS最大连续子序列和*
#### 连续关系-->一位递推，看末位
*LIS最大上升子序列*
#### 每次刷新(长度不变时让某位更小)
```cpp
for(i=0;i<n;++i){
    scanf("%d",&m);
    fill(dp,dp+40000,60000);
    for(j=0;j<m;++j){
        scanf("%d",&x);
        *lower_bound(dp,dp+m,x)=x;
    }
    printf("%d\n",lower_bound(dp,dp+m,60000)-dp);
}
```
*LCS最长公共子序列*
#### 看两个末尾(交叉型+递推型，加个空间保存上一行即可)
```cpp
for(int i=0;i<strlen(a);++i){
    for(int j=0;j<strlen(b);++j){
        if(a[i]==b[j])dp[j]=(j-1<0?0:last[j-1])+1;
        else dp[j]=max(j-1<0?0:dp[j-1],last[j]);
    }
    last=dp;
}
printf("%d\n",dp[strlen(b)-1]);
```
*完全背包*
#### 递推被前面结果影响
```cpp
for(int i=0;i<m;++i){
    scanf("%d%d",&v,&p);
    for(int j=n;j>=v;--j)
    dp[j]=max(dp[j],dp[j-v]+v*p);
}
printf("%d",dp[n]);
```
*01背包*
#### 递推不能被前面结果影响
```cpp
for(i=0;i<m;++i)scanf("%d%d",&g[i],&w[i]);
for(i=0;i<m;++i)for(j=t-v[i].g;j>=0;--j)
dp[j]=max(dp[j],dp[j+g[i]]+w[i]);
printf("%d",dp[0]);
```

- 树形dp