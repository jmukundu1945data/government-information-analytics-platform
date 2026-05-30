# Jonathan’s Analytics Engineering Human Oversight Checklist

Analytics engineering is not only about building pipelines, models, dashboards, and reports. It is also about applying human judgment to ensure that data products are realistic, semantically sound, operationally useful, and trustworthy.

This checklist captures the human oversight practices that should accompany analytics engineering work, especially when working with simulated data, dimensional models, Power BI semantic models, and dbt transformations.

## 1. Validate Business Realism — Never Trust Simulated Data Blindly

- Validate simulations against real-world institutional scale and operational context.
- Ensure analytical outputs make practical business sense.
- Check proportionality between ministries, provinces, programs, and indicators.

## 2. Validate Relationships — Never Assume Auto-Relationships Are Correct

- Manually review relationships created by Power BI.
- Verify filter propagation behavior.
- Keep cardinality clean and understandable.
- Remove unused dimensions from the active semantic model.

## 3. Understand Conformed Dimensions Properly

- Shared dimensions across facts are expected in enterprise analytics.
- A visually complex schema can still be architecturally correct.
- Focus on semantic correctness rather than visual neatness.

## 4. Use Proper Date Dimensions for Time Intelligence

- Use a dedicated `dim_date` table.
- Include `date_key`, `date`, `year`, `month`, `quarter`, and `year_month`.
- Connect all fact tables to the date dimension.

## 5. Maintain Naming Consistency

- Use consistent naming conventions across dimensions and facts.
- Prefer readable enterprise-style naming such as `date_key`.
- Avoid unnecessary semantic ambiguity.

## 6. Validate Conditional Formatting Logic Carefully

- Always test threshold logic visually.
- Remember Power BI percentages are stored as decimals.
- Validate KPI coloring against actual business rules.

## 7. Handle Data Quality Logic at the Database Layer

- Move complex DQ rules into SQL/dbt models.
- Keep Power BI visuals simple.
- Use exception tables/views for operational monitoring.

## 8. Validate Interactivity and Filter Context

- Test slicers and cross-filter behavior thoroughly.
- Most interactivity problems originate from semantic model design.
- Confirm visuals respond correctly to dimension filters.

## 9. Understand the Role of Measures

- Measures operate across the semantic model through relationships.
- Centralize reusable calculations in a dedicated measures table.
- Avoid duplicated logic across visuals.

## 10. Use AI as an Accelerator — Not as a Replacement for Thinking

- Use AI for scaffolding, refactoring, and repetitive work.
- Use human reasoning for architecture, semantics, and realism.
- Validate all AI-generated outputs carefully.

## 11. Understand That Enterprise Models Evolve Iteratively

- Enterprise analytics models improve gradually over time.
- Refactor confidently as understanding deepens.
- Continuous semantic improvement is normal.

## Final Reflection

> “The strongest interventions in this project were not coding interventions. They were semantic, architectural, business realism, and dimensional modeling interventions — the true foundation of analytics engineering.”
